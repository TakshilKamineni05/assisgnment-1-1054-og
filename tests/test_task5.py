from unittest import TestCase

from ed_utils.decorators import number, visibility
from data_structures.referential_array import ArrayR

from game import Game
from game_stats import GameStats, StatsColumn
from random_gen import RandomGen
from player import Player
from constants import Constants


class TestTask5(TestCase):

    def setUp(self) -> None:
        self.players: ArrayR[Player] = ArrayR(8)
        self.players[0] = Player("Alice", 0)
        self.players[1] = Player("Bob", 1)
        self.players[2] = Player("Charlie", 2)
        self.players[3] = Player("David", 3)
        self.players[4] = Player("Eve", 4)
        self.players[5] = Player("Frank", 5)
        self.players[6] = Player("Grace", 6)
        self.players[7] = Player("Helen", 7)

    @number("5.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_init(self) -> None:
        stats: GameStats = GameStats(self.players)
        self.assertEqual(len(stats), 8)
        for i in range(8):
            self.assertEqual(stats.players[i].name, self.players[i].name)
            self.assertEqual(stats.stats[i][0], self.players[i].name)
            for j in range(1, 7):
                self.assertEqual(stats.stats[i][j], 0)

    @number("5.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_add_player(self) -> None:
        stats: GameStats = GameStats(self.players[0:2])
        player: Player = Player("Ivy", 3)
        stats.add_player(player)
        self.assertEqual(len(stats),3)
        self.assertEqual(stats.players[2].name, player.name)
        self.assertEqual(stats.stats[2][0], player.name)
        for j in range(1, 7):
            self.assertEqual(stats.stats[2][j], 0)

    @number("5.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_recording_of_stats(self) -> None:
        stats: GameStats = GameStats(self.players)
        player: Player = self.players[0]
        stats.record_game_played(player)
        stats.record_turn(player)
        stats.record_card_played(player)
        stats.record_card_drawn(player)
        stats.record_game_won(player)
        self.assertEqual(stats.stats[0][1], 1)
        self.assertEqual(stats.stats[0][2], 1)
        self.assertEqual(stats.stats[0][3], 1)
        self.assertEqual(stats.stats[0][4], 1)
        self.assertEqual(stats.stats[0][6], 1)

    @number("5.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_updating_stats_after_game(self) -> None:
        RandomGen.set_seed(123)
        Constants.NUM_CARDS_AT_INIT = 2
        game: Game = Game()
        game.initialise_game(self.players[0:4])
        _ = game.play_game()
        stats: GameStats = game.game_stats

        # Check the stats of all the players
        expected_stats: ArrayR[ArrayR] = ArrayR(8)

        # Add the expected stats

        """
        Name    Games Played    Turns Taken     Cards Played    Cards Drawn     Cards Left      Games Won
        Alice           1               4               2               6               6               0
        Bob             1               4               2               3               3               0
        Charlie         1               5               4               3               1               0
        David           1               3               3               1               0               1
        """

        # Add the stats for Alice
        expected_stats[0] = ArrayR(7)
        expected_stats[0][0] = "Alice"
        expected_stats[0][1] = 1
        expected_stats[0][2] = 4
        expected_stats[0][3] = 2
        expected_stats[0][4] = 6
        expected_stats[0][5] = 6
        expected_stats[0][6] = 0

        # Add the stats for Bob
        expected_stats[1] = ArrayR(7)
        expected_stats[1][0] = "Bob"
        expected_stats[1][1] = 1
        expected_stats[1][2] = 4
        expected_stats[1][3] = 2
        expected_stats[1][4] = 3
        expected_stats[1][5] = 3
        expected_stats[1][6] = 0

        # Add the stats for Charlie
        expected_stats[2] = ArrayR(7)
        expected_stats[2][0] = "Charlie"
        expected_stats[2][1] = 1
        expected_stats[2][2] = 5
        expected_stats[2][3] = 4
        expected_stats[2][4] = 3
        expected_stats[2][5] = 1
        expected_stats[2][6] = 0

        # Add the stats for David
        expected_stats[3] = ArrayR(7)
        expected_stats[3][0] = "David"
        expected_stats[3][1] = 1
        expected_stats[3][2] = 3
        expected_stats[3][3] = 3
        expected_stats[3][4] = 1
        expected_stats[3][5] = 0
        expected_stats[3][6] = 1

        # Check the equality of the stats
        for i in range(4):
            for j in range(7):
                self.assertEqual(stats.stats[i][j], expected_stats[i][j])

    @number("5.5")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_sorted_stats(self) -> None:
        RandomGen.set_seed(123)
        Constants.NUM_CARDS_AT_INIT = 2
        game: Game = Game()
        game.initialise_game(self.players[0:4])
        _ = game.play_game()
        stats: GameStats = game.game_stats

        # Sort the stats by turns taken in descending order
        stats.sort_stats(StatsColumn.TURNS_TAKEN, ascending=False)

        # Check the stats of all the players
        expected_stats: ArrayR[ArrayR] = ArrayR(8)

        # Add the expected stats

        """
        Name    Games Played    Turns Taken     Cards Played    Cards Drawn     Cards Left      Games Won
        Alice           1               4               2               6               6               0
        Bob             1               4               2               3               3               0
        Charlie         1               5               4               3               1               0
        David           1               3               3               1               0               1
        """

        # Add the stats for Charlie
        expected_stats[0] = ArrayR(7)
        expected_stats[0][0] = "Charlie"
        expected_stats[0][1] = 1
        expected_stats[0][2] = 5
        expected_stats[0][3] = 4
        expected_stats[0][4] = 3
        expected_stats[0][5] = 1
        expected_stats[0][6] = 0

        # Add the stats for Alice
        expected_stats[1] = ArrayR(7)
        expected_stats[1][0] = "Alice"
        expected_stats[1][1] = 1
        expected_stats[1][2] = 4
        expected_stats[1][3] = 2
        expected_stats[1][4] = 6
        expected_stats[1][5] = 6
        expected_stats[1][6] = 0

        # Add the stats for Bob
        expected_stats[2] = ArrayR(7)
        expected_stats[2][0] = "Bob"
        expected_stats[2][1] = 1
        expected_stats[2][2] = 4
        expected_stats[2][3] = 2
        expected_stats[2][4] = 3
        expected_stats[2][5] = 3
        expected_stats[2][6] = 0

        # Add the stats for David
        expected_stats[3] = ArrayR(7)
        expected_stats[3][0] = "David"
        expected_stats[3][1] = 1
        expected_stats[3][2] = 3
        expected_stats[3][3] = 3
        expected_stats[3][4] = 1
        expected_stats[3][5] = 0
        expected_stats[3][6] = 1

        # Check the equality of the stats
        for i in range(4):
            for j in range(7):
                self.assertEqual(stats.stats[i][j], expected_stats[i][j])
