"""
Random agent. Chooses to raise the bet 80% of the time and otherwise calls bluff.
"""

from agents.A_abstractagent import Agent
import numpy as np
from typing import List,Union

class RandomAgent(Agent):
    def __init__(self):
        self.name = "Random Agent"
    
    def make_decision(self, own_dices: List[int], total_dices: int, current_bet: List[int], first_bet: bool) -> Union[str,List[int]]:
        """
        Our random agents decides what to do randomly. 
        Currently, it bluffs 20% of the time.

        If it's the first bet, always place a (random) bet
        """
        if first_bet == True: 
            # it is the first bet, so we cannot call bluff
            decision = self._place_bet(own_dices, current_bet, first_bet)

        elif current_bet[0] > total_dices:
            # if the bet quantity is more than the amount of dices, always call bluff
            decision = self._call_bluff()

        else:
            x = np.random.rand()

            if x < 0.8:
                decision = self._place_bet(own_dices, current_bet, first_bet)
            else:
                decision = self._call_bluff()
        return decision

    def _place_bet(self, own_dices: List[int], current_bet, first_bet: bool) -> List[int]:
        """
        Placing the bet. The random agents decides at random (50/50) whether to increase value or quantity.

        If it's the first bet, choose quantity and value at (semi-) random
        """
        bet = current_bet
        if first_bet == True:
            # we are at the first bet. choose some random quantity within our own quantity of dices + 1 (there is always at least one other dice in the game), and some random value
            bet[0] = np.random.randint(1,len(own_dices)+1)
            bet[1] = np.random.randint(1,7)
        else: 
            # randomly decide whether to raise value or quantity
            x = np.random.rand()

            if x > 0.5 and bet[1] < 6:
                # increase value
                bet[1] = bet[1] + 1
            else:
                # increase quantity
                bet[0] = bet[0] + 1
                # choose random value for the value (higher than the current one)
                bet[1] = np.random.randint(bet[1],7)
        return bet
    
    def _call_bluff(self) -> str:
        return "bluff"