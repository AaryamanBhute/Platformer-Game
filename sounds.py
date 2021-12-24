import os
import pygame

class Sounds:
	def __init__(self):
		#pygame.mixer.Sound()

		self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mediafiles', 'sounds')

		self.hollowDeath = pygame.mixer.Sound(pygame.mixer.Sound(os.path.join(self.path, 'hollowdeath.wav')))

		self.walk = pygame.mixer.Sound(os.path.join(self.path, 'walk.wav'))
		self.walk.set_volume(1)

		self.swing1 = pygame.mixer.Sound(os.path.join(self.path, 'swing1.wav'))
		self.swing1.set_volume(0.1)
		self.swing2 = pygame.mixer.Sound(os.path.join(self.path, 'swing2.wav'))
		self.swing2.set_volume(0.1)
		self.swing3 = pygame.mixer.Sound(os.path.join(self.path, 'swing3.wav'))
		self.swing3.set_volume(0.1)

		self.getsuga = pygame.mixer.Sound(os.path.join(self.path, 'getsuga.wav'))

		self.cero = pygame.mixer.Sound(os.path.join(self.path, 'cero.wav'))

		self.baseDeath = pygame.mixer.Sound(os.path.join(self.path, 'basedeath.wav'))

		self.baseToVizard = pygame.mixer.Sound(os.path.join(self.path, 'toVizard.wav'))

		self.vizardDeath = pygame.mixer.Sound(os.path.join(self.path, 'vizarddeath.wav'))

		self.vizardToVastolorde = pygame.mixer.Sound(os.path.join(self.path, 'toVastolorde.wav'))

		self.vastolordeDeath = pygame.mixer.Sound(os.path.join(self.path, 'vastolordedeath.wav'))

		self.damageTaken = pygame.mixer.Sound(os.path.join(self.path, 'damagetaken.wav'))

		self.baseaudio = pygame.mixer.Sound(os.path.join(self.path, 'baseaudio.wav'))
		self.baseaudio.set_volume(0.1)
		self.vizardaudio = pygame.mixer.Sound(os.path.join(self.path, 'vizardaudio.wav'))
		self.vizardaudio.set_volume(0.1)
		self.vastolordeaudio = pygame.mixer.Sound(os.path.join(self.path, 'vastolordeaudio.wav'))
		self.vastolordeaudio.set_volume(0.1)

		self.menuaudio = pygame.mixer.Sound(os.path.join(self.path, 'menuaudio.wav'))
		self.menuaudio.set_volume(0.1)