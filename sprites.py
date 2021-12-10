import pygame

import sys

import random

import os

from settings import Settings

class menuLogo(pygame.sprite.Sprite):#complete
	def __init__(self, settings):
		super(menuLogo, self).__init__()
		self.y = 250
		self.settings = settings
		self.images = []
		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'mainmenulogo')
		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			self.images.append(image)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect((self.settings.screen_width-self.image.get_width())//2, 250, self.image.get_width(), self.image.get_height())
	def get_rect(self):
		return(self.rect)
	def update(self):
		self.index += 1
		if(self.index//10 >= len(self.images)):
			self.index = 0
		self.image = self.images[self.index//10]
	def load_image(self, path):
		image = pygame.image.load(path)
		return image

class startButton(pygame.sprite.Sprite):#complete
	def __init__(self, settings):
		super(startButton, self).__init__()
		self.y = 400
		self.settings = settings
		self.images = []
		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'startbutton')
		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			self.images.append(image)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(220	, 400, self.image.get_width(), self.image.get_height())
	def get_rect(self):
		return(self.rect)
	def update(self):
		None
	def onHover(self):
		self.image = self.images[1]
	def offHover(self):
		self.image = self.images[0]
	def load_image(self, path):
		image = pygame.image.load(path)
		return image

class quitButton(pygame.sprite.Sprite):#complete
	def __init__(self, settings):
		super(quitButton, self).__init__()
		self.y = 400
		self.settings = settings
		self.images = []
		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'quitbutton')
		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			self.images.append(image)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(450, 400, self.image.get_width(), self.image.get_height())
	def get_rect(self):
		return(self.rect)
	def update(self):
		None
	def onHover(self):
		self.image = self.images[1]
	def offHover(self):
		self.image = self.images[0]
	def load_image(self, path):
		image = pygame.image.load(path)
		return image

class Cloud(pygame.sprite.Sprite):#complete
	def __init__(self, settings):
		super(Cloud, self).__init__()
		self.x = random.randint(0, 800)
		self.y = random.randint(20, 150)
		self.settings = settings
		self.images = []
		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'clouds')
		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			self.images.append(image)
		self.index = random.randint(0, 17)
		self.image = self.images[self.index]
		self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

		self.velocity = random.randint(5, 20)/20
		if(random.randint(0, 1) == 1):
			self.velocity *= -1

	def update(self):
		self.x += self.velocity*2
		self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
	def get_rect(self):
		return(self.rect)
	def load_image(self, path):
		image = pygame.image.load(path)
		return image

class Ground(pygame.sprite.Sprite):#complete
	def __init__(self, x, settings):
		super(Ground, self).__init__()
		self.settings = settings
		self.x = x
		self.y = self.settings.screen_height-24
		self.images = []
		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'ground')
		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			self.images.append(image)
		self.image = self.images[0]
		self.rect = pygame.Rect(self.x, self.y, self.image.get_width()+100, self.image.get_height())
	def update(self):
		self.rect = pygame.Rect(self.x, self.y, self.image.get_width()+100, self.image.get_height())
	def get_rect(self):
		return(self.rect)
	def get_image(self):
		return(self.image)
	def load_image(self, path):
		image = pygame.image.load(path)
		return image

