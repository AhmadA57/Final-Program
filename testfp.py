#TODO: Update this example showing how to use a temporary surface and pygame.transform.flip(tempSurface,True,False)
import pygame
import random

    
def main():
    """ Set up the game and run the main game loop """
    #----------------------Set up the game------------#  

    pygame.init()      # Prepare the pygame module for use
    WindowX = 1000
    WindowY = 1000
    Window = (WindowX*WindowY)   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    frameRate = 60               #Slowing down the program
    frameCount = 0               #Count the number of frames that have occurred
    
    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((WindowX, WindowY))
    pygame.display.set_caption("Fire Knight")
    
    spriteSheet = pygame.image.load("Images\Fireknight.png")
    spriteSheet = pygame.transform.scale2x(spriteSheet)
    
    
    FireKnightPos = [-30,50]
    rectColor = (0, 200, 255)
    
    #These are needed for the image animation
    FireKnightRect = [1,60,224,53]  #Old Values
    FireKnightRect = [2,120,448,106]  #New values are doubled since I doubled the scale
    FireKnightPatchNumber = 0         #Start at the initial patch
    FireKnightNumPatches = 8          #Only use 4 patches
    FireKnightFrameCount = 0          #Start at intial frame
    FireKnightFrameRate = 6;         #How often to re-draw the FireKnight
    FireKnightDirection = 'Right'     #Control which direction FireKnight is facing
    FireKnightSpeed = 6
    
    FireKnightMove = False            #Control whether the FireKnight can move
    wallInTheWayRight = False
    wallInTheWayLeft = False
    wallInTheWayUp = False
    wallInTheWayDown = False
    wallCollide = False
    
    wall1 = pygame.Rect(0,0, 10, 1000)  #x y width hight
    wall2 = pygame.Rect(0,0, 1000, 10)
    wall3 = pygame.Rect(0,980, 1000, 10)
    wall4 = pygame.Rect(990, 0, 10, 1000)

    
    while True:
        
        #----------------------Check all the events to see if anything is happening------------#  

        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.KEYDOWN:
            FireKnightMove = True
            if ev.key == pygame.K_d:
                FireKnightDirection = 'Right'
            elif ev.key == pygame.K_a:
                FireKnightDirection = 'Left'
            elif ev.key == pygame.K_w:
                FireKnightDirection = 'Up'
            elif ev.key == pygame.K_s:
                FireKnightDirection = 'Down'
        elif ev.type == pygame.KEYUP:
            FireKnightMove = False

 

        #----------------------Game Logic Goes After Here----------------------------#  
        # Update your game objects and data structures here...

        #Game logic for the FireKnight
        
        FireKnightHitbox = pygame.Rect(FireKnightPos[0]+195, FireKnightPos[1]+10, 60, 90)
        
        if (pygame.Rect.colliderect(FireKnightHitbox, wall1)):
            wallCollide = True
        elif (pygame.Rect.colliderect(FireKnightHitbox, wall2)):
            wallCollide = True
        elif (pygame.Rect.colliderect(FireKnightHitbox, wall3)):
            wallCollide = True
        elif (pygame.Rect.colliderect(FireKnightHitbox, wall4)):
            wallCollide = True

        #check for a collision between FireKnight's hitbox and the walls
        if wallCollide and FireKnightDirection =='Right':
            print("collision onthe right!!!")
            wallInTheWayRight = True
            FireKnightPos[0] -= (2*FireKnightSpeed)
        elif wallCollide and FireKnightDirection =='Left':
            print("collision on the left!!!")
            wallInTheWayLeft = True
            FireKnightPos[0] -= (2*FireKnightSpeed)
        elif wallCollide and FireKnightDirection =='Up':
            print("collision up!!!")
            wallInTheWayUp = True
            FireKnightPos[1] -= (4*FireKnightSpeed)     #update the y for the FireKnight
        elif wallCollide and FireKnightDirection =='Down':
            print("collision down!!!")
            wallInTheWayDown = True
            FireKnightPos[1] -= (2*FireKnightSpeed)     #update the y for the FireKnight
        else:
            print("NO collision!!!")
            wallInTheWayLeft = False
            wallInTheWayRight = False
            wallInTheWayDown = False
            wallInTheWayUp = False
        
        
        if (FireKnightMove):  #Check if the FireKnight should move
            #Move the FireKnight
            if FireKnightDirection =='Right' and wallInTheWayRight == False: #FireKnight goes right
                FireKnightPos[0] += FireKnightSpeed     #update the x for the FireKnight
                wallInTheWayLeft = False
            elif FireKnightDirection =='Left' and wallInTheWayLeft == False:                               #FireKnight goes left
                FireKnightPos[0] -= FireKnightSpeed     #update the x for the FireKnight
                wallInTheWayRight = False
            elif FireKnightDirection =='Up' and wallInTheWayUp == False:                               #FireKnight goes left
                FireKnightPos[1] -= FireKnightSpeed     #update the y for the FireKnight
                wallInTheWayDown = False
            elif FireKnightDirection =='Down' and wallInTheWayDown == False:                               #FireKnight goes left
                FireKnightPos[1] += FireKnightSpeed     #update the y for the FireKnight
                wallInTheWayUp = False
        
        if FireKnightMove == False:
        
            if (frameCount % FireKnightFrameRate == 0):    #Only change the animation frame once every {FireKnightFrameRate} frames
                if (FireKnightPatchNumber < FireKnightNumPatches-1) :
                    FireKnightPatchNumber += 1
                    FireKnightRect[0] += FireKnightRect[2]  #Shift the "display window" to the right along the sprite sheet by the width of the image
                else:
                    FireKnightPatchNumber = 0           #Reset back to first patch
                    FireKnightRect[0] -= FireKnightRect[2]*(FireKnightNumPatches-1)  #Reset the rect position of the rect back too
                    #self.imageRect = copy.copy(self.origImageRect)
                    #print(f"Patch Number: {FireKnightPatchNumber}   Image Rect: {FireKnightRect}  ")
                    
        elif FireKnightMove == True:
             FireKnightRect = [1,177,224,53]  #Old Values
             FireKnightRect = [2,354,448,106]  #Old Values
        
           
        #else:
            #oof code
        
        wallCollide = False
        
        #----------------------Draw all the images----------------------------#  
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0,0,0))
        
        
        #draw the wall
        wall1 = pygame.draw.rect(mainSurface, rectColor, (wall1))
        wall2 = pygame.draw.rect(mainSurface, rectColor, (wall2))
        wall3 = pygame.draw.rect(mainSurface, rectColor, (wall3))
        wall4 = pygame.draw.rect(mainSurface, rectColor, (wall4))
        #wall5 = pygame.draw.rect(mainSurface, rectColor, (wall5))
        #wall6 = pygame.draw.rect(mainSurface, rectColor, (wall6))
        #wall7 = pygame.draw.rect(mainSurface, rectColor, (wall7))
        #wall8 = pygame.draw.rect(mainSurface, rectColor, (wall8))
        #wall9 = pygame.draw.rect(mainSurface, rectColor, (wall9))
        #wall10 = pygame.draw.rect(mainSurface, rectColor, (wall10))
        #wall11 = pygame.draw.rect(mainSurface, rectColor, (wall11))
        #wall12 = pygame.draw.rect(mainSurface, rectColor, (wall12))
        #wall13 = pygame.draw.rect(mainSurface, rectColor, (wall13))
        #wall14 = pygame.draw.rect(mainSurface, rectColor, (wall14))
        #wall15 = pygame.draw.rect(mainSurface, rectColor, (wall15))
        #wall16 = pygame.draw.rect(mainSurface, rectColor, (wall16))
        #wall17 = pygame.draw.rect(mainSurface, rectColor, (wall17))
        #wall18 = pygame.draw.rect(mainSurface, rectColor, (wall18))
       # wall19 = pygame.draw.rect(mainSurface, rectColor, (wall19))
       # wall20 = pygame.draw.rect(mainSurface, rectColor, (wall20))
      #  wall21 = pygame.draw.rect(mainSurface, rectColor, (wall21))
                 
        
        
        
        
        
        #you can comment the line of code below to see the hitbox
#         pygame.draw.rect(mainSurface, (255,0,0), FireKnightHitbox, 2)
        #the print below is for troubleshooting, it shows FireKnight's location and hitbox
#         print(f"FireKnight position = {FireKnightPos} , {FireKnightHitbox}")
                
        
        
        #Draw the image of the FireKnight sprite using the rect
        #mainSurface.blit(spriteSheet, FireKnightPos, FireKnightRect)  #Positions found using msPaint
        tempSurface = pygame.Surface( (FireKnightRect[2], FireKnightRect[3]) ) #Make a temp Surface using the width and height of the rect
        tempSurface.fill((1,1,1))
        tempSurface.set_colorkey((1,1,1))                                      #Set the color black to be transparent
        tempSurface.blit(spriteSheet, (0,0),  FireKnightRect)                      #Copy the FireKnight image to the temp surface
        
        if FireKnightDirection == 'Left':
            tempSurface = pygame.transform.flip(tempSurface,True,False)
        
        mainSurface.blit(tempSurface, FireKnightPos)  #Positions found using msPaint
        
        
        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        
        #----------------------Set your frame rate----------------------------#  

        frameCount += 1;
        clock.tick(frameRate) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()


