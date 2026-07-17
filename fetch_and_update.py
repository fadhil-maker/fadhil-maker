import os
import requests
import json
from generate_stats import generate_stats_svg
from generate_langs import generate_langs_svg
from generate_trophies import generate_trophies_svg

def main():
    username = os.environ.get("GITHUB_ACTOR", "fadhil-maker")
    token = os.environ.get("GITHUB_TOKEN")

    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    print(f"Fetching stats for {username}...")

    # Fetch User Stats (REST)
    user_resp = requests.get(f"https://api.github.com/users/{username}", headers=headers)
    if user_resp.status_code != 200:
        print("Failed to fetch user:", user_resp.text)
        return
    user_data = user_resp.json()
    followers = user_data.get("followers", 0)
    repos_count = user_data.get("public_repos", 0)

    # Fetch Repos to calculate Stars and Languages (REST)
    repos_url = f"https://api.github.com/users/{username}/repos?per_page=100"
    repos_resp = requests.get(repos_url, headers=headers)
    repos_data = repos_resp.json() if repos_resp.status_code == 200 else []

    total_stars = sum(repo.get("stargazers_count", 0) for repo in repos_data)

    # Count languages
    lang_counts = {}
    for repo in repos_data:
        lang = repo.get("language")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1

    # In a perfect world we would fetch the language bytes from each repo, 
    # but for simplicity we will just count the primary language of each repo.
    total_langs = sum(lang_counts.values())
    if total_langs == 0:
        lang_counts = {"Python": 1, "Django": 1, "React": 1, "Docker": 1}
        total_langs = 4

    sorted_langs = sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)
    top_4 = sorted_langs[:4]

    # Map colors for top languages
    colors = {
        "Python": "#3b82f6",
        "JavaScript": "#fde047",
        "TypeScript": "#3178c6",
        "HTML": "#e34c26",
        "CSS": "#563d7c",
        "React": "#06b6d4",
        "Docker": "#f59e0b",
        "Java": "#b07219",
        "C++": "#f34b7d",
        "C": "#555555"
    }

    langs_param = []
    # If less than 4, pad
    while len(top_4) < 4:
        top_4.append(("Other", 0))

    for name, count in top_4:
        pct = (count / total_langs) * 100 if total_langs > 0 else 0
        color = colors.get(name, "#0ea5e9") # Default to Cyber Tech Light Blue
        langs_param.append({'name': name, 'pct': pct, 'color': color})

    # Fetch Commits using GraphQL (if token is available)
    total_commits = 0
    if token:
        graphql_query = """
        query {
          user(login: "%s") {
            contributionsCollection {
              totalCommitContributions
            }
          }
        }
        """ % username
        g_resp = requests.post(
            "https://api.github.com/graphql",
            json={"query": graphql_query},
            headers=headers
        )
        if g_resp.status_code == 200:
            g_data = g_resp.json()
            try:
                total_commits = g_data["data"]["user"]["contributionsCollection"]["totalCommitContributions"]
            except Exception:
                pass

    if total_commits == 0:
        total_commits = 1200 # Fallback 

    print(f"Stats - Stars: {total_stars}, Commits: {total_commits}, Repos: {repos_count}, Followers: {followers}")

    # Determine Rank for Stats
    rank = "S" if total_stars >= 100 or total_commits >= 1000 else ("A" if total_stars >= 40 else "B")
    
    # Generate SVGs
    # Stats expects string formatted with + etc if desired, we'll format them:
    s_stars = f"{total_stars}"
    s_commits = f"{total_commits}"
    if total_commits >= 1000:
        s_commits = f"{total_commits/1000:.1f}K"
    s_repos = f"{repos_count}"
    s_followers = f"{followers}"
    
    generate_stats_svg(s_stars, s_commits, s_repos, s_followers, "12+", rank)
    generate_langs_svg(langs_param)
    generate_trophies_svg(total_stars, total_commits, repos_count, followers)
    
if __name__ == "__main__":
    main()
