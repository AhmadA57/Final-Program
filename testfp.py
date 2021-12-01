import pygame
import random

    
def main():
    #----------------------Set up the game------------#  

    pygame.init()    
    screenY = 1040
    screenX = 1040     
    
    clock = pygame.time.Clock()
    frameRate = 60             
    frameCount = 0              
    
    mainSurface = pygame.display.set_mode((screenX, screenY))
    
    spriteSheet = pygame.image.load("Fireknight.png")
    spriteSheet = pygame.transform.scale2x(spriteSheet)
    FireKnightSheet = pygame.image.load("Fireknight.png")
    
        
    FireknightX = 0
    FireknightY = 0
    FireknightPos = [FireknightX, FireknightY]
    
    #These are needed for the image animation
    FireKnightrect = [1,66,228,45]  #Old Values
    FireKnightrect = [2,132,456,90]  #New values are doubled since I doubled the scale
    FireKnightPatchNumber = 0         #Start at the initial patch
    FireKnightPatches =  8         #Only use 4 patches
    FireKNightFrameCount = 0          #Start at intial frame
    FireKnightFrameRate = 8;         #How often to re-draw the PinkMan
    FireKnightDirection = 'Right'     #Control which direction PinkMan is facing
    FireKnightSpeed = 5
    
   
    
    PinkManMove = False            #Control whether the PinkMan can move
    
    while True:
        
        #----------------------Check all the events to see if anything is happening------------#  

        button = pygame.event.poll()    # Look for any event
        if button.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif button.type == pygame.KEYDOWN:
            PinkManMove = True
            if button.key == pygame.K_d:
                PinkManDirection = 'Right'
            elif button.key == pygame.K_a:
                PinkManDirection = 'Left'
            elif button.key == pygame.K_w:
                PinkManDirection = 'Up'
            elif button.key == pygame.K_s:
                PinkManDirection = 'Down'
        elif button.type == pygame.KEYUP:
            PinkManMove = False

    
    
    

    pygame.quit()     # Once we leave the loop, close the window.

main()