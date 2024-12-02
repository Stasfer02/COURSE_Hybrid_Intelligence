"""
Abstract base class for agents
"""
from abc import ABC, abstractmethod
from typing import List
class Agent(ABC):
    """
    Abstract base class for agents.
    """
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def make_decision(self, own_dices: List[int], current_bet: List[int], first_bet: bool):
        pass

    @abstractmethod
    def _place_bet(self, current_bet: List[int], first_bet: bool):
        pass

    @abstractmethod
    def _call_bluff(self):
        pass