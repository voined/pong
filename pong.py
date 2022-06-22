import pygame
pygame.init()

pygame.display.set_caption('Pong')

screen_width = 750
screen_height = 600

bg_color = (0,0,0)
player1color = (255,255,255)
player2color = (255,255,255)
ballcolor = (255,255,255)

win = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()



class player1(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.vel = 12


	def display(self):
		self.move()
		pygame.draw.rect(win, player1color, (self.x, self.y, self.width, self.height))


	def move(self):
		KEYS = pygame.key.get_pressed()
		if KEYS[pygame.K_w] and self.y >= 0:
			self.y -= self.vel
		elif KEYS[pygame.K_s] and self.y + self.height <= screen_height:
			self.y += self.vel





class ai(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.vel = 7

	def display(self):
		self.move()
		pygame.draw.rect(win, player2color, (self.x, self.y, self.width, self.height))


	def move(self):
		if self.y + self.height/2 >= ball_.y + ball_.radius:
			self.y -= self.vel
		elif self.y + self.height/2 <= ball_.y - ball_.radius:
			self.y += self.vel
		









class ball(object):
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius

		self.acceleration = 0.5

		self.xvel = -7
		self.yvel = 7

	def display(self):
		self.move()
		pygame.draw.circle(win, ballcolor, (self.x, self.y), self.radius)


	def move(self):
		if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
			self.yvel *= -1

		if self.x - self.radius <= player_1.x + player_1.width and self.y + self.radius >= player_1.y and self.y - self.radius <= player_1.y + player_1.height:
			self.xvel *= -1
			self.xvel += self.acceleration
			if self.yvel > 0:
				self.yvel += self.acceleration
			else:
				self.yvel -= self.acceleration


		elif self.x + self.radius >= ai_.x and self.y + self.radius >= ai_.y and self.y - self.radius <= ai_.y + ai_.height:
			self.xvel *= -1
			self.xvel -= self.acceleration
			if self.yvel > 0:
				self.yvel += self.acceleration
			else:
				self.yvel -= self.acceleration



		if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
			self.x = screen_width/2
			self.y = screen_height/2
			self.xvel = -7
			self.yvel = 7





		self.y += self.yvel
		self.x += self.xvel











ai_ = ai(screen_width-15, screen_height/2, 15, 80)
player_1 = player1(0, screen_height/2, 15, 80)
ball_ = ball(screen_width/2, screen_height/2, 9)
def refreshwindow():
	pygame.draw.rect(win, bg_color, (0, 0, screen_width, screen_height))

	pygame.draw.line(win, (220,220,220), (screen_width/2, 0), (screen_width/2, screen_height))


	player_1.display()
	ball_.display()
	ai_.display()

	pygame.display.update()




run = True
while run:

	clock.tick(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	refreshwindow()




pygame.quit()