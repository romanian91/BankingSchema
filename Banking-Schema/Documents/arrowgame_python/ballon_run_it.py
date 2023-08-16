import pygame, random, sys, time
from pygame.locals import *

WINDOWWIDTH = 1364
WINDOWHEIGHT = 760

MAXGOTTENPASS = 10
BALLONSIZE = 70 #includes newKindZombies
BALLON1RATE = 900
BALLON2RATE = 150
BALLON3RATE = 150
BALLON4RATE = 150
BALLON5RATE = 150
ARROWSIZE=20
BALLONSPEED = 1

PLAYERMOVERATE = 15
ARROWSPEED = 10
ARROWRATE = 20

TEXTCOLOR = (255, 20, 20)
RED = (255, 0, 0)
FPS=60

def terminate():
    pygame.quit()
    sys.exit()

def ArrowHasHitBallon(Arrows, Ballons):
    for a in Arrows:
        if a['rect'].colliderect(b['rect']):
            Arrows.remove(a)
            pygame.mixer.music.load('hit.wav')
            pygame.mixer.music.play(-1, 0.0)
            pygame.mixer.music.set_volume(20.0)
            return True
    return False
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                if event.key == K_RETURN:
                    return


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),pygame.FULLSCREEN,32)#, pygame.FULLSCREEN)
pygame.display.flip()
pygame.display.set_caption('Baloon Hitting')
pygame.mouse.set_visible(False)

# set up fonts
font = pygame.font.SysFont(None, 48)

# set up sounds
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('grasswalk.mp3')

# set up images
playerImg = pygame.image.load('player2.gif')
playerRect = playerImg.get_rect()

Ballon1Img = pygame.image.load('blue.gif')
Ballon1Rect = Ballon1Img.get_rect()

Ballon2Img = pygame.image.load('green.gif')
Ballon2Rect = Ballon2Img.get_rect()

Ballon3Img = pygame.image.load('orange.gif')
Ballon3Rect = Ballon3Img.get_rect()

Ballon4Img = pygame.image.load('purple.gif')
Ballon4Rect = Ballon4Img.get_rect()

Ballon5Img = pygame.image.load('red.gif')
Ballon5Rect = Ballon5Img.get_rect()

ArrowImg = pygame.image.load('arrow1.gif')
ArrowRect = ArrowImg.get_rect()
ArrowRect.width=60
ArrowRect.height=30
BackgroundImg = pygame.image.load('background.png')
FitBackground = pygame.transform.scale(BackgroundImg,(WINDOWWIDTH,WINDOWHEIGHT))

#Set up sounds
GameOverSound=pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('grasswalk.mp3')

# Start Screen
windowSurface.blit(FitBackground,(0,0))

#pygame.display.flip()
windowSurface.blit(playerImg,(WINDOWWIDTH/2,WINDOWHEIGHT/2+50))

drawText('Hit Ballons with Arrow and Enjoy',font,windowSurface,WINDOWWIDTH/3,WINDOWHEIGHT/3)
drawText('Press Enter to Play ',font,windowSurface,WINDOWWIDTH/3+80,WINDOWHEIGHT/3+60)
pygame.display.update()
waitForPlayerToPressKey()