class Player(pygame.sprite.Sprite):#needs transformation
	def __init__(self, settings):
		super(Player, self).__init__()
		self.settings = settings
		self.wrap = True
		self.tick = 0
		self.releaseGetsuga = 0

		self.power = 0
		self.kills = 0

		self.standleft = []
		self.standright = []
		self.walkright = []
		self.walkleft = []

		self.swingright = []

		self.swingright1 = []
		self.swingright2 = []
		self.swingright3 = []

		self.swingleft = []

		self.swingleft1 = []
		self.swingleft2 = []
		self.swingleft3 = []

		self.swingupfromleft = []
		self.swingupfromright = []

		self.dieFromLeft = []
		self.dieFromRight = []

		self.getsugaright = []
		self.getsugaleft = []

		self.standleftbase = []
		self.standrightbase = []
		self.walkrightbase = []
		self.walkleftbase = []

		self.standleftvizard = []
		self.standrightvizard = []
		self.walkrightvizard = []
		self.walkleftvizard = []

		self.swingleft1base = []
		self.swingleft2base = []
		self.swingleft3base = []

		self.swingleft1vizard = []
		self.swingleft2vizard = []
		self.swingleft3vizard = []

		self.swingright1base = []
		self.swingright2base = []
		self.swingright3base = []

		self.swingright1vizard = []
		self.swingright2vizard = []
		self.swingright3vizard = []

		self.swingupfromleftbase = []
		self.swingupfromrightbase = []

		self.swingupfromleftvizard = []
		self.swingupfromrightvizard = []

		self.dieFromLeftbase = []
		self.dieFromRightbase = []

		self.dieFromLeftvizard = []
		self.dieFromRightvizard = []

		self.getsugarightvizard = []
		self.getsugaleftvizard = []

		self.toVizard = []

		self.form = 'base'

		self.swinging = False

		self.transforming = False

		self.isDead = False

		self.currentAnimation = "walkRight"
		self.animationFrame = 0

		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'character', 'base')

		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			if(file_name.find("standleft") >= 0):
				self.standleftbase.append(image)
			elif(file_name.find("standright") >= 0):
				self.standrightbase.append(image)
			elif(file_name.find("walkleft") >= 0):
				self.walkleftbase.append(image)
			elif(file_name.find("walkright") >= 0):
				self.walkrightbase.append(image)
			elif(file_name.find("swingright1") >= 0):
				self.swingright1base.append(image)
			elif(file_name.find("swingleft1") >= 0):
				self.swingleft1base.append(image)
			elif(file_name.find("swingright2") >= 0):
				self.swingright2base.append(image)
			elif(file_name.find("swingleft2") >= 0):
				self.swingleft2base.append(image)
			elif(file_name.find("swingright3") >= 0):
				self.swingright3base.append(image)
			elif(file_name.find("swingleft3") >= 0):
				self.swingleft3base.append(image)
			elif(file_name.find("deathfromleft") >= 0):
				self.dieFromLeftbase.append(image)
			elif(file_name.find("deathfromright") >= 0):
				self.dieFromRightbase.append(image)
			elif(file_name.find("swingupfromright") >= 0):
				self.swingupfromrightbase.append(image)
			elif(file_name.find("swingupfromleft") >= 0):
				self.swingupfromleftbase.append(image)

		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'character', 'vizard')

		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			if(file_name.find("standleft") >= 0):
				self.standleftvizard.append(image)
			elif(file_name.find("standright") >= 0):
				self.standrightvizard.append(image)
			elif(file_name.find("walkleft") >= 0):
				self.walkleftvizard.append(image)
			elif(file_name.find("walkright") >= 0):
				self.walkrightvizard.append(image)
			elif(file_name.find("swingright1") >= 0):
				self.swingright1vizard.append(image)
			elif(file_name.find("swingleft1") >= 0):
				self.swingleft1vizard.append(image)
			elif(file_name.find("swingright2") >= 0):
				self.swingright2vizard.append(image)
			elif(file_name.find("swingleft2") >= 0):
				self.swingleft2vizard.append(image)
			elif(file_name.find("swingright3") >= 0):
				self.swingright3vizard.append(image)
			elif(file_name.find("swingleft3") >= 0):
				self.swingleft3vizard.append(image)
			elif(file_name.find("deathfromleft") >= 0):
				self.dieFromLeftvizard.append(image)
			elif(file_name.find("deathfromright") >= 0):
				self.dieFromRightvizard.append(image)
			elif(file_name.find("swingupfromright") >= 0):
				self.swingupfromrightvizard.append(image)
			elif(file_name.find("swingupfromleft") >= 0):
				self.swingupfromleftvizard.append(image)
			elif(file_name.find("getsugaright") >= 0):
				self.getsugarightvizard.append(image)
			elif(file_name.find("getsugaleft") >= 0):
				self.getsugaleftvizard.append(image)

		self.standleft = self.standleftbase
		self.standright = self.standrightbase
		self.walkleft = self.walkleftbase
		self.walkright = self.walkrightbase
		self.swingleft1 =self.swingleft1base
		self.swingleft2 =self.swingleft2base
		self.swingleft3 =self.swingleft3base
		self.swingright1 = self.swingright1base
		self.swingright2 = self.swingright2base
		self.swingright3 = self.swingright3base
		self.swingupfromleft = self.swingupfromleftbase
		self.swingupfromright = self.swingupfromrightbase
		self.dieFromLeft = self.dieFromLeftbase
		self.dieFromRight = self.dieFromRightbase

		self.swingleft = self.swingleft3
		self.swingright = self.swingright3

		self.getsugaright = self.swingright2
		self.getsugaleft = self.swingleft2
		self.getsugaupfromright =  self.swingright2
		self.getsugaupfromleft = self.swingleft2

		self.image = self.standleft[0]
		self.x = 50
		self.y = self.settings.screen_height-50-self.image.get_height()
		self.minY = self.settings.screen_height-25-self.image.get_height()

		self.velocity = 0
		self.yVelocity = 0
		self.gravity = False

		self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
	def transformToVizard(self):
		self.velocity = 0
		self.form = 'vizard'
		self.swinging = False
		self.standleft = self.standleftvizard
		self.standright = self.standrightvizard
		self.walkleft = self.walkleftvizard
		self.walkright = self.walkrightvizard
		self.swingleft1 =self.swingleft1vizard
		self.swingleft2 =self.swingleft2vizard
		self.swingleft3 =self.swingleft3vizard
		self.swingright1 = self.swingright1vizard
		self.swingright2 = self.swingright2vizard
		self.swingright3 = self.swingright3vizard
		self.swingupfromleft = self.swingupfromleftvizard
		self.swingupfromright = self.swingupfromrightvizard
		self.dieFromLeft = self.dieFromLeftvizard
		self.dieFromRight = self.dieFromRightvizard

		self.swingleft = self.swingleft3
		self.swingright = self.swingright3

		self.getsugaright = self.getsugarightvizard
		self.getsugaleft = self.getsugaleftvizard
		self.getsugaupfromright =  self.getsugarightvizard
		self.getsugaupfromleft = self.getsugaleftvizard

		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'character', 'toVizard')
		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			if(file_name.find("toVizard") >= 0):
				self.toVizard.append(image)
		self.animationFrame = -1
		self.transforming = True
		self.currentAnimation = "toVizard"
	def isSwinging(self):
		return(self.swinging)
	def get_rect(self):
		return(self.rect)
	def get_image(self):
		return(self.image)
	def setVelocity(self, n):
		self.velocity = n
	def setYVelocity(self, n):
		self.yVelocity = n
	def jump(self):
		self.yVelocity += 30
	def setGravity(self, b):
		self.gravity = b
	def setAnimation(self, s):
		self.currentAnimation = s
	def continueAnimation(self):
		if(self.transforming):
			if(self.tick%15 != 0):
				return
			if(self.currentAnimation == "toVizard"):
				self.animationFrame += 1
				if(self.animationFrame >= len(self.toVizard)):
					self.transforming = False
					self.swinging = False
					self.tick = 0
					self.animationFrame -= 1
			self.image = self.toVizard[self.animationFrame]
			return
		if(self.isDead):
			return
		if(self.currentAnimation == "deathFromRight"):
			if(self.tick%6 != 0):
				return
			self.animationFrame += 1
			if(self.animationFrame >= len(self.dieFromRight)):
				self.isDead = True
				self.animationFrame -= 1
			self.image = self.dieFromRight[self.animationFrame]
			return
		elif(self.currentAnimation == "deathFromLeft"):
			if(self.tick%6 != 0):
				return
			self.animationFrame += 1
			if(self.animationFrame >= len(self.dieFromLeft)):
				self.isDead = True
				self.animationFrame -= 1
			self.image = self.dieFromLeft[self.animationFrame]
			return
		if(self.swinging):
			if(self.tick%4 != 0):
				return
			self.animationFrame += 1
			if(self.currentAnimation == "swingingRight"):
				if(self.animationFrame >= len(self.swingright)):
					self.animationFrame -= 1
					self.swinging = False
				self.image = self.swingright[self.animationFrame]
			elif(self.currentAnimation == "swingingLeft"):
				if(self.animationFrame >= len(self.swingleft)):
					self.animationFrame -= 1
					self.swinging = False
				self.image = self.swingleft[self.animationFrame]
			elif(self.currentAnimation == "swingingUpFromLeft"):
				if(self.animationFrame >= len(self.swingupfromleft)):
					self.animationFrame -= 1
					self.swinging = False
				self.image = self.swingupfromleft[self.animationFrame]
			elif(self.currentAnimation == "swingingUpFromRight"):
				if(self.animationFrame >= len(self.swingupfromright)):
					self.animationFrame -= 1
					self.swinging = False
				self.image = self.swingupfromright[self.animationFrame]
			elif(self.currentAnimation == "getsugaRight"):
				if(self.animationFrame >= len(self.getsugaright)):
					self.animationFrame -= 1
					self.swinging = False
				elif(self.animationFrame == len(self.getsugaright)-2):
					self.releaseGetsuga = 1
				self.image = self.getsugaright[self.animationFrame]
			elif(self.currentAnimation == "getsugaLeft"):
				if(self.animationFrame >= len(self.getsugaleft)):
					self.animationFrame -= 1
					self.swinging = False
				elif(self.animationFrame == len(self.getsugaleft)-2):
					self.releaseGetsuga = 2
				self.image = self.getsugaleft[self.animationFrame]
			elif(self.currentAnimation == "getsugaUpFromLeft"):
				if(self.animationFrame >= len(self.getsugaupfromleft)):
					self.animationFrame -= 1
					self.swinging = False
				elif(self.animationFrame == len(self.getsugaupfromleft)-2):
					self.releaseGetsuga = 3
				self.image = self.getsugaupfromleft[self.animationFrame]
			elif(self.currentAnimation == "getsugaUpFromRight"):
				if(self.animationFrame >= len(self.getsugaupfromright)):
					self.animationFrame -= 1
					self.swinging = False
				elif(self.animationFrame == len(self.getsugaupfromright)-2):
					self.releaseGetsuga = 1
				self.image = self.getsugaupfromright[self.animationFrame]
			return


		if(self.tick%2 != 0):
			return
		
		self.animationFrame += 1
		if(self.currentAnimation == "walkRight"):
			if(self.animationFrame >= len(self.walkright)):
				self.animationFrame = 0
			self.image = self.walkright[self.animationFrame]
			self.velocity = 1
		elif(self.currentAnimation == "walkLeft"):
			if(self.animationFrame >= len(self.walkleft)):
				self.animationFrame = 0
			self.image = self.walkleft[self.animationFrame]
			self.velocity = -1
		elif(self.currentAnimation == "standRight"):
			if(self.animationFrame >= len(self.standright)):
				self.animationFrame = 0
			self.image = self.standright[self.animationFrame]
			self.velocity = 0
		elif(self.currentAnimation == "standLeft"):
			if(self.animationFrame >= len(self.standleft)):
				self.animationFrame = 0
			self.image = self.standleft[self.animationFrame]
			self.velocity = 0
		elif(self.currentAnimation == "dieFromLeft"):
			if(self.animationFrame >= len(self.dieFromLeft)):
				self.animationFrame = 0
				self.isDead = True
			self.image = self.dieFromLeft[self.animationFrame]

	def update(self):
		#update internal tick
		self.tick += 1
		if(self.tick < 120):
			self.isDead = False
		if(self.tick%10 == 0):
			self.power += 1
			self.power = min(self.power, 1000)

		#animation updates
		self.continueAnimation()

		#positional updates
		self.x += self.velocity*6

		if(self.gravity):
			self.yVelocity -= 2
			self.yVelocity = max(-20, self.yVelocity)
		
		changeY = self.yVelocity*-1
		self.y += self.yVelocity*-1
		if(self.wrap):
			if(self.x > 820):
				self.x = -20
			elif(self.x < -20):
				self.x = 820
		else:
			if(self.get_rect().right > 800):
				self.x = 800 - self.image.get_width()/2
			elif(self.get_rect().left < 0):
				self.x = self.image.get_width()/2

		bottom = self.rect.bottom
		self.rect = pygame.Rect(self.x-self.image.get_width()/2, self.y, self.image.get_width(), self.image.get_height())
		self.rect.bottom = bottom + changeY
		self.y = self.rect.top

