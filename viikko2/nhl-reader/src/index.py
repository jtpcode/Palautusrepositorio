import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()
    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == 'FIN':
            players.append(player)
    
    def sort_by(player):
        return player.points

    sorted_players = sorted(players,
                            reverse=True,
                            key=sort_by)

    print("Players from FIN\n")

    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    main()
