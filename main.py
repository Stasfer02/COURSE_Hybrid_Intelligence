"""
main running file
"""

from gamemanager import PerudoGameManager
from agents.A_abstractagent import Agent
from agents.A_random import RandomAgent
from agents.A_SafeBet import SafeBetAgent
from agents.A_Probabilistic import ProbabilisticAgent

from typing import List
import matplotlib.pyplot as plt
import logging
import os

def play_game(gameManager: PerudoGameManager, num_players: int, players: List[Agent]) -> int:
    """
    playing a single game, returns the winner of that game (player index).
    """
    active_game = True
    count = 0
    while active_game == True and count < 100:
        if count > 10:
            exit
        # While there is more than 1 active player, roll the dices for a round of Perudo!
        logging.debug(f"\n {'-'* 100} NEW ROUND, ROLLING THE DICES{'-'*100}")
        gameManager.roll_all_dices()

        bluff_called = False
        first_bet = True
        while bluff_called == False:
            # now we enter a series of betting/bluffing
            active_players, all_dices, current_bet, player_to_move = gameManager.get_game_state()
            logging.debug(f"BETTING ROUND: players: {active_players} current bet: {current_bet} player to move: {player_to_move} all dices: {all_dices}")

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

    return winning_player

def main() -> None:
    """
    Play a certain amount of games, and store the result as a plot in the data folder.
    """
    logging.basicConfig(
    level=logging.INFO,  # Set the minimum level to DEBUG
    format='%(message)s'
    )

    # specify the amount of players
    num_players = 3
    players = [ProbabilisticAgent(),ProbabilisticAgent(),ProbabilisticAgent()]

    # create the game manager
    gameManager = PerudoGameManager(num_players)

    games = 1000
    player_wins = [0] * num_players
    for _ in range(games):

        gameManager = PerudoGameManager(num_players)

        winning_player = play_game(gameManager, num_players, players)
        # game is done! print the winner.
        logging.info(f"{'-' * 200}")
        logging.debug(f"{'-'* 200}")
        logging.info(f"End of the game! The winning player: {winning_player} \n")

        player_wins[winning_player] += 1
    
    logging.info("End of all games.")
    
    # names for plotting
    names = []
    for i in range(len(players)):
        name = players[i].name + " " + str(i)
        names.append(name)

    # file storage
    curr_folder = os.path.dirname(__file__)
    plot_path = os.path.join(curr_folder, "data/PPP.png")
    print(plot_path)

    # plotting!
    plt.figure()
    plt.bar(names,player_wins,  color=['green', 'green', 'green'])
    plt.savefig(plot_path)
    plt.close()

if __name__ == "__main__":
    main()
    pass