import pygame
import time
import random

pygame.init()

pygame.mixer.music.load("../Sounds/music/St_Francis.wav")
crash_sound = pygame.mixer.Sound("../Sounds/effects/Crash.wav")


display_width = 800
display_height = 600

white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)

car_width = 294

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('images/car.png')
gameIcon = carImg

pygame.display.set_icon(gameIcon)

pause = False

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay,color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()

##def message_display(text):
##    largeText = pygame.font.Font('../Fonts/freesansbold.ttf',115)
##    TextSurf, TextRect = text_objects(text, largeText)
##    TextRect.center = ((display_width/2),(display_height/2))
##    gameDisplay.blit(TextSurf, TextRect)
##
##    pygame.display.update()
##
##    time.sleep(2)
##
##    game_loop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf,TextRect = text_objects("You Crashed", largeText)
    TextRect.center = (display_width/2,display_height/2)
    gameDisplay.blit(TextSurf,TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play Again", 150,450,100,50,green,bright_green,game_loop)
        button("Quit", 550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def unpaused():
    global pause
    pause = False
    pygame.mixer.music.unpause()

def paused():
    pygame.mixer.music.pause()

    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf,TextRect = text_objects("Paused", largeText)
    TextRect.center = (display_width/2, display_height/2)
    gameDisplay.blit(TextSurf,TextRect)

    while pause:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150,450,100,50,green,bright_green,unpaused)
        button("Quit",550,450,100,50,red,bright_red,quitgame)


        pygame.display.update()
        clock.tick(15)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.Font("../Fonts/freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( x+(w/2), y+(h/2) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('../Fonts/freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Pongatron", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Solo", 150,450,100,50,green,bright_green,game_loop)
        button("Multiplayer", 300,450,200,50,green,bright_green,multi_menu)
        button("QUIT!",550,450,100,50,red,bright_red,quitgame)

        #pygame.draw.rect(gameDisplay, red,(550,450,100,50))

        pygame.display.update()
        clock.tick(15)

def multi_menu():
    multi = True

    while multi:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('../Fonts/freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Pongatron", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Create a game",150,450,200,50,green,bright_green,multi_gamecreate)
        button("Join a game", 550,450,200,50, green,bright_green,multi_gamesearch)
        button("Back", 0,50,200,50,red,bright_red,game_intro)
        pygame.display.update()
        clock.tick(15)

def multi_gamesearch():
    gamesearch = True

    while gamesearch:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('../Fonts/freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Pongatron", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("Create a game",150,450,200,50,green,bright_green,multi_gamecreate)
        button("Join a game", 550,450,200,50, green,bright_green,multi_gamesearch)
        button("Back", 0,50,200,50,red,bright_red,game_intro)
        pygame.display.update()
        clock.tick(15)


def multi_gamecreate():


def game_loop():
    pygame.mixer.music.play(-1 )

    global pause
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    dodged = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_w = 100
    thing_h = 100

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)


        things(thing_startx, thing_starty, thing_w, thing_h, black)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_h
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed +=1
            thing_w += (dodged*1.2)


        if y < thing_starty+thing_h:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_w:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
