"""
Implement a probabilty-calculating agent. 

It calculates the possibility of a bet being correct (incorporating it's own dices) and then decides accordingly.
"""

from agents.A_abstractagent import Agent
from typing import List, Union
from math import comb

class ProbabilisticAgent(Agent):
    """
    class for a probabilistic agent. basically, it does the following:
    
    We calculate a few different probabilities:
    1. The probability of the current bet being false (call bluff)
    2. the probability of a new bet by incrementing quantity being correct
    3. the probability of a new bet by incrementing value being correct

    We then choose the most likely option. 
    """
    def __init__(self):
        
        pass

    def make_decision(self, own_dices: List[int], total_dices: int, current_bet: int, first_bet: bool) -> Union[str,int]: 
        
        # we calculate the probability of the bet being correct, so subtract that from 1 to find the probability of it being false
        p_current_bet_false= 1 - self._p_bet(own_dices, total_dices, current_bet)

        # incrementing value (keep quantity)
        incr_value_bet = [current_bet[0], current_bet[1]+1]
        p_incr_value_bet = self._p_bet(own_dices, total_dices, incr_value_bet)

        # increment quantity
        # TODO for all values!
        p_quantities = []
        for val in range(1,7):
            incr_quantity_bet = [current_bet[0]+1, val]

            p_incr_quantity_bet = self._p_bet(own_dices, total_dices, incr_quantity_bet)
            p_quantities.append(p_incr_quantity_bet)

        p_quantity_best = max(p_quantities)

        # decide on return
        if p_current_bet_false >= p_incr_value_bet and p_current_bet_false >= p_quantity_best:
            print("FROM PROB-AGENT: BLUFF CHOSEN")
            return self._call_bluff()
        elif p_incr_value_bet > p_quantity_best:
            print("FROM PROB-AGENT: INCR-VALUE CHOSEN")
            return incr_value_bet
        else:
            print("FROM PROB-AGENT: INCR QUANTITY CHOSEN FOR QUANTITY: ", p_quantities.index(p_quantity_best)+1)
            return [current_bet[0]+1, p_quantities.index(p_quantity_best)+1]

    def _p_bet(self, own_dices: List[int], total_dices: int, bet: int):
        """
        We calculate the probabilty of some bet being correct using a binomial distribution. 
        """
        
        bet_quantity = bet[0]
        bet_value = bet[1]
        if bet_value > 6:
            # we cannot increment value
            return 0

        # count values on own dices
        dice_value_counts = [0,0,0,0,0,0]
        for dice_value in own_dices:
            dice_value_counts[dice_value-1] += 1

        # subtract our own dices from the quantity (as we are certain they are in the set)
        rest_quantity = bet_quantity - dice_value_counts[bet_value-1]
        rest_dices = total_dices - len(own_dices)
        if rest_quantity <= 0:
            # the wanted amount is already in our own collection of dices, so return 1
            return 1

        p_dice = 1/6        # probability for each value on a dice
        p_bet_true = 0     # probability of bet being correct

        # now we calculate the probabilties of the dices landing on the target value. 
        # Note that we do not need exactly the target value, but AT LEAST the target value
        for i in range(rest_quantity, rest_dices+1):
            p_bet_true += comb(rest_dices, i) * (p_dice ** i) * ((1 - p_dice) ** (rest_dices - i))
        
        return p_bet_true



    def _call_bluff(self) -> str:
        return "bluff"