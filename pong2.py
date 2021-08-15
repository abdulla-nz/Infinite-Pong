import pygame
import random
import math
from bar import bar
from ball import ball
from pygame import mixer

pygame.init()

win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Infinite Pong")
icon = pygame.image.load('icon.png')
pygame.display.set_icon=(icon)

background = pygame.image.load('background.png') # 1000x500

player = bar("p")
enemy = bar("e")
ball = ball()
# game loop

run = True
while run:
	win.fill((0,0,0))
	win.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP]:
		if player.getCoord('y')>0:
			player.setCoord('y',-1)
	elif keys[pygame.K_DOWN]:
		if player.getCoord('y')<400:
			player.setCoord('y',1)

	if (ball.getCoord('x')>925) :
		ball.changeDirection()

	if (ball.getCoord('x')<65 and (ball.getCoord('y')>player.getCoord('y') and ball.getCoord('y')<player.getCoord('y')+100)) :
		ball.changeDirection()



	ball.setCoord('x',ball.getCoord('v'))

	win.blit(player.getImage(), (player.getCoord('x'),player.getCoord('y')))
	win.blit(enemy.getImage(), (enemy.getCoord('x'),enemy.getCoord('y')))
	win.blit(ball.getImage(), (ball.getCoord('x'),ball.getCoord('y')))
	pygame.display.update()
	pygame.time.delay(3)

pygame.quit()
quit()