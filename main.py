# main.py

from pathfinder import show_menu
from scores import get_team_results
from premier_league_standings import display_standings

def run_tracker():
    while True:
        choice = show_menu()

        if choice == "1":
            display_standings()
        elif choice == "2":
            team = input("Enter a team name: ")
            get_team_results(team)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    run_tracker()
