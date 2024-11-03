import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_hakee_pelaajaolion(self):
        self.assertEqual(isinstance(self.stats.search("Semenko"), Player), True)
    
    def test_search_ei_palauta_olematonta_pelaajaoliota(self):
        self.assertEqual(self.stats.search("dingdong"), None)

    