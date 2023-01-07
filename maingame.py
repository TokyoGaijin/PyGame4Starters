"""
This is a general template for game creation using PyGame.
It attempts to organize the coding experience into an easy-to-use template,
formulated to appear like XNA Game Studio / Mono Game for C#.

To use this, place your logic in the fields when and where prompted.

This does not contain code that involves the Screen class.
This template gives you control so that you can see how the screen is initialized.
For a simpler game logic where the screen is handled within an object,
please load main_game.py.

"""

## Mandatory Includes
import pygame

## TODO: Import your necessary and custom libraries/modules here

## Initialize Pygame
pygame.init()

## Pre-determined global variables
WINDOW = None
FPS = 0
CLOCK = None
BG_COLOR = (0, 0, 0)
inPlay = None

# Set up your screen dimensions here
def initialize_screen():
    global WINDOW, FPS, CLOCK, inPlay
    SIZE_W = 0 ## EDIT THIS
    SIZE_H = 0 ## EDIT THIS
    SCREEN_SIZE = (SIZE_W, SIZE_H)

    GAME_NAME = "" ## EDIT THIS
    FPS = 0 ## EDIT THIS
    inPlay = True ## YOUR GAME LOOP REFERENCER

    WINDOW = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(GAME_NAME)
    CLOCK = pygame.time.Clock()


## TODO: Declare your variables here
## TODO: Create your custom functions here



def main_game():
    ## This global reference is necessary. Do not erase.
    global inPlay
    
    def initializer():
        initialize_screen()

        ## TODO: Initialize your game objects here.
        


    def update():
        ## Leave this line of code to manage your update flops
        CLOCK.tick(FPS)

        ## TODO: Run your objects' update logics here
        
        
        
        ## Leave the last 2 lines of code for update logic
        pygame.display.update()
        WINDOW.fill(BG_COLOR)
        


    def draw():
        ## TODO: Run your objects draw functions here
        pass
    
    

    ## This is your GameLoop logic
    while inPlay:
        ## TODO: Add your controller logic here
        ## TIP: Your collision logic should go in this main class's 
        ##      update() method to avoid code crowding


        ## WARNING: Do not delete the following lines of code:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False

        draw()
        update()




if __name__=="__main__":
    main_game()
