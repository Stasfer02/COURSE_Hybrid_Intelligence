"""
Random agent. Chooses to raise the bet 80% of the time and otherwise calls bluff.
"""

from agents.A_abstractagent import Agent
import numpy as np
from typing import List

class RandomAgent(Agent):
    def __init__(self):
        pass
    
    def make_decision(self, own_dices, current_bet) -> None:
        """
        Our random agents decides what to do randomly. 
        Currently, it bluffs 20% of the time.
        """
        x = np.random.rand()

        if x < 0.8:
            self._place_bet(current_bet)
        else:
            self._call_bluff()
        pass

    def _place_bet(self, current_bet) -> List[int]:
        """
        Placing the bet. The random agents decides at random (50/50) whether to increase value or quantity.
        """
        bet = current_bet

        # randomly decide whether to raise value or quantity
        x = np.random.rand()

        if x > 0.5 and bet[1] < 6:
            # increase value
            bet[1] = bet[1] + 1
        else:
            # increase quantity
            bet[0] = bet[0] + 1
            # choose random value for the value
            bet[1] = np.random.randint(1,7)

        return bet
    
    def _call_bluff(self) -> str:
        return "bluff"