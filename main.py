"""
main running file
"""

from gamemanager import PerudoGameManager
from agents.A_abstractagent import Agent
from agents.A_random import RandomAgent


def main() -> None:

    # specify the amount of players
    num_players = 3
    players = (RandomAgent(),RandomAgent(),RandomAgent())

    # create the game manager
    gameManager = PerudoGameManager(num_players)

    active_game = True
    winning_player = None
    while active_game == True:
        # While there is more than 1 active player
        print("\n","-"* 100,"NEW ROUND, ROLLING THE DICES", "-"*100)
        gameManager.roll_all_dices()                    # roll the dices
        bluff_called = False

        while bluff_called == False:
            # now we enter a game of betting/bluffing
            active_players, all_dices, current_bet, player_to_move = gameManager.get_game_state()
            player_dices = all_dices[player_to_move]
            print("BETTING ROUND: players: ",active_players, "current bet: ", current_bet, "player to move: ", player_to_move, " total dices: ", all_dices)

            decision = players[player_to_move].make_decision(player_dices, current_bet)
            
            if decision == "bluff":
                # bluff called! let's evaluate.
                gameManager.bluff_called()
                bluff_called = True
            else:
                # we place a bet
                gameManager.bet_placed(decision)
                # we continue the game until bluffed
        
        # a game has been played, dices are taken. Continue if there is still more than 1 player.
        active_players, x, y, z = gameManager.get_game_state()
        if len(active_players) <= 1:
            active_game = False
            winning_player = active_players
    
    # game is done! print the winner.
    print("-"* 200,"\n","-"* 200)
    print("End of the game! player(s) left: ", winning_player)
    print("\n")

if __name__ == "__main__":
    main()
    pass