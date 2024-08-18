from data_structures.referential_array import ArrayR
from player import Player
from constants import Constants
from enum import Enum, auto


class StatsColumn(Enum):
    """
    StatsColumn class to store the columns of the statistics
    """
    PLAYER_NAME = 0
    GAMES_PLAYED = auto()
    TURNS_TAKEN = auto()
    CARDS_PLAYED = auto()
    CARDS_DRAWN = auto()
    CARDS_LEFT = auto()
    WINS = auto()


class GameStats:
    """
    GameStats class to store the statistics
    """
    def __init__(self, players: ArrayR[Player]) -> None:
        """
        Constructor for the GameStats class

        Args:
            players (ArrayR[Player]): The list of players

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def add_player(self, player: Player) -> None:
        """
        Method to add a player to the statistics

        Args:
            player (Player): The player to be added

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def record_game_played(self, player: Player) -> None:
        """
        Method to record a game played by a player

        Args:
            player (Player): The player who played the game

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def record_turn(self, player: Player) -> None:
        """
        Method to record a turn played by a player

        Args:
            player (Player): The player who played the turn

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def record_card_played(self, player: Player) -> None:
        """
        Method to record a card played by a player

        Args:
            player (Player): The player who played the card

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def record_card_drawn(self, player: Player) -> None:
        """
        Method to record a card drawn by a player

        Args:
            player (Player): The player who drew the card

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def record_game_won(self, player: Player) -> None:
        """
        Method to record a game won by a player

        Args:
            player (Player): The player who won the game

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def record_card_left(self, player: Player) -> None:
        """
        Method to record a card left by a player

        Args:
            player (Player): The player who left the card

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def sort_stats(self, stat: StatsColumn, ascending: bool = True) -> None:
        """
        Method to sort the statistics

        Args:
            stat (str): The statistic to sort by
            ascending (bool): The order to sort in

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """
        Method to return the length of the GameStats object

        Returns:
            int: The length of the GameStats object

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Method to return the string representation of the GameStats object

        Returns:
            str: The string representation of the GameStats object

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        raise NotImplementedError
