import pygame
import random
import math
from bar import bar
from ball import ball
from pygame import mixer

# this comment is to test github commit functionality
# second comment 

pygame.init()

win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Infinite Pong")
icon = pygame.image.load('icon.png')
pygame.display.set_icon=(icon)

background = pygame.image.load('background.png') # 1000x500
menuBackgroundRed = pygame.image.load('menuBackgroundRed.png') # 1000x500
menuBackgroundWhite = pygame.image.load('menuBackgroundWhite.png') # 1000x500

player = bar("p")
enemy = bar("e")
ball = ball()
# game loop

run = True
menu = True
gameRunning = False

while run:
	win.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	while menu:
		if pygame.Rect(200, 150, 600, 150).collidepoint(pygame.mouse.get_pos()) :
			win.blit(menuBackgroundRed, (0,0))
		else : win.blit(menuBackgroundWhite, (0,0))

		event = pygame.event.get()

		for event in event:
			if event.type == pygame.QUIT:
				menu = False
				run = False
			elif event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect(200, 150, 600, 150).collidepoint(pygame.mouse.get_pos()):
				menu = False
				gameRunning = True

		pygame.display.update()	

	win.blit(background, (0,0))

	while gameRunning:

		win.blit(background, (0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameRunning = False
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

		#if (ball.getCoord('x')<65 and (ball.getCoord('y')>player.getCoord('y') and ball.getCoord('y')<player.getCoord('y')+100)) :
		if (ball.rectFrame.colliderect(player.rectFrame)):
			#ball.changeDirection()
			print('collided')
			
		if ball.getCoord('x')<35 :
			ball.reset()
			player.reset('p')
			gameRunning = False
			menu = True



		ball.setCoord('x',ball.getCoord('v'))

		win.blit(player.getImage(), (player.getCoord('x'),player.getCoord('y')))
		win.blit(enemy.getImage(), (enemy.getCoord('x'),enemy.getCoord('y')))
		win.blit(ball.getImage(), (ball.getCoord('x'),ball.getCoord('y')))
		pygame.display.update()


pygame.quit()
quit()
