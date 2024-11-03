import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_player_found(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")

    def test_search_player_not_found(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team_with_existing_players(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_team_with_no_players(self):
        players = self.stats.team("ABCD")
        self.assertEqual(len(players), 0)

    def test_top_players_more_than_available(self):
        top_players = self.stats.top(10)
        self.assertEqual(len(top_players), 5)

    def test_top_players_by_points(self):
        top_players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")

    def test_top_players_by_goals(self):
        top_players = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")

    def test_top_players_by_assists(self):
        top_players = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Yzerman")

    def test_top_players_default_sorting(self):
        top_players = self.stats.top(2)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")

