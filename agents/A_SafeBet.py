"""
Implement a safe agent.

It is solely focused on not making mistakes.
It evaluates its own dices, and bets the maximum that it is certain to be on the table (with its own dices). 
Otherwise, it calls bluff, because it cannot be certain that its bet will be correct.
"""

from agents.A_abstractagent import Agent
from typing import List, Union

class SafeBetAgent(Agent):

    def __init__(self):
        pass

    def make_decision(self, own_dices: List[int], total_dices: int,  current_bet: int, first_bet: bool) -> Union[str,int]: 
        bet_quantity = current_bet[0]
        bet_value = current_bet[1]

        dice_value_counts = [0,0,0,0,0,0]
        for dice_value in own_dices:
            dice_value_counts[dice_value-1] += 1

        if dice_value_counts[bet_value-1] > bet_quantity:
            # increment the quantity
            # we have more dices of the betting value on hand than the current bet, so we maximize the increment and return.
            return [dice_value_counts[bet_value-1], bet_value]
        else:
            # see of we have some higher value
            for val_step in range(bet_value, 5):
                if dice_value_counts[val_step] > 0:
                    # we return the amount we have of those.
                    return [dice_value_counts[val_step], val_step]
            
            # no increment possible in quantity or value, so we call bluff
            return self._call_bluff()

    def _place_bet(self, current_bet: List[int], first_bet: bool):
        
        pass

    def _call_bluff(self) -> str:
        return "bluff"