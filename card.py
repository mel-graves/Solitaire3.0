import arcade

from constants import *


class Card(arcade.Sprite):

    def __init__(self, suit, value, scale=1):
        # Attributes for suit and value
        self.suit = suit
        self.value = value

        # Image to use for the sprite when face up from arcade resources
        self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"
        self.is_face_up = False
        super().__init__(FACE_DOWN_IMAGE, scale, hit_box_algorithm="None")

    def face_down(self):
        # Turn card face down
        self.texture = arcade.load_texture(FACE_DOWN_IMAGE)
        self.is_face_up = False

    def face_up(self):
        # Turn card face up
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True

    @property
    def is_face_down(self):
        # Check if card is face down
        return not self.is_face_up
