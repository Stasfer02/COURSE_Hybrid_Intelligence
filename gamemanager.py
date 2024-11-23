"""
Creating a game manager class that determines state of the game and what information is available to what player.

We have chosen the game of Perudo. 

"""
from typing import List
import numpy as np

class PerudoGameManager:
    """
    Perudo Game Manager class.
    """
    def __init__(self, num_players) -> None:
        """
        Initialize with the amount of players. 
        
        Set amount of dices per player (starting value = 5)
        initialize dictionary for player dice throws
        """
        self.players: List[int] = list(range(num_players))
        self.dices_pp: List[int] = [5] * num_players

        self.dice_values: dict = {}
        self.current_bet: List[int] = [0,0]
        self.player_to_move = 0
        self.eliminated_players: List[int] = []

    def roll_all_dices(self):
        """
        Roll the dices for all players. 
        """
        for player in self.players:
            if not player in self.eliminated_players:
                # for each player, roll it's dices
                player_dicethrow = [np.random.randint(1,7) for _ in range(self.dices_pp[player])]
            
            self.dice_values[player] = player_dicethrow
    
    def bet_placed(self, player, bet):
        """
        Player places a bet.
        """
        self.current_bet = bet
        pass

    def bluff_called(self, player, quantity):
        """
        Player calls a bluff.
        """
        pass

    def get_game_state(self):
        """
        Provide the current game state, consisting of:
        1. players in the game
        2. dices on the table
        3. current bet
        """
        active_players = []
        for player in self.players:
            if not player in self.eliminated_players:
                active_players.append(player)

        return active_players, self.dice_values, self.current_bet, self.player_to_move