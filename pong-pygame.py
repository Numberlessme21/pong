def Ball(x,y):
    w.blit(ball, (x,y))

def BallClear(x,y):
    w.blit(dBall, (x,y))

def PaddleClear(x,y):
    w.blit(dPad, (x,y))

def Paddle(x,y):
    w.blit(pad, (x,y))

def collision(P, d, a):
    if P=="P":
        d *=-1
        a*=-1
    elif P == "S":
        d*=-1
        a = math.pi-a
    return [a,d]

def isCollision(d, a):
    if (50 < b_x < 60 and PlHitbox[0]<b_y<PlHitbox[1]) or (740<b_x<750 and PrHitbox[0]<b_y<PrHitbox[1]):
        [a,d] = collision("P", d, a)
    if 10<b_y<20 or 570<b_y<580:
        [a,d] = collision("S", d, a)
    return [a,d]

import pygame
import random as r
import math
alpha = 0.3*math.pi*r.random()
dir = pow(-1, r.choice([0,1]))
w = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong")
pygame.display.update()
pygame.init()
pygame.draw.rect(w, (255,255,255), rect=(10,10,780,580), width= 5)
pad = pygame.image.load("Paddle.png")
dPad = pygame.image.load("darkPaddle.png")
ball = pygame.image.load("Ball.png")
dBall = pygame.image.load("darkBall.png")
[l_x,l_y,r_x,r_y,b_x,b_y] = [50,225,750,225,400,300]

b = True
down = False

def isWin():
    if b_x <15:
        return [True,'R']
    elif b_x >765:
        return [True, 'L']
    else:
        return [False]

while b:
    pygame.draw.rect(w, (255,255,255), rect=(10,10,780,580), width= 5)
    Paddle(l_x,l_y)
    Paddle(r_x,r_y)
    Ball(b_x,b_y)
    PlHitbox = [l_y, l_y+150]
    PrHitbox = [r_y,r_y+150]
    [alpha,dir] = isCollision(dir, alpha)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            b = False
    if keys[pygame.K_UP] and r_y >20:
        PaddleClear(r_x,r_y)
        r_y -= 0.25
    if keys[pygame.K_DOWN] and r_y <420:
        PaddleClear(r_x,r_y)
        r_y += 0.25
    if keys[pygame.K_w] and l_y >20:
        PaddleClear(l_x,l_y)
        l_y -= 0.25
    if keys[pygame.K_s] and l_y <420:
        PaddleClear(l_x,l_y)
        l_y += 0.25
    BallClear(b_x,b_y)
    l = isWin()
    if l[0]:
        print(l[1],"Wins!")
        break
    b_x += dir*0.25*math.cos(alpha)
    b_y += dir*0.25*math.sin(alpha)
            