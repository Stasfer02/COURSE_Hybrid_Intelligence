"""
Abstract base class for agents
"""
from abc import ABC, abstractmethod

class Agent(ABC):
    """
    Abstract base class for agents.
    """
    @abstractmethod
    def __init__(self):

        pass
    
    @abstractmethod
    def make_decision(self, own_dices, current_bet):

        pass

    @abstractmethod
    def place_bet(self):

        pass

    @abstractmethod
    def call_bluff(self):
        
        pass