import pygame
import random
import math
from pygame import mixer

class bar:
	def __init__(self, type):

		self.image = pygame.image.load('bar.png') # 15x100

		if type=="p":
			self.xcoord = 50
			self.ycoord = 200
			self.rectFrame = pygame.Rect(50, 200, 15, 100)

		elif type=="e":
			self.xcoord = 950
			self.ycoord = 200
			self.rectFrame = pygame.Rect(950, 200, 15, 100)

	def getImage(self):
		return self.image

	def getCoord(self,type):
		if type=="x" :
			return self.xcoord
		elif type=="y" :
			return self.ycoord

	def setCoord(self,type,val):
		if type=="x" :
			self.xcoord+=val
			self.rectFrame.move(val,0)
		elif type=="y" :
			self.ycoord+=val
			self.rectFrame.move(0,val)

	# this method is redundant. I should just instantiate a new object.
	def reset(self, type):
		if type=="p":
			self.xcoord = 50
			self.ycoord = 200
			self.rectFrame = pygame.Rect(50, 200, 15, 100)
		elif type=="e":
			self.xcoord = 950
			self.ycoord = 200
			self.rectFrame = pygame.Rect(950, 200, 15, 100)
