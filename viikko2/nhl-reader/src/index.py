from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    console = Console()

    url = "https://studies.cs.helsinki.fi/nhlstats/"

    console.print("NHL statistics by nationality\n", style="italic")
    seasons = ["2018-19", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    while True:
        season = Prompt.ask("""Select season [magenta][2018-19/2020-21/2021-22/2022-23/2023-24/2024-25/][/magenta]""")
        if season in seasons:
            break

    url += f"{season}/players"
    nationalities = ["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS", "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"]
    nationality = ""

    while True:
        nationality = Prompt.ask("""Select nationality[magenta][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR][/magenta]""")
        if nationality == "exit":
            break
        if nationality not in nationalities:
            continue

        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}", header_style="white",
                      title_style="italic", show_header=True)
        table.add_column("name")
        table.add_column("team", justify="left")
        table.add_column("goals", justify="right")
        table.add_column("assists", justify="right")
        table.add_column("points", justify="right")

        for p in players:
            table.add_row(f"[cyan]{p.name}[/cyan]", f"[purple]{p.team}[/purple]",
                          f"[green]{p.goals}[/green]", f"[green]{p.assists}[/green]",
                          f"[green]{p.points}[/green]")

        console.print(table)


if __name__ == "__main__":
    main()
