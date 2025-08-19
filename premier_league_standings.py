standings = [
    {"pos": 1, "team": "Liverpool", "pts": 84, "gd": 45, "note": "Champions 🏆"},
    {"pos": 2, "team": "Arsenal", "pts": 74, "gd": 35, "note": "Champions League"},
    {"pos": 3, "team": "Manchester City", "pts": 71, "gd": 28, "note": "Champions League"},
    {"pos": 4, "team": "Chelsea", "pts": 69, "gd": 21, "note": "Champions League"},
    {"pos": 5, "team": "Newcastle United", "pts": 66, "gd": 21, "note": "Champions League"},
    {"pos": 6, "team": "Aston Villa", "pts": 66, "gd": 7, "note": "Europa League"},
    {"pos": 7, "team": "Nottingham Forest", "pts": 65, "gd": 12, "note": "Conference League"},
    {"pos": 8, "team": "Brighton & Hove Albion", "pts": 61, "gd": 7, "note": ""},
    {"pos": 9, "team": "Bournemouth", "pts": 56, "gd": 12, "note": ""},
    {"pos": 10, "team": "Brentford", "pts": 56, "gd": 9, "note": ""},
    {"pos": 11, "team": "Fulham", "pts": 54, "gd": 0, "note": ""},
    {"pos": 12, "team": "Crystal Palace", "pts": 53, "gd": 0, "note": "Europa League via FA Cup"},
    {"pos": 13, "team": "Everton", "pts": 48, "gd": -2, "note": ""},
    {"pos": 14, "team": "West Ham United", "pts": 43, "gd": -16, "note": ""},
    {"pos": 15, "team": "Manchester United", "pts": 42, "gd": -10, "note": ""},
    {"pos": 16, "team": "Wolves", "pts": 42, "gd": -15, "note": ""},
    {"pos": 17, "team": "Tottenham Hotspur", "pts": 38, "gd": -1, "note": "Champions League via Europa League win"},
    {"pos": 18, "team": "Leicester City", "pts": 25, "gd": -47, "note": "Relegated"},
    {"pos": 19, "team": "Ipswich Town", "pts": 22, "gd": -46, "note": "Relegated"},
    {"pos": 20, "team": "Southampton", "pts": 12, "gd": -60, "note": "Relegated"}
]

def display_standings():
    print("\n🏆 Final Premier League Standings – 2024–25 Season 🏆")
    print("=" * 75)
    print(f"{'Pos':<4} {'Team':<25} {'PTS':<5} {'GD':<5} Notes")
    print("-" * 75)
    for team in standings:
        print(f"{team['pos']:<4} {team['team']:<25} {team['pts']:<5} {team['gd']:<5} {team['note']}")

if __name__ == "__main__":
    display_standings()
