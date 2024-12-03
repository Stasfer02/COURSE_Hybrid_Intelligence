"""
main running file
"""

from gamemanager import PerudoGameManager
from agents.A_abstractagent import Agent
from agents.A_random import RandomAgent
from agents.A_SafeBet import SafeBetAgent
from agents.A_Probabilistic import ProbabilisticAgent


def main() -> None:

    # specify the amount of players
    num_players = 3
    players = (RandomAgent(),ProbabilisticAgent(),SafeBetAgent())

    # create the game manager
    gameManager = PerudoGameManager(num_players)

    active_game = True
    count = 0
    while active_game == True and count < 100:
        if count > 10:
            exit
        # While there is more than 1 active player, roll the dices for a round of Perudo!
        print("\n","-"* 100,"NEW ROUND, ROLLING THE DICES", "-"*100)
        gameManager.roll_all_dices()

        bluff_called = False
        first_bet = True
        while bluff_called == False:
            # now we enter a series of betting/bluffing
            active_players, all_dices, current_bet, player_to_move = gameManager.get_game_state()
            print("BETTING ROUND: players: ",active_players, "current bet: ", current_bet, "player to move: ", player_to_move, " all dices: ", all_dices)

            # get the player decision
            player_dices = all_dices[player_to_move]
            total_dices_cnt = sum(len(dices) for dices in all_dices.values())
            decision = players[player_to_move].make_decision(player_dices, total_dices_cnt, current_bet, first_bet)
            first_bet = False # only place a first_bet once

            if decision == "bluff":
                # bluff called! We can exit the series now.
                bluff_called = True
                # let's evaluate the bluff.
                gameManager.bluff_called()
            else:
                # A bet is placed, we continue with the series.
                gameManager.bet_placed(decision)
                count += 1
        
        # A game has been played after someone has called bluff.
        # We have taken the dices and potentially eliminated a player, so evaluate the amount of players to determine whether or not to continue.
        active_players, x, y, z = gameManager.get_game_state()
        if len(active_players) <= 1:
            active_game = False
            winning_player = active_players[0]
    
    # game is done! print the winner.
    print("-"* 200,"\n","-"* 200)
    print("End of the game! The winning player: ", winning_player, "\n")

if __name__ == "__main__":
    main()
    pass