while True:
    Ballon1=[]
    Ballon2=[]
    Ballon3=[]
    Ballon4=[]
    Ballon5=[]
    Arrows=[]
    
    Ballonmissed=0
    score=0
    playerRect.topleft=(-5,WINDOWHEIGHT/2)

    count1=count2=count3=count4=count5=0
    Arrowcount=30

    pygame.mixer.music.play(-1, 0.0)
    Moveup=Movedown=Moveright=Moveleft=False
    shoot=False

    while True:
        # Event Handling
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==KEYDOWN:
                if event.key==K_UP or event.key==ord('w'):
                    Moveup=True
                    Movedown=Moveright=Moveleft=False
                if event.key==K_DOWN or event.key==ord('s'):
                    Movedown=True
                    Movedup=Moveright=Moveleft=False
                if event.key==K_RIGHT or event.key==ord('d'):
                    Moveright=True
                    Movedown=Moveup=Moveleft=False
                if event.key==K_LEFT or event.key==ord('a'):
                    Moveleft=True
                    Movedown=Moveright=Moveup=False
                if event.key==K_SPACE:
                    shoot=True
            if event.type==KEYUP:
                if event.key==K_ESCAPE:
                    terminate()
                if event.key==K_UP or event.key==ord('w'):
                    Moveup=False
                if event.key==K_DOWN or event.key==ord('s'):
                    Movedown=False
                if event.key==K_RIGHT or event.key==ord('d'):
                    Moveright=False
                if event.key==K_LEFT or event.key==ord('a'):
                    Moveleft=False
                if event.key==K_SPACE:
                    shoot=False
        # ADDING BALOONS IN SCREEN
        count1+=1
        if count1==BALLON1RATE:
            count1=0
            Ballon1size=BALLONSIZE
            NewBallon1= {'rect': pygame.Rect(random.randint(200,WINDOWWIDTH-BALLONSIZE-20),WINDOWHEIGHT,Ballon1size,Ballon1size),
                        'surface': pygame.transform.scale(Ballon1Img,(Ballon1size,Ballon1size))
                        }
            Ballon1.append(NewBallon1)

        count2+=1
        if count2==BALLON2RATE:
            count2=0
            Ballon2size=BALLONSIZE
            NewBallon2={'rect':pygame.Rect(random.randint(200,WINDOWWIDTH-BALLONSIZE-20),WINDOWHEIGHT,Ballon2size,Ballon2size),
                        'surface':pygame.transform.scale(Ballon2Img,(Ballon2size,Ballon2size))
                }
            Ballon2.append(NewBallon2)

        count3+=1
        if count3==BALLON3RATE:
            count3=0
            Ballon3size=BALLONSIZE
            NewBallon3={'rect':pygame.Rect(random.randint(200,WINDOWWIDTH-BALLONSIZE-20),WINDOWHEIGHT,Ballon3size,Ballon3size),
                       'surface':pygame.transform.scale(Ballon3Img,(Ballon3size,Ballon3size))
               }
            Ballon3.append(NewBallon3)

        count4+=1
        if count4==BALLON4RATE:
            count4=0
            Ballon4size=BALLONSIZE
            NewBallon4={'rect':pygame.Rect(random.randint(200,WINDOWWIDTH-BALLONSIZE-20),WINDOWHEIGHT,Ballon4size,Ballon4size),
                        'surface':pygame.transform.scale(Ballon4Img,(Ballon4size,Ballon4size))
                }
            Ballon4.append(NewBallon4)

        count5+=1
        if count5==BALLON5RATE:
            count5=0
            Ballon5size=BALLONSIZE
            NewBallon5={'rect':pygame.Rect(random.randint(200,WINDOWWIDTH-BALLONSIZE-20),WINDOWHEIGHT,Ballon5size,Ballon5size),
                        'surface':pygame.transform.scale(Ballon5Img,(Ballon5size,Ballon5size))
                }
            Ballon5.append(NewBallon5)

        Arrowcount+=1
        if Arrowcount>=ARROWRATE and shoot==True:
            Arrowcount=0
            newArrow={'rect':pygame.Rect(playerRect.centerx+20,playerRect.centery-35,ArrowRect.width,ArrowRect.height),
                        'surface':pygame.transform.scale(ArrowImg,(ArrowRect.width,ArrowRect.height))
                }
            Arrows.append(newArrow)

        # Move the player around.
        if Moveup and playerRect.top > 0:
            playerRect.move_ip(0,-1 * PLAYERMOVERATE)
        if Movedown and playerRect.bottom < WINDOWHEIGHT+5:
            playerRect.move_ip(0,PLAYERMOVERATE)
        if Moveright and playerRect.right > 30 and playerRect.right<200:
            playerRect.move_ip(PLAYERMOVERATE,0)
        if Moveleft and playerRect.left < WINDOWWIDTH-30 and  playerRect.left>5:
            playerRect.move_ip(-1*PLAYERMOVERATE,0)

        # Moving Balloons up
        for b in Ballon1:
            b['rect'].move_ip(0,-1*BALLONSPEED)
        for b in Ballon2:
            b['rect'].move_ip(0,-1*BALLONSPEED*1.5)
        for b in Ballon3:
            b['rect'].move_ip(0,-1*BALLONSPEED*2.0)
        for b in Ballon4:
            b['rect'].move_ip(0,-1*BALLONSPEED*3.0)
        for b in Ballon5:
            b['rect'].move_ip(0,-1*BALLONSPEED*2.5)

        # Moving the Arrow
        for a in Arrows:
            a['rect'].move_ip(1 * ARROWSPEED, 0)

        # Delete Balloons that are passed
         # Delete zombies that have fallen past the bottom.
        for b in Ballon1[:]:
            if b['rect'].bottom < 0:
                Ballon1.remove(b)
                Ballonmissed+= 1
        for b in Ballon2[:]:
            if b['rect'].bottom < 0:
                Ballon2.remove(b)
                Ballonmissed+= 1
        for b in Ballon3[:]:
            if b['rect'].bottom < 0:
                Ballon3.remove(b)
                Ballonmissed+= 1
        for b in Ballon4[:]:
            if b['rect'].bottom < 0:
                Ballon4.remove(b)
                Ballonmissed+= 1
        for b in Ballon5[:]:
            if b['rect'].bottom < 0:
                Ballon5.remove(b)
                Ballonmissed+= 1
        for a in Arrows[:]:
            if a['rect'].right>WINDOWWIDTH:
                Arrows.remove(a)

       # check if the Arrow has hit the Ballon
        for b in Ballon1:
            if ArrowHasHitBallon(Arrows, Ballon1):
                score += 1
                Ballon1.remove(b)
        for b in Ballon2:
            if ArrowHasHitBallon(Arrows, Ballon2):
                score += 1
                Ballon2.remove(b)
        for b in Ballon3:
            if ArrowHasHitBallon(Arrows, Ballon3):
                score += 1
                Ballon3.remove(b)
        for b in Ballon4:
            if ArrowHasHitBallon(Arrows, Ballon4):
                score += 1
                Ballon4.remove(b)
        for b in Ballon5:
            if ArrowHasHitBallon(Arrows, Ballon5):
                score += 1
                Ballon5.remove(b)

          # Draw the game world on the window.
        windowSurface.blit(FitBackground, (0, 0))

        # Draw the player's rectangle, rails
        windowSurface.blit(playerImg, playerRect)

        # Draw each baddie
        for b in Ballon1:
            windowSurface.blit(b['surface'], b['rect'])
        for b in Ballon2:
            windowSurface.blit(b['surface'], b['rect'])
        for b in Ballon3:
            windowSurface.blit(b['surface'], b['rect'])
        for b in Ballon4:
            windowSurface.blit(b['surface'], b['rect'])
        for b in Ballon5:
            windowSurface.blit(b['surface'], b['rect'])


        # draw each Arrow
        for a in Arrows:
            windowSurface.blit(a['surface'], a['rect'])

        # Draw the score and how many ballons got past
        drawText('Ballons gotten past: %s' % (Ballonmissed), font, windowSurface, 10, 20)
        drawText('Score: %s' % (score), font, windowSurface, 10, 50)

        # update the display
        pygame.display.update()
        mainClock.tick(FPS)

        # check if score is over MAXGOTTENPASS which means game over
        if Ballonmissed >= MAXGOTTENPASS:
            break

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()
    time.sleep(1)
    if Ballonmissed >= MAXGOTTENPASS:
        windowSurface.blit(FitBackground, (0, 0))
        windowSurface.blit(playerImg, (WINDOWWIDTH / 2, WINDOWHEIGHT/2))
        drawText('Score: %s' % (score), font, windowSurface, WINDOWWIDTH/3+150, WINDOWHEIGHT/3-60)
        drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3)+130, (WINDOWHEIGHT / 3))
        drawText('Press enter to play again or escape to exit', font, windowSurface, (WINDOWWIDTH / 4)+60 - 80, (WINDOWHEIGHT / 3) + 50)
        pygame.display.update()
        waitForPlayerToPressKey()

    gameOverSound.stop()
