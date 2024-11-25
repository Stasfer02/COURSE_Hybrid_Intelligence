"""
main running file
"""

from gamemanager import PerudoGameManager
from agents.A_abstractagent import Agent
from agents.A_random import RandomAgent


def main() -> None:

    # specify the amount of players
    num_players = 3
    players = (RandomAgent,RandomAgent,RandomAgent)

    # create the game manager
    gameManager = PerudoGameManager(num_players)

    #while len(gameManager.get_game_state[0]) > 1:
    test = True
    while test == True:
        # While there is more than 1 active player:
        gameManager.roll_all_dices()                    # roll the dices

        bluffed = False
        while bluffed == False:
            # now we enter a game of betting/bluffing
            active_players, all_dices, current_bet, player_to_move = gameManager.get_game_state()

            print("ROUND: ")
            player_dices = all_dices[player_to_move]
            decision = players[player_to_move].make_decision(player_dices,current_bet)
            
            if decision == "bluff":
                # bluff called! let's evaluate.
                gameManager.bluff_called(player_to_move, current_bet)
                bluffed = True
            else:
                gameManager.bet_placed(player_to_move, decision)
        
        # a game has been played, dices are taken. Continue if there is still more than 1 player.
        test = False
    
    # game is done! print the winner.


        
    

if __name__ == "__main__":
    main()
    pass