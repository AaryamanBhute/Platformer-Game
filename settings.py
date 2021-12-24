class Settings:
	def __init__(self):
		self.fps = 60
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (105,105,105)
		self.darkblue = (0, 0, 100)
		self.black = (0, 0, 0)
		self.blue = (0, 0, 255)
		self.green = (0, 255, 0)
		self.white = (255, 255, 255)
		self.purple = (153,50,204)
		self.red = (255, 0, 0)
		self.screen = "main"
		self.highscore = 0
		self.gameOver = False
		self.vizardThreshold = 50
		self.vastoLordeThreshold = 100
	def setScreen(self, s):
		self.screen = s
	def setHighScore(self, n):
		self.highscore = n