class Hollow(pygame.sprite.Sprite):#complete
	def __init__(self ,x1, x2 , y1, y2, settings):

		super(Hollow, self).__init__()
		self.settings = settings
		self.tick = 0

		self.maxX = x2

		self.standleft = []
		self.standright = []
		self.walkright = []
		self.walkleft = []

		self.deathfacingright = []
		self.deathfacingleft = []

		self.swinging = False

		self.currentAnimation = "walkRight"
		self.animationFrame = 0

		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'hollows')

		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			if(file_name.find("standleft") >= 0):
				self.standleft.append(image)
			elif(file_name.find("standright") >= 0):
				self.standright.append(image)
			elif(file_name.find("walkleft") >= 0):
				self.walkleft.append(image)
			elif(file_name.find("walkright") >= 0):
				self.walkright.append(image)
			elif(file_name.find("deathfacingright") >= 0):
				self.deathfacingright.append(image)
			elif(file_name.find("deathfacingleft") >= 0):
				self.deathfacingleft.append(image)

		self.image = self.standleft[0]

		self.dying = -1
		self.isDead = False

		self.x = random.randint(x1, x2)

		self.y = random.randint(y1, y2)
		self.minY = self.settings.screen_height-25-self.image.get_height()

		self.velocity = random.randint(-2, 2)
		self.yVelocity = 0

		self.gravity = True

		self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
	def get_rect(self):
		return(self.rect)
	def get_image(self):
		return(self.image)
	def setGravity(self, b):
		self.gravity = b
	def setAnimation(self, s):
		self.currentAnimation = s
	def continueAnimation(self):
		if(self.tick%5 != 0):
			return
		self.animationFrame += 1
		if(self.currentAnimation == "deathFacingLeft"):
			if(self.animationFrame >= len(self.deathfacingleft)):
				self.isDead = True
				self.animationFrame -= 1
			self.image = self.deathfacingleft[self.animationFrame]
			return
		elif(self.currentAnimation == "deathFacingRight"):
			if(self.animationFrame >= len(self.deathfacingright)):
				self.isDead = True
				self.animationFrame -= 1
			self.image = self.deathfacingright[self.animationFrame]
			return
		if(self.tick%15 != 0):
			return
		self.animationFrame += 1
		if(self.currentAnimation == "walkRight"):
			if(self.animationFrame >= len(self.walkright)):
				self.animationFrame = 0
			self.image = self.walkright[self.animationFrame]
		elif(self.currentAnimation == "walkLeft"):
			if(self.animationFrame >= len(self.walkleft)):
				self.animationFrame = 0
			self.image = self.walkleft[self.animationFrame]
		elif(self.currentAnimation == "standRight"):
			if(self.animationFrame >= len(self.standright)):
				self.animationFrame = 0
			self.image = self.standright[self.animationFrame]
		elif(self.currentAnimation == "standLeft"):
			if(self.animationFrame >= len(self.standleft)):
				self.animationFrame = 0
			self.image = self.standleft[self.animationFrame]
	def update(self):
		#animation updates
		if(self.currentAnimation.lower().find("death") >= 0):
			self.continueAnimation()
		elif(self.tick%60 == 0):
			self.jump = random.randint(0, 1)
			if(self.jump == 0):
				self.yVelocity += 15
			self.velocity = random.randint(-2, 2)
			if(self.velocity == 0):
				if(self.currentAnimation == "standLeft"):
					self.continueAnimation()
				elif(self.currentAnimation == "walkLeft"):
					self.animationFrame = -1
					self.currentAnimation = "standLeft"
					self.continueAnimation()
				elif(self.currentAnimation == "standRight"):
					self.continueAnimation()
				elif(self.continueAnimation == "walkRight"):
					self.animationFrame = -1
					self.currentAnimation = "standRight"
					self.continueAnimation()
			elif(self.velocity > 0):
				if(self.currentAnimation == "walkRight"):
					self.continueAnimation()
				else:
					self.animationFrame = -1
					self.currentAnimation = "walkRight"
					self.continueAnimation()
			elif(self.velocity < 0):
				if(self.currentAnimation == "walkLeft"):
					self.continueAnimation()
				else:
					self.animationFrame = -1
					self.currentAnimation = "walkLeft"
					self.continueAnimation()
		else:
			self.continueAnimation()

		self.tick += 1
		if(self.tick%3 == 0):
			self.x += self.velocity*2

		if(self.gravity):
			self.yVelocity -= 2
			self.yVelocity = max(-20, self.yVelocity)
		
		self.y += self.yVelocity*-1

		self.tick += 1

		if(self.x < 0):
			self.isDead = True
		elif(self.x > self.maxX):
			self.isDead = True

		self.rect = pygame.Rect(self.x-self.image.get_width()/2, self.y, self.image.get_width(), self.image.get_height())

