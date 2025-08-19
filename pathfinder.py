# pathfinder.py

from scores import get_team_results
from premier_league_standings import display_standings

def show_menu():
    print("\n⚽ Premier League Tracker Menu:")
    print("1. View Final League Standings")
    print("2. View a Team’s Season Results")
    print("3. Exit")

    choice = input("Enter your choice (1–3): ")
    return choice
