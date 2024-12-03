"""
Creating a game manager class that determines state of the game and what information is available to what player.

We have chosen the game of Perudo. 

"""
from typing import List
import numpy as np
import logging

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
        # inialize as empty at the start of every round.
        self.dice_values = {}
        
        for player_idx in range(len(self.players)):
            # for each player, roll it's dices
            player_dicethrow = [np.random.randint(1,7) for _ in range(self.dices_pp[player_idx])]
            
            self.dice_values[self.players[player_idx]] = player_dicethrow
        
        # also reset the current bet. 
        # TODO maybe we should incorporate some starting command for the first bet.
        self.current_bet = [0,1]
    
    def bet_placed(self, bet) -> None:
        """
        Player places a bet.
        """
        self.current_bet = bet
        self._next_player()
        logging.debug(f"New bet placed: {bet} \n")

    def bluff_called(self) -> None:
        """
        Player calls a bluff.
        1. Evaluate it's truth.
        2. Determine who wins/loses and withdraw a dice accordingly.
        """
        logging.debug(f"Bluff called by player: {self.players[self.player_to_move_idx]} at player index: {self.player_to_move_idx} \n")
        
        bet = self.current_bet
        quantity = bet[0]
        value = bet[1]
        logging.debug(f"Current bet: There are {quantity} dices with value: {value}")

        true_quantity = self._count_dices(value)
        logging.debug(f"True quantity: {true_quantity}")

        if true_quantity >= quantity:
            # wrong bluff! remove dice 
            self._remove_dice(self.player_to_move_idx)
        else:
            # correct bluff! remove dice from previous player
            prev_player_idx = self._prev_player_idx()
            self._remove_dice(prev_player_idx)
        
        # reset player to move
        # TODO we now always set this to player at index 0, but maybe this should be different? like always the player that just lost a dice or something.
        self.player_to_move_idx = 0

    def _next_player(self) -> None:
        """
        Private method to determine the next player to move. 
        """
        if self.player_to_move_idx == (len(self.players)-1):
            # it is the last player in the list, go back to player at index 0
            self.player_to_move_idx = 0
        else:
            self.player_to_move_idx += 1
    
    def _prev_player_idx(self) -> int:
        """
        Private method to get the previous player. (for taking dices)
        """
        if self.player_to_move_idx == 0:
            # it is the first player, so go to end of the list.
            return (len(self.players) - 1)
        else:
            return (self.player_to_move_idx - 1)


    def _remove_dice(self, player_idx) -> None:
        """
        Private method for removing a dice from a certain player.
        """
        logging.debug(f"Removing dice from player: {self.players[player_idx]} at player index: {player_idx}")

        # subtract a dice 
        self.dices_pp[player_idx] -= 1

        # check if the player has no dices left
        if self.dices_pp[player_idx] == 0:
            # if so, eliminate the player
            self._eliminate_player(player_idx)

    def _eliminate_player(self, player_idx) -> None:
        """
        eliminate a player from the active player list, also remove it's index from the "dices per player" list to ensure these align.
        """
        logging.debug(f"Eliminating player: {self.players[player_idx]} at index: {player_idx}")

        del self.players[player_idx]
        del self.dices_pp[player_idx]

    def _count_dices(self, value) -> int:
        """
        Private method to evaluate the amount of dices of some value in the current round. 
        Used to evaluate the bluff.
        """
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
        4. player to move.
        """
        return self.players, self.dice_values, self.current_bet, self.players[self.player_to_move_idx]
    
    def evaluate_bet(self, previous_bet: List[int], new_bet: List[int]) -> bool:
        """
        evaluate bet to ensure that the agents do not make mistakes.
        """
        if new_bet[0] < previous_bet[0]:
            # we decreased in quantity
            logging.debug(f"BETTING MISTAKE: previous bet: {previous_bet}, next bet: {new_bet}")
            return False
        elif new_bet[0] == previous_bet[0] and new_bet[1] <= previous_bet[1]:
            # quantity stayed the same, but so did the value (or it decreased)
            logging.debug(f"BETTING MISTAKE: previous bet: {previous_bet}, next bet: {new_bet}")
            return False
        else:
            # we either increased quantity or value
            return True