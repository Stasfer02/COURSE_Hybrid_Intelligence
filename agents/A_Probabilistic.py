"""
Implement a probabilty-calculating agent. 

It calculates the possibility of a bet being correct (incorporating it's own dices) and then decides accordingly.
"""

from agents.A_abstractagent import Agent
from typing import List, Union

class ProbabilisticAgent(Agent):

    def __init__(self):
        
        pass

    def make_decision(self, own_dices: List[int], total_dices: int, current_bet: int, first_bet: bool) -> Union[str,int]: 

        pass

    def _place_bet(self, current_bet: List[int], first_bet: bool) -> List[int]:
        bet = [0,0]
        return bet

    def _call_bluff(self) -> str:
        return "bluff"