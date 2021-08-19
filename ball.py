import pygame
import random
import math
from pygame import mixer

class ball:
	def __init__(self):

		self.image = pygame.image.load('ball.png') # 15x100
		self.xcoord = 500
		self.ycoord = 250
		self.velocity = -1
		self.direction = 0

		self.rectFrame = pygame.Rect(500,250,25,25)

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
			self.rectFrame.move(val,0)
		elif type=="y" :
			self.ycoord+=val
			self.rectFrame.move(0,val)

	def changeDirection(self):
		if self.velocity<0:
			self.velocity = self.velocity-1
		else : self.velocity=self.velocity+1
		self.velocity = -self.velocity

	def reset(self):
		self.xcoord = 500
		self.ycoord = 250
		self.velocity = -1
		self.direction = 0
		self.rectFrame = pygame.Rect(500,250,25,25)