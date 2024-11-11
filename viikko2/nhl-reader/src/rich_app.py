from rich import print
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

class RichApp:
    def __init__(self):
        self.url_template = "https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        self.seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
        self.nationalities = ["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS", "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"]

    def select_season(self):
        print("Select season", f"[bold magenta]{self.seasons}", end=": ")
        season = input()
        if season not in self.seasons:
            print("[bold red]Invalid season![/bold red] Try again.")
            return self.select_season()
        return season

    def select_nationality(self):
        print("Select nationality", f"[bold magenta]{self.nationalities}", end=": ")
        nationality = input().upper()
        if nationality not in self.nationalities:
            print("[bold red]Invalid nationality![/bold red] Try again.")
            return self.select_nationality()
        return nationality

    def display_stats(self, players):
        table = Table(title=f"Top scorers of {self.nationality} season {self.season}")
        table.add_column("name", style="cyan", justify="left")
        table.add_column("team", style="magenta")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

        print(table)

    def run(self):
        self.season = self.select_season()
        self.nationality = self.select_nationality()

        url = self.url_template.format(season=self.season)
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        
        players = stats.top_scorers_by_nationality(self.nationality)
        
        self.display_stats(players)