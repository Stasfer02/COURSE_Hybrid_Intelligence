"""
Creating a game manager class that determines state of the game and what information is available to what player.

We have chosen the game of Perudo. 

"""
from typing import List, Tuple
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
        self.players: List[int] =  list(range(num_players))
        self.dices_pp: List[int] = [5] * num_players

        self.dice_values: dict = {}
        self.current_bet: List[int] = [1,1] # quantity, value
        self.player_to_move_idx = 0
    
    def roll_all_dices(self):
        """
        Roll the dices for all players. 
        """
        # inialize as empty
        self.dice_values = {}
        
        for player_idx in range(len(self.players)):
            # for each player, roll it's dices
            player_dicethrow = [np.random.randint(1,7) for _ in range(self.dices_pp[player_idx])]
            
            self.dice_values[self.players[player_idx]] = player_dicethrow
        
        # also reset the current bet
        self.current_bet = [1,1]

        pass
    
    def bet_placed(self, bet) -> None:
        """
        Player places a bet.
        """
        self.current_bet = bet
        self._next_player()
        print("New bet placed: ", bet,"\n")
        
        pass


    def bluff_called(self) -> None:
        """
        Player calls a bluff.
        1. Evaluate it's truth.
        2. Determine who wins/loses and withdraw a dice accordingly.
        """
        print("Bluff called by player: ", self.players[self.player_to_move_idx],"at player index:", self.player_to_move_idx, "\n")
        bet = self.current_bet
        quantity = bet[0]
        value = bet[1]
        print("Current bet: There are ", quantity, " dices with value: ", value)
        true_quantity = self._count_dices(value)
        print("True quantity: ", true_quantity)

        if true_quantity >= quantity:
            # wrong bluff! remove dice 
            self._remove_dice(self.player_to_move_idx)
        else:
            # correct bluff! remove dice from previous player
            prev_player_idx = self._prev_player_idx()
            self._remove_dice(prev_player_idx)
        
        # reset player to move
        self.player_to_move_idx = 0
        pass


    def _next_player(self) -> None:
        if self.player_to_move_idx == (len(self.players)-1):
            self.player_to_move_idx = 0
        else:
            self.player_to_move_idx += 1

        pass
    
    def _prev_player_idx(self) -> int:
        if self.player_to_move_idx == 0:
            return (len(self.players) - 1)
        else:
            return (self.player_to_move_idx - 1)


    def _remove_dice(self, player_idx) -> None:
        print("Removing dice from player: ", self.players[player_idx], "at player index: ", player_idx)
        print("Dices_pp: ",self.dices_pp)
        self.dices_pp[player_idx] -= 1
        print("Dices)pp: ",self.dices_pp)
        # check if the player has no dices left
        if self.dices_pp[player_idx] == 0:
            self._eliminate_player(player_idx)

        else:
            # not eliminated, so start the next round
            self.player_to_move_idx = player_idx
        
        pass

    def _eliminate_player(self, player_idx) -> None:
        """
        eliminate a player from the active player list
        """
        print("Eliminating player: ", self.players[player_idx], "at index: ", player_idx)
        del self.players[player_idx]
        del self.dices_pp[player_idx]

        pass

    def _count_dices(self, value) -> int:
        count = 0

        for key, valuelist in self.dice_values.items():
            for item in valuelist:
                if item == value:
                    count += 1

        return count
    def get_game_state(self):
        """
        Provide the current game state, consisting of:
        1. players in the game
        2. dices on the table
        3. current bet
        4. player to move
        """

        return self.players, self.dice_values, self.current_bet, self.players[self.player_to_move_idx]