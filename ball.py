import pygame
import random
import math
from pygame import mixer

class ball:
	def __init__(self):

		self.image = pygame.image.load('ball.png') # 15x100
		self.xcoord = 500
		self.ycoord = 250
		self.velocity = 1
		self.direction = 0

	def getImage(self):
		return self.image

	def getCoord(self,type):
		if type=="x" :
			return self.xcoord
		elif type=="y" :
			return self.ycoord
		elif type=="v" :
			return self.velocity

	def setCoord(self,type,val):
		if type=="x" :
			self.xcoord+=val
		elif type=="y" :
			self.ycoord+=val

	def changeDirection(self):
		self.velocity = -self.velocity
