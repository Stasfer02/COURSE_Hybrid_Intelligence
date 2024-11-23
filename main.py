"""
main running file
"""

from gamemanager import PerudoGameManager



def main() -> None:

    # specify the amount of players
    num_players = 5

    # create the game manager
    gameManager = PerudoGameManager(num_players)

    gameManager.roll_all_dices()

    values_dices = gameManager.get_game_state()[1]

if __name__ == "__main__":
    main()
    pass