class Getsuga(pygame.sprite.Sprite):#needs transformation
	def __init__(self, vX, vY, x, y, settings, form):
		super(Getsuga, self).__init__()

		self.form = form

		self.settings = settings
		self.tick = 0

		self.move = []

		self.moveright1 = []
		self.moveleft1 = []
		self.moveup1 = []

		self.animationFrame = 0

		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'getsugas', self.form)

		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			if(file_name.find("getsugaleft1base") >= 0):
				self.moveleft1.append(image)
			elif(file_name.find("getsugaright1base") >= 0):
				self.moveright1.append(image)
			elif(file_name.find("getsugaup1base") >= 0):
				self.moveup1.append(image)

		self.x = x

		self.y = y

		self.velocityX = vX

		self.velocityY = vY

		if(self.velocityY > 0):
			self.move = self.moveup1
		elif(self.velocityX > 0):
			self.move = self.moveright1
		elif(self.velocityX < 0):
			self.move = self.moveleft1

		self.currentAnimation = "move"

		self.image = self.move[0]

		self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
	def get_rect(self):
		return(self.rect)
	def get_image(self):
		return(self.image)
	def setAnimation(self, s):
		self.currentAnimation = s
	def continueAnimation(self):
		if(self.tick%3 != 0):
			return
		self.animationFrame += 1
		if(self.currentAnimation == "move"):
			if(self.animationFrame >= len(self.move)):
				self.animationFrame = 0
			self.image = self.move[self.animationFrame]
	def update(self):
		#animation updates
		self.continueAnimation()

		self.x += self.velocityX*10
		self.y += self.velocityY*-10

		self.rect = pygame.Rect(self.x-self.image.get_width()/2, self.y, self.image.get_width(), self.image.get_height())

class Platform(pygame.sprite.Sprite):#complete
	def __init__(self, x, y, settings):
		super(Platform, self).__init__()
		self.settings = settings
		self.tick = 0

		self.platforms = []

		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'platforms')

		for file_name in os.listdir(self.path):
			image = pygame.image.load(os.path.join(self.path, file_name))
			if(file_name.find("platform") >= 0):
				self.platforms.append(image)

		self.x = x

		self.y = y

		self.image = self.platforms[random.randint(0, len(self.platforms)-1)]

		self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
	def get_rect(self):
		return(self.rect)
	def get_image(self):
		return(self.image)
	def update(self):
		self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())#complete