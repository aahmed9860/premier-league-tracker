# scores.py

# Manchester United 2024–25 Premier League results
team_results_2024_25 = {
    "Manchester United": [
        {"date": "May 25, 2025", "opponent": "Aston Villa", "score": "2‑0"},
        {"date": "May 11, 2025", "opponent": "West Ham United", "score": "0‑2"},
        {"date": "May 4, 2025", "opponent": "Brentford", "score": "3‑4"},
        {"date": "Apr 27, 2025", "opponent": "Bournemouth", "score": "1‑1"},
        {"date": "Apr 20, 2025", "opponent": "Wolves", "score": "0‑1"},
        {"date": "Apr 13, 2025", "opponent": "Newcastle United", "score": "1‑4"},
        {"date": "Apr 6, 2025", "opponent": "Manchester City", "score": "0‑0"},
        {"date": "Apr 1, 2025", "opponent": "Nottingham Forest", "score": "0‑1"},
        {"date": "Mar 16, 2025", "opponent": "Leicester City", "score": "3‑0"},
        {"date": "Mar 9, 2025", "opponent": "Arsenal", "score": "1‑1"},
        {"date": "Feb 26, 2025", "opponent": "Ipswich Town", "score": "3‑2"},
        {"date": "Feb 22, 2025", "opponent": "Everton", "score": "2‑2"},
        {"date": "Feb 16, 2025", "opponent": "Tottenham", "score": "0‑1"},
        {"date": "Feb 2, 2025", "opponent": "Crystal Palace", "score": "0‑2"},
        {"date": "Jan 26, 2025", "opponent": "Fulham", "score": "1‑0"},
        {"date": "Jan 19, 2025", "opponent": "Brighton", "score": "1‑3"},
        {"date": "Jan 16, 2025", "opponent": "Southampton", "score": "3‑1"},
        {"date": "Jan 5, 2025", "opponent": "Liverpool", "score": "2‑2"},
        {"date": "Dec 30, 2024", "opponent": "Newcastle United", "score": "0‑2"},
        {"date": "Dec 26, 2024", "opponent": "Wolves", "score": "0‑2"},
        {"date": "Dec 22, 2024", "opponent": "Bournemouth", "score": "0‑3"},
        {"date": "Dec 15, 2024", "opponent": "Manchester City", "score": "2‑1"},
        {"date": "Dec 7, 2024", "opponent": "Nottingham Forest", "score": "2‑3"},
        {"date": "Dec 1, 2024", "opponent": "Everton", "score": "4‑0"},
        {"date": "Nov 10, 2024", "opponent": "Leicester City", "score": "3‑0"},
        {"date": "Nov 3, 2024", "opponent": "Chelsea", "score": "1‑1"},
        {"date": "Oct 27, 2024", "opponent": "West Ham United", "score": "1‑2"},
        {"date": "Oct 19, 2024", "opponent": "Brentford", "score": "2‑1"},
        {"date": "Oct 6, 2024", "opponent": "Aston Villa", "score": "0‑0"},
        {"date": "Sept 29, 2024", "opponent": "Tottenham", "score": "0‑3"},
        {"date": "Sept 21, 2024", "opponent": "Crystal Palace", "score": "0‑0"},
        {"date": "Sept 14, 2024", "opponent": "Southampton", "score": "3‑0"},
        {"date": "Sept 1, 2024", "opponent": "Liverpool", "score": "0‑3"},
        {"date": "Aug 24, 2024", "opponent": "Brighton", "score": "1‑2"},
        {"date": "Aug 16, 2024", "opponent": "Fulham", "score": "1‑0"}
    ]
}


def get_team_results(team_name):
    team = team_name.strip().title()
    results = team_results_2024_25.get(team)

    if not results:
        print(f"\n❌ No results found for {team}.")
        return

    print(f"\n📅 {team}'s 2024–25 Premier League Results:")
    for match in results:
        print(f"{match['date']}: vs {match['opponent']} – {match['score']}")


# Example usage
if __name__ == "__main__":
    name = input("Enter team name (e.g., Manchester United): ").strip()
    get_team_results(name)

