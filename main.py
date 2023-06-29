import arcade
from game import MyGame

"""
Adapted from: https://api.arcade.academy/en/latest/tutorials/card_game/index.html
Original author: Paul Vincent Craven
Modified for our use
"""


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
