# 1. Include py-game (we needed pip to get this for us because python doesn't ship with it.)
import pygame

# 2. initalzie pygame; why? because we have too
pygame.init()

# 3. Make a sceeen with a size. The size MUST be a tuple
screen_size = (512, 480)
pygame_screen = pygame.display.set_mode(screen_size) #we have to assign our screen to the foundation.
# set the title of the window screen that opens
pygame.display.set_caption('FRIED') #tell the pygame to display this...

#=============VARIABLES FOR OUR GAME=============
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')
arrow_image = pygame.image.load('arrow.png')
heroLoc = {
    'x': 0,
    'y': 0
}


# ============EVENT CHECKER============
game_on = True # the loop will run as long as game_on is TRUE
while game_on: #in our game loop from here on out.
    # 5. Listen for events and quit if the user clicks the 'x'
    for event in pygame.event.get(): #interacts with what the user is doing
        #THE USER CLICKED THE RED DOT! 
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN: # this will track and tell us which keys the user has pressed.
            print event.key # this is crucial because it will show you the number that is equivalent to the key you pressed. 
                            # if not, you would not be able to identify what key is equal to what number
            if event.key == 275: #the user pressed the right arrow, which is 275. THIS IS ONLY CONTROLLING THE RIGHT ARROW.
                #we need to move our hero now.
                heroLoc['x'] += 5 # this is how far over your hero will move when you press the right arrow.
            elif event.key ==
# ============DRAW STUFF============
    #we use B.L.I.T (blit) to draw on the screen. blit = bock image transfer
    # a. What to draw
    # b. Where to draw it
    # in the docs... SURFACE = our "pygame screen"
    pygame_screen.blit(background_image,[0,0])
    pygame_screen.blit(hero_image,[heroLoc['x'], heroLoc['y']]) # this places the image of our hero on the game; see lines 20 and 21 to reflect this.
    pygame.display.flip() #this should clear the screen when you move the character because it basically refresh sceen.