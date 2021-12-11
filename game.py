"""Chess game, for learning to grab images from a sprite sheet."""

import sys

import os

import time

import random

import pygame

from pygame import gfxdraw

from settings import Settings

from sprites import menuLogo
from sprites import startButton
from sprites import quitButton
from sprites import Cloud
from sprites import Ground
from sprites import Player
from sprites import Hollow
from sprites import Getsuga
from sprites import Platform

"""Overall class to manage game assets and behavior."""	

class Platformer:
	
	def __init__(self):
		"""Initialize the game, and create resources."""
		pygame.init()
		pygame.font.init()

		self.settings = Settings()
		self.prepareMenu()
	def prepareGame(self):
		self.settings.gameOver = False
		self.tick = 0

		self.gameEndCountDown = 10
		self.collidables = []
		self.enemies = []

		self.score = 0
		self.level = 0
		self.scrollspeed = 2

		self.gameFont = pygame.font.Font(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'zero-velocity-brk.regular.ttf'), 24)

		self.settings.setScreen("game")

		self.fpsClock = pygame.time.Clock()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("pyplatformer")

		#sprite/group initialization
		self.player = Player(self.settings)
		self.player.wrap = False
		self.playerGroup = pygame.sprite.Group()
		self.playerGroup.add(self.player)

		self.getsugas = []
		self.getsugaGroup = pygame.sprite.Group()

		self.hollowGroup = pygame.sprite.Group()
		for i in range(0, 5):
			self.enemies.append(Hollow(800, 1600, 0, 300, self.settings))
			self.hollowGroup.add(self.enemies[i])

		self.clouds = [Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings)]
		self.cloudGroup = pygame.sprite.Group()
		for cloud in self.clouds:
			self.cloudGroup.add(cloud)

		self.ground1 = Ground(0, self.settings)
		self.ground2 = Ground(800, self.settings)
		self.groundGroup = pygame.sprite.Group()
		self.groundGroup.add(self.ground1)
		self.groundGroup.add(self.ground2)

		self.collidables.append(self.ground1)
		self.collidables.append(self.ground2)

		self.platforms = []
		self.platformGroup = pygame.sprite.Group()
		self.generatePlatforms(random.randint(0, 5))
		for p in self.platforms:
			self.platformGroup.add(p)

		self.scoreText = self.gameFont.render("Score:", False, self.settings.white)
		self.scoreTextVal = self.gameFont.render(str(self.player.kills), False, self.settings.white)

		self.healthText = self.gameFont.render("Health: ", False, self.settings.white)
		self.healthTextVal = self.gameFont.render(str(self.player.health), False, self.settings.green)

		self.gameOverText = self.gameFont.render("", False, self.settings.red)

		self.powerText = self.gameFont.render("Power:", False, self.settings.white)
		

		self.powerRect = pygame.Rect(550, 10, self.player.power/1000 * 200, 25)
	def prepareMenu(self):
		self.settings.gameOver = False

		self.background = image = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'background', 'background.png'))

		self.collidables = []
		self.enemies = []

		self.gameFont = pygame.font.Font(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'zero-velocity-brk.regular.ttf'), 24)

		self.fpsClock = pygame.time.Clock()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("pyplatformer")

		#sprite/group initialization
		self.player = Player(self.settings)
		self.playerGroup = pygame.sprite.Group()
		self.playerGroup.add(self.player)

		self.getsugas = []
		self.getsugaGroup = pygame.sprite.Group()

		self.hollowGroup = pygame.sprite.Group()
		for i in range(0, 5):
			self.enemies.append(Hollow(0, 800, 0, 300, self.settings))
			self.hollowGroup.add(self.enemies[i])

		self.menuLogo = menuLogo(self.settings)
		self.menuLogoGroup = pygame.sprite.Group()
		self.menuLogoGroup.add(self.menuLogo)

		self.collidables.append(self.menuLogo)

		self.startButton = startButton(self.settings)
		self.startButtonGroup = pygame.sprite.Group()
		self.startButtonGroup.add(self.startButton)

		self.collidables.append(self.startButton)

		self.quitButton = quitButton(self.settings)
		self.quitButtonGroup = pygame.sprite.Group()
		self.quitButtonGroup.add(self.quitButton)

		self.collidables.append(self.quitButton)

		self.clouds = [Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings), Cloud(self.settings)]
		self.cloudGroup = pygame.sprite.Group()
		for cloud in self.clouds:
			self.cloudGroup.add(cloud)

		self.ground = Ground(0, self.settings)
		self.groundGroup = pygame.sprite.Group()
		self.groundGroup.add(self.ground)

		self.collidables.append(self.ground)

		self.highscoreText = self.gameFont.render("Highscore: ", False, self.settings.white)
		self.highscoreTextVal = self.gameFont.render(str(self.settings.highscore), False, self.settings.white)

		self.healthText = self.gameFont.render("Health: ", False, self.settings.white)
		self.healthTextVal = self.gameFont.render(str(self.player.health), False, self.settings.green)

		self.powerText = self.gameFont.render("Power:", False, self.settings.white)

		self.powerRect = pygame.Rect(550, 10, self.player.power/1000 * 200, 25)
	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			#runs game 30 times per second
			self.fpsClock.tick(self.settings.fps)
			self._check_events()
			self._update_screen()
	def _check_events(self):
		if(self.settings.screen == "main"):
			self._check_events_main_screen()
		elif(self.settings.screen == "game"):
			self._check_events_game_screen()
	def onGround(self, o):
		for element in self.collidables:
			if(o.get_rect().colliderect(element.get_rect()) and (o.get_rect().bottom <= element.get_rect().top+25)):
				return(True)
		return(False)
	def isEmpty(self, l):
		for e in l:
			if e != None:
				return(False)
		return(True)
	def scroll(self, o, v):
		velocity = v
		o.x -= velocity*1
	def generatePlatforms(self, n):
		for i in range(0, n):
			p = Platform(random.randint(820, 1500), random.randint(100, 500), self.settings)
			collidesAny = False
			for platform in self.platforms:
				if(p.get_rect().colliderect(platform.get_rect())):
					collidesAny = True
			while(collidesAny):
				collidesAny = False
				p = Platform(random.randint(820, 1500), random.randint(300, 500), self.settings)
				for platform in self.platforms:
					if(p.get_rect().colliderect(platform.get_rect())):
						collidesAny = True
			self.platforms.append(p)
			self.platformGroup.add(p)
			self.collidables.append(p)
	def generateEnemies(self, n):
		for i in range(0, n):
			self.enemies.append(Hollow(900, 1600, 0, 300, self.settings))
			self.hollowGroup.add(self.enemies[len(self.enemies)-1])
	def rectWidth(self, r):

		return(r.right-r.left)
	def rectHeight(self, r):

		return(r.bottom-r.top)
	def _check_events_main_screen(self):
		#check if the player is on ground
		#if not apply gravity

		if(self.onGround(self.player)):
			self.player.setGravity(False)
			if(self.player.yVelocity < 0):
				self.player.yVelocity = 0
		else:
			self.player.setGravity(True)

		#check if the enemies are on ground
		#apply gravity to all non grounded enemies
		for hollow in self.enemies:
			if(hollow == None):
				continue
			if(self.onGround(hollow)):
				hollow.setGravity(False)
				if(hollow.yVelocity < 0):
					hollow.yVelocity = 0
			else:
				hollow.setGravity(True)
		if(self.player.transforming):
			return
		for i in range(0, len(self.clouds)):
			if(self.clouds[i].x > 800):
				try:
					self.collidables.remove(self.clouds[i])
					self.cloudGroup.remove(self.clouds[i])
				except:
					None
				self.clouds[i] = Cloud(self.settings)
				if(self.clouds[i].velocity > 0):
					self.clouds[i].x = -200
				else:
					self.clouds[i].x = 1000
				self.cloudGroup.add(self.clouds[i])
		if(self.player.releaseGetsuga == 1):
			g = Getsuga(1, 0, self.player.x+60, self.player.get_rect().bottom-150, self.settings, self.player.form)
			self.getsugas.append(g)
			self.getsugaGroup.add(g)
			self.player.releaseGetsuga = 0
		elif(self.player.releaseGetsuga == 2):
			g = Getsuga(-1, 0, self.player.x, self.player.get_rect().bottom-150, self.settings, self.player.form)
			self.getsugas.append(g)
			self.getsugaGroup.add(g)
			self.player.releaseGetsuga = 0
		elif(self.player.releaseGetsuga == 3):
			g = Getsuga(0, 1, self.player.x, self.player.get_rect().bottom-170, self.settings, self.player.form)
			self.getsugas.append(g)
			self.getsugaGroup.add(g)
			self.player.releaseGetsuga = 0
		#update power rect
		self.powerRect = pygame.Rect(550, 10, self.player.power/1000 * 200, 25)
		#check if getsugas are out of range, is so delete them
		for i in range(0, len(self.getsugas)):
			if(self.getsugas[i] == None):
				continue
			if(self.getsugas[i].x > 820 or self.getsugas[i].x < -20 or self.getsugas[i].y < 0):
				self.getsugaGroup.remove(self.getsugas[i])
				self.getsugas[i] = None
		#clean up getsugas
		temp = self.getsugas
		self.getsugas = []
		for g in temp:
			if(g != None):
				self.getsugas.append(g)
		#check if all enemies are dead, if so create new enemies
		if(self.isEmpty(self.enemies)):
			for i in range(0, len(self.enemies)):
				self.enemies[i] = Hollow(0, 800, 0, 300, self.settings)
				self.hollowGroup.add(self.enemies[i])
		#is the player is dead, respawn it
		if(self.player.isDead):
			self.playerGroup.remove(self.player)
			self.player = Player()
			self.playerGroup.add(self.player)
		#check each enemy and remove dead ones
		for i in range(0, len(self.enemies)):
			if(self.enemies[i] == None):
				continue
			if(self.enemies[i].isDead):
				self.hollowGroup.remove(self.enemies[i])
				self.enemies[i] = None
		#check each alive enemy and check if player or enemy or neither should die
		#kill necessary units
		for hollow in self.enemies:
			if(hollow == None):
				continue
			if(hollow.currentAnimation.lower().find("death") >= 0):
				continue
			if(self.player.get_rect().colliderect(hollow.get_rect())):
				if(self.player.x < hollow.x and self.player.currentAnimation == "swingingRight"):
					hollow.animationFrame = -1
					if(hollow.currentAnimation.lower().find("left") >= 0):
						hollow.currentAnimation = "deathFacingLeft"
					elif(hollow.currentAnimation.lower().find("right") >= 0):
						hollow.currentAnimation = "deathFacingRight"
					self.player.power += 10
					self.player.kills += 1
				elif(self.player.x > hollow.x and self.player.currentAnimation == "swingingLeft"):
					hollow.animationFrame = -1
					if(hollow.currentAnimation.lower().find("left") >= 0):
						hollow.currentAnimation = "deathFacingLeft"
					elif(hollow.currentAnimation.lower().find("right") >= 0):
						hollow.currentAnimation = "deathFacingRight"
					self.player.power += 10
					self.player.kills += 1
				elif(self.player.y < hollow.get_rect().bottom and self.player.currentAnimation.lower().find("swingingup") >= 0):
					hollow.animationFrame = -1
					if(hollow.currentAnimation.lower().find("left") >= 0):
						hollow.currentAnimation = "deathFacingLeft"
					elif(hollow.currentAnimation.lower().find("right") >= 0):
						hollow.currentAnimation = "deathFacingRight"
					self.player.power += 10
					self.player.kills += 1
				else:
					None#here the player would typically die
			for getsuga in self.getsugas:
				if(getsuga == None):
					continue
				if(hollow.get_rect().colliderect(getsuga.get_rect())):
					hollow.animationFrame = -1
					if(hollow.currentAnimation.lower().find("left") >= 0):
						hollow.currentAnimation = "deathFacingLeft"
					elif(hollow.currentAnimation.lower().find("right") >= 0):
						hollow.currentAnimation = "deathFacingRight"
					self.player.power += 10
					self.player.kills += 1
		

		#check all events
		if(self.player.kills >= self.settings.vizardThreshold and self.player.form == 'base'):
			self.player.transformToVizard()
		elif(self.player.kills >= self.settings.vastoLordeThreshold and self.player.form == 'vizard'):
			self.player.transformToVastolorde()
		for event in pygame.event.get():
			#check if mouse is on the start button, if it is and clicked start the game
			#otherwise if only hovered over the start button, make it green
			#else revert it to normal
			if(self.startButton.get_rect().collidepoint(pygame.mouse.get_pos())):
				if(pygame.mouse.get_pressed()[0]):
					self.prepareGame()
				self.startButton.onHover()
			else:
				self.startButton.offHover()

			#check if mouse is on the quit button, if it is and clicked quit the game
			#otherwise if only hovered over the quit button, make it red
			#else revert it to normal
			if(self.quitButton.get_rect().collidepoint(pygame.mouse.get_pos())):
				if(pygame.mouse.get_pressed()[0]):
					pygame.quit()
					sys.exit()
				self.quitButton.onHover()
			else:
				self.quitButton.offHover()

			#if the game is quit, end pygame and program
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			#if a key is pressed
			elif event.type == pygame.KEYDOWN:
				#if return is pressed, start game
				if event.key == pygame.K_RETURN:
					self.settings.setScreen("game")
					self.prepareGame()
					return
				#if escape is pressed, quit game
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
				#if space is pressed and player is on ground, jump
				elif event.key == pygame.K_SPACE and self.onGround(self.player):
					self.player.jump()
		
		#get pressed keys
		self.keys = pygame.key.get_pressed()

		#uncancellable animation
		if(self.player.swinging or self.player.transforming):
			return


		#possibly update animation
		if (self.keys[pygame.K_UP] and self.keys[pygame.K_LSHIFT]):
			self.player.swinging = True
			if(self.player.currentAnimation.lower().find("left") >= 0):
				self.player.setAnimation("swingingUpFromLeft")
			elif(self.player.currentAnimation.lower().find("right") >= 0):
				self.player.setAnimation("swingingUpFromRight")
			self.player.animationFrame = -1
		elif self.keys[pygame.K_RIGHT] and self.keys[pygame.K_LSHIFT]:
			self.player.swinging = True
			self.player.setAnimation("swingingRight")
			#update swing animation to next one
			if(self.player.swingright == self.player.swingright1):
				self.player.swingright = self.player.swingright2
			elif(self.player.swingright == self.player.swingright2):
				self.player.swingright = self.player.swingright3
			elif(self.player.swingright == self.player.swingright3):
				self.player.swingright = self.player.swingright1
			self.player.animationFrame = -1

		elif (self.keys[pygame.K_LEFT] and self.keys[pygame.K_LSHIFT]):
			self.player.swinging = True
			self.player.setAnimation("swingingLeft")
			#update swing animation to next one
			if(self.player.swingleft == self.player.swingleft1):
				self.player.swingleft = self.player.swingleft2
			elif(self.player.swingleft == self.player.swingleft2):
				self.player.swingleft = self.player.swingleft3
			elif(self.player.swingleft == self.player.swingleft3):
				self.player.swingleft = self.player.swingleft1
			self.player.animationFrame = -1
		elif (self.keys[pygame.K_LEFT] and self.keys[pygame.K_LCTRL] and self.player.power >= 100):
			self.player.power -= 100
			self.player.swinging = True
			self.player.setAnimation("getsugaLeft")
			self.player.animationFrame = -1
			#create a getsuga in direction
		elif (self.keys[pygame.K_RIGHT] and self.keys[pygame.K_LCTRL] and self.player.power >= 100):
			self.player.power -= 100
			self.player.swinging = True
			self.player.setAnimation("getsugaRight")
			self.player.animationFrame = -1
		elif (self.keys[pygame.K_UP] and self.keys[pygame.K_LCTRL] and self.player.power >= 100):
			self.player.power -= 100
			self.player.swinging = True
			if(self.player.currentAnimation.lower().find("left") >= 0):
				self.player.setAnimation("getsugaUpFromLeft")
			elif(self.player.currentAnimation.lower().find("right") >= 0):
				self.player.setAnimation("getsugaUpFromRight")
			self.player.animationFrame = -1
		elif self.keys[pygame.K_RIGHT]:
			self.player.velocity = 1
			if(self.player.currentAnimation != "walkRight"):
				self.player.setAnimation("walkRight")
				self.player.animationFrame = -1
		elif self.keys[pygame.K_LEFT]:
			self.player.velocity = -1
			if(self.player.currentAnimation != "walkLeft"):
				self.player.setAnimation("walkLeft")
				self.player.animationFrame = -1
		elif self.keys[pygame.K_DOWN] and self.onGround(self.player) and self.player.get_rect().colliderect(self.ground.get_rect()) == False:
			self.player.get_rect().bottom += 10
		else:
			self.player.velocity = 0
			if(self.player.currentAnimation == "walkLeft" or self.player.currentAnimation == "swingingLeft" or self.player.currentAnimation == "swingingUpFromLeft"):
				self.player.setAnimation("standLeft")
				self.player.animationFrame = -1
			elif(self.player.currentAnimation == "walkRight" or self.player.currentAnimation == "swingingRight" or self.player.currentAnimation == "swingingUpFromRight"):
				self.player.setAnimation("standRight")
				self.player.animationFrame = -1
	def _check_events_game_screen(self):

		self.tick += 1
		#check if the player is on ground
		#if not apply gravity
		if(self.onGround(self.player)):
			self.player.setGravity(False)
			if(self.player.yVelocity < 0):
				self.player.yVelocity = 0
		else:
			self.player.setGravity(True)

		#check if the enemies are on ground
		#apply gravity to all non grounded enemies
		for hollow in self.enemies:
			if(hollow == None):
				continue
			if(self.onGround(hollow)):
				hollow.setGravity(False)
				if(hollow.yVelocity < 0):
					hollow.yVelocity = 0
			else:
				hollow.setGravity(True)


		for i in range(0, len(self.clouds)):
			if(self.clouds[i].x > 800):
				try:
					self.collidables.remove(self.clouds[i])
					self.cloudGroup.remove(self.clouds[i])
				except:
					None
				self.clouds[i] = Cloud(self.settings)
				if(self.clouds[i].velocity > 0):
					self.clouds[i].x = -200
				else:
					self.clouds[i].x = 1000
				self.cloudGroup.add(self.clouds[i])

		if(self.player.transforming):
			return

		#if the player is dead, update highscore and go back to menu
		if(self.settings.gameOver):
			if(self.tick%20 != 0):
				return
			if(self.gameEndCountDown == 0):
				self.settings.setScreen("main")
				self.settings.highscore = max(self.player.kills, self.settings.highscore)
				self.prepareMenu()
			else:
				if(self.gameEndCountDown%2 == 0):
					self.gameOverText = self.gameFont.render("GAME OVER", False, self.settings.red)
				else:
					self.gameOverText = self.gameFont.render("", False, self.settings.red)
				self.gameEndCountDown -= 1
			return
		if(self.player.isDead):
			self.settings.gameOver = True
			return
		if(self.player.currentAnimation.lower().find("death") >= 0):
			return
		self.level = self.player.kills//50

		if(self.player.releaseGetsuga == 1):
			g = Getsuga(1, 0, self.player.x, self.player.get_rect().bottom-150, self.settings, self.player.form)
			self.getsugas.append(g)
			self.getsugaGroup.add(g)
			self.player.releaseGetsuga = 0
		elif(self.player.releaseGetsuga == 2):
			g = Getsuga(-1, 0, self.player.x, self.player.get_rect().bottom-150, self.settings, self.player.form)
			self.getsugas.append(g)
			self.getsugaGroup.add(g)
			self.player.releaseGetsuga = 0
		elif(self.player.releaseGetsuga == 3):
			g = Getsuga(0, 1, self.player.x, self.player.get_rect().bottom-170, self.settings, self.player.form)
			self.getsugas.append(g)
			self.getsugaGroup.add(g)
			self.player.releaseGetsuga = 0

		if(self.ground1.x <= -1*self.ground1.get_image().get_width()):
			self.scrollspeed = 3 + self.level
			self.groundGroup.remove(self.ground1)
			self.groundGroup.remove(self.ground2)
			self.collidables.remove(self.ground1)
			self.collidables.remove(self.ground2)
			self.ground1 = self.ground2
			self.ground2 = Ground(self.ground1.get_image().get_width(), self.settings)
			self.groundGroup.add(self.ground1)
			self.groundGroup.add(self.ground2)
			self.collidables.append(self.ground1)
			self.collidables.append(self.ground2)
			self.generateEnemies(3 + self.level)
			self.generatePlatforms(random.randint(5, 10))
		self.scroll(self.player, self.scrollspeed)
		self.scroll(self.ground1, self.scrollspeed)
		self.scroll(self.ground2, self.scrollspeed)
		for e in self.enemies:
			if(e != None):
				self.scroll(e, self.scrollspeed)
		for p in self.platforms:
			if(p != None):
				self.scroll(p, self.scrollspeed)
		for g in self.getsugas:
			if(g != None and g.velocityY > 0):
				self.scroll(g, self.scrollspeed)
		#update power rect
		self.powerRect = pygame.Rect(550, 10, self.player.power/1000 * 200, 25)
		#check if getsugas are out of range, if so delete them
		for i in range(0, len(self.getsugas)):
			if(self.getsugas[i] == None):
				continue
			if(self.getsugas[i].x > 800 or self.getsugas[i].x < -20) or self.getsugas[i].y < 0:
				self.getsugaGroup.remove(self.getsugas[i])
				self.getsugas[i] = None
		#clean up getsugas
		temp = self.getsugas
		self.getsugas = []

		for g in temp:
			if(g != None):
				self.getsugas.append(g)

		#check if platforms are out of range, if so delete them
		for i in range(0, len(self.platforms)):
			if(self.platforms[i] == None):
				continue
			if(self.platforms[i].x < -120):
				self.platformGroup.remove(self.platforms[i])
				self.collidables.remove(self.platforms[i])
				self.platforms[i] = None

		#clean up platforms
		temp = self.platforms
		self.platforms = []
		for p in temp:
			if(p != None):
				self.platforms.append(p)
		#check each enemy and remove dead ones
		for i in range(0, len(self.enemies)):
			if(self.enemies[i] == None):
				continue
			if(self.enemies[i].isDead):
				self.hollowGroup.remove(self.enemies[i])
				self.enemies[i] = None
		#check each alive enemy and check if player or enemy or neither should die
		#kill necessary units
		for hollow in self.enemies:
			if(hollow == None):
				continue
			if(hollow.currentAnimation.lower().find("death") >= 0):
				continue
			if(self.player.get_rect().colliderect(hollow.get_rect())):
				if(self.player.x < hollow.x and (self.player.currentAnimation == "swingingRight" or self.player.currentAnimation == "getsugaRight")):
					hollow.animationFrame = -1
					if(hollow.currentAnimation.lower().find("left") >= 0):
						hollow.currentAnimation = "deathFacingLeft"
					elif(hollow.currentAnimation.lower().find("right") >= 0):
						hollow.currentAnimation = "deathFacingRight"
					self.player.power += 10
					self.player.kills += 1
				elif(self.player.get_rect().right > hollow.get_rect().right and (self.player.currentAnimation == "swingingLeft" or self.player.currentAnimation == "getsugaLeft")):
					hollow.animationFrame = -1
					if(hollow.currentAnimation.lower().find("left") >= 0):
						hollow.currentAnimation = "deathFacingLeft"
					elif(hollow.currentAnimation.lower().find("right") >= 0):
						hollow.currentAnimation = "deathFacingRight"
					self.player.power += 10
					self.player.kills += 1
				elif(self.player.y > hollow.y and (self.player.currentAnimation.lower().find("swingingup") >= 0 or self.player.currentAnimation.lower().find("getsugaup") >= 0)):
					hollow.animationFrame = -1
					if(hollow.currentAnimation.lower().find("left") >= 0):
						hollow.currentAnimation = "deathFacingLeft"
					elif(hollow.currentAnimation.lower().find("right") >= 0):
						hollow.currentAnimation = "deathFacingRight"
					self.player.power += 10
				elif(self.player.tick >= 180):
					#when checking for player death, use shrunken hitbox created below
					playerHitBox = pygame.Rect(self.player.get_rect().x, self.player.get_rect().y, 20, 20)
					
					playerHitBox.center = self.player.get_rect().center

					if(hollow.get_rect().colliderect(playerHitBox) == False):
						continue

					self.player.velocity = 0
					if(self.player.currentAnimation.lower().find("left") >= 0):
						self.player.animationFrame = -1
						self.player.currentAnimation = "deathFromLeft"
					elif(self.player.currentAnimation.lower().find("right") >= 0):
						self.player.animationFrame = -1
						self.player.currentAnimation = "deathFromRight"
					return
			for getsuga in self.getsugas:
				if(getsuga == None):
					continueself.swingleft3vizard.append(image)
				if(hollow.get_rect().colliderect(getsuga.get_rect())):
					hollow.animationFrame = -1
					if(hollow.currentAnimation.lower().find("left") >= 0):
						hollow.currentAnimation = "deathFacingLeft"
					elif(hollow.currentAnimation.lower().find("right") >= 0):
						hollow.currentAnimation = "deathFacingRight"
					self.player.power += 10
					self.player.kills += 1

		if(self.player.kills >= self.settings.vizardThreshold and self.player.form == 'base'):
			self.player.transformToVizard()
		elif(self.player.kills >= self.settings.vastoLordeThreshold and self.player.form == 'vizard'):
			self.player.transformToVastolorde()

		#check all events
		for event in pygame.event.get():

			#if the game is quit, end pygame and program
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			#if a key is pressed
			elif event.type == pygame.KEYDOWN:
				#if escape is pressed, go to menu
				if event.key == pygame.K_ESCAPE:
					self.settings.setScreen("main")
					self.settings.highscore = self.player.kills
					self.prepareMenu()
				#if space is pressed and player is on ground, jump
				elif event.key == pygame.K_SPACE and self.onGround(self.player):
					self.player.jump()
		
		#get pressed keys
		self.keys = pygame.key.get_pressed()

		#uncancellable animation
		if(self.player.swinging or self.player.transforming):
			return

		#possibly update animation
		if (self.keys[pygame.K_UP] and self.keys[pygame.K_LSHIFT]):
			self.player.swinging = True
			if(self.player.currentAnimation.lower().find("left") >= 0):
				self.player.setAnimation("swingingUpFromLeft")
			elif(self.player.currentAnimation.lower().find("right") >= 0):
				self.player.setAnimation("swingingUpFromRight")
			self.player.animationFrame = -1
		elif self.keys[pygame.K_RIGHT] and self.keys[pygame.K_LSHIFT]:
			self.player.swinging = True
			self.player.setAnimation("swingingRight")
			#update swing animation to next one
			if(self.player.swingright == self.player.swingright1):
				self.player.swingright = self.player.swingright2
			elif(self.player.swingright == self.player.swingright2):
				self.player.swingright = self.player.swingright3
			elif(self.player.swingright == self.player.swingright3):
				self.player.swingright = self.player.swingright1
			self.player.animationFrame = -1
		
		elif (self.keys[pygame.K_LEFT] and self.keys[pygame.K_LSHIFT]):
			self.player.swinging = True
			self.player.setAnimation("swingingLeft")
			#update swing animation to next one
			if(self.player.swingleft == self.player.swingleft1):
				self.player.swingleft = self.player.swingleft2
			elif(self.player.swingleft == self.player.swingleft2):
				self.player.swingleft = self.player.swingleft3
			elif(self.player.swingleft == self.player.swingleft3):
				self.player.swingleft = self.player.swingleft1
			self.player.animationFrame = -1
		elif (self.keys[pygame.K_LEFT] and self.keys[pygame.K_LCTRL] and self.player.power >= 100):
			self.player.power -= 100
			self.player.swinging = True
			self.player.setAnimation("getsugaLeft")
			self.player.animationFrame = -1
		elif (self.keys[pygame.K_RIGHT] and self.keys[pygame.K_LCTRL] and self.player.power >= 100):
			self.player.power -= 100
			self.player.swinging = True
			self.player.setAnimation("getsugaRight")
			self.player.animationFrame = -1
		elif (self.keys[pygame.K_UP] and self.keys[pygame.K_LCTRL] and self.player.power >= 100):
			self.player.power -= 100
			self.player.swinging = True
			if(self.player.currentAnimation.lower().find("left") >= 0):
				self.player.setAnimation("getsugaUpFromLeft")
			elif(self.player.currentAnimation.lower().find("right") >= 0):
				self.player.setAnimation("getsugaUpFromRight")
			self.player.animationFrame = -1
		elif self.keys[pygame.K_RIGHT]:
			self.player.velocity = 1
			if(self.player.currentAnimation != "walkRight"):
				self.player.setAnimation("walkRight")
				self.player.animationFrame = -1
		elif self.keys[pygame.K_LEFT]:
			self.player.velocity = -1
			if(self.player.currentAnimation != "walkLeft"):
				self.player.setAnimation("walkLeft")
				self.player.animationFrame = -1
		elif self.keys[pygame.K_DOWN] and self.onGround(self.player) and self.player.get_rect().colliderect(self.ground.get_rect()) == False:
			self.player.get_rect().bottom += 10
		else:
			self.player.velocity = 0
			if(self.player.currentAnimation == "walkLeft" or self.player.currentAnimation == "swingingLeft" or self.player.currentAnimation == "swingingUpFromLeft"):
				self.player.setAnimation("standLeft")
				self.player.animationFrame = -1
			elif(self.player.currentAnimation == "walkRight" or self.player.currentAnimation == "swingingRight" or self.player.currentAnimation == "swingingUpFromRight"):
				self.player.setAnimation("standRight")
				self.player.animationFrame = -1
	def _display_main_screen(self):
		self.menuLogoGroup.update()
		self.menuLogoGroup.draw(self.screen)
		#self.startButtonGroup.update()
		self.startButtonGroup.draw(self.screen)
		#self.quitButtonGroup.update()
		self.quitButtonGroup.draw(self.screen)
		self.cloudGroup.update()
		self.cloudGroup.draw(self.screen)
		self.getsugaGroup.update()
		self.getsugaGroup.draw(self.screen)


		self.groundGroup.draw(self.screen)
		self.screen.blit(self.highscoreText, (10, 10))
		self.screen.blit(self.highscoreTextVal, (10 + self.highscoreText.get_width(), 10))
		self.screen.blit(self.healthText, (10 , 50))
		self.screen.blit(self.healthTextVal, (10 + self.healthText.get_width(), 50))
		self.screen.blit(self.powerText, (550 - self.powerText.get_width() - 20, 10))

		if(self.player.power < 100):
			self.powerColor = self.settings.red
		else:
			self.powerColor = self.settings.blue
		pygame.draw.rect(self.screen, self.powerColor, self.powerRect)

		self.playerGroup.update()
		self.playerGroup.draw(self.screen)

		self.hollowGroup.update()
		self.hollowGroup.draw(self.screen)
	def _display_game_screen(self):

		self.scoreTextVal = self.gameFont.render(str(self.player.kills), False, self.settings.white)
		self.healthTextVal = self.gameFont.render(str(self.player.health), False, self.settings.green)

		self.cloudGroup.update()
		self.cloudGroup.draw(self.screen)

		self.screen.blit(self.healthText, (10 , 50))
		self.screen.blit(self.healthTextVal, ((10 + self.healthText.get_width(), 50)))

		self.groundGroup.update()
		self.groundGroup.draw(self.screen)
		self.screen.blit(self.scoreText, (10, 10))
		self.screen.blit(self.scoreTextVal, (10 + self.scoreText.get_width(), 10))
		self.screen.blit(self.powerText, (550 - self.powerText.get_width() - 20, 10))

		if(self.player.power < 100):
			self.powerColor = self.settings.red
		else:
			self.powerColor = self.settings.blue
		pygame.draw.rect(self.screen, self.powerColor, self.powerRect)


		self.platformGroup.update()
		self.platformGroup.draw(self.screen)

		self.playerGroup.update()
		self.playerGroup.draw(self.screen)

		self.hollowGroup.update()
		self.hollowGroup.draw(self.screen)

		self.getsugaGroup.update()
		self.getsugaGroup.draw(self.screen)

		self.screen.blit(self.scoreText, (10, 10))
		self.screen.blit(self.scoreTextVal, (10 + self.scoreText.get_width(), 10))
		self.screen.blit(self.powerText, (550 - self.powerText.get_width() - 20, 10))
		self.screen.blit(self.gameOverText, ((self.settings.screen_width-self.gameOverText.get_width())//2, (self.settings.screen_height-self.gameOverText.get_height())//2))
	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		if(self.settings.screen == "main"):
			pygame.display.set_caption("PyPlatformer-Home")
			self._display_main_screen()
		elif(self.settings.screen == "game"):
			pygame.display.set_caption("PyPlatformer-Game")
			self._display_game_screen()
		pygame.display.flip()

if __name__ == '__main__':
	game = Platformer()
	game.run_game()