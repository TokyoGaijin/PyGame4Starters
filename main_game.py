"""
This is a general template for game creation using PyGame.
It attempts to organize the coding experience into an easy-to-use template,
formulated to appear like XNA Game Studio / Mono Game for C#.

To use this, place your logic in the fields when and where prompted.

This involves the Screen class.
This template automates some of the screen management.
For a slightly more challenging game logic where the screen is not handled within an object,
please load maingame.py.

"""

## Mandatory includes
import pygame
import screen

## TODO: Import your necessary and custom libraries\modules here

## Initialize PyGame
pygame.init()

## Declare your global variables here.
SCREEN = None


## The game logic
def main_game():
    
    def initializer():
        global SCREEN

        ## screen.Screen takes multiple arguments.
        ## Here, these are the basic args: (width, height, FramesPerSecond)
        SCREEN = screen.Screen(640, 480, 60)
        ## Additional, option args include: (..., color=(R,G,B), caption="My Game")
        ## RGB: This value is a 3-element tuple and is defaulted at (0,0,0) - the RGB color code for black
        ## No caption is set, by default. See screen.py for more information.
        
        ## TODO: Initialize your game objeccts here.



    def draw():
        ## TODO* Run your objects draw functions here
        pass




    def update():
        ## TODO: Run your objects draw functions here
       

        SCREEN.screen_update()


    ## Initialize the class objects
    initializer()


    while SCREEN.inPlay:
        ## TODO: Add your controller logic here.
        ## TIP: Your collision logic should go in the main class's 
        ##      update() method to avoid code crowding

        ## WARNING: Do not delete the following lines of code:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SCREEN.inPlay = False


        draw()
        update()



## Auto-start the game
if __name__ == "__main__":
    main_game()
