"""
This is a typical screen class.
You may use this class instead of hard-programming the logic
in your maingame.py script.

Default values are set, so please change them as you like.
"""

import pygame

class Screen(object):
    def __init__(self, width, height, FPS, bg_color = (0, 0, 0), caption = None):
        """
        This takes 3 mandatory and 2 optional variables.
        You MUST declare a width and height.
        You MUST declare the FPS
        The background color is defaulted to 'black'
        There is no game caption set. Declare this when you initialize the game.
        """

        self.WIDTH = width
        self.HEIGHT = height
        self.SCREEN_SIZE = (self.WIDTH, self.HEIGHT)

        self.WINDOW = pygame.display.set_mode(self.SCREEN_SIZE)

        if caption != None:
            self.GAME_NAME = caption
            pygame.display.set_cap(self.GAME_NAME)

        self.BG_COLOR = bg_color
        self.CLOCK = pygame.time.Clock()
        self.FPS = FPS
        self.inPlay = True

        

    def kill_screen(self):
        ### Exits the game loop
        if self.inPlay:
            self.inPlay = False


    def screen_update(self):
        ### The update handler for this screen object
        pygame.display.update()
        self.WINDOW.fill(self.BG_COLOR)
