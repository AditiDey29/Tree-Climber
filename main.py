#I have copied most of the code including all the function definitions and the pygame concepts from a youtube video. LINK:https://youtu.be/-8n91btt5d8
#Background Image: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.1zoom.me%2Fen%2Fwallpaper%2F521300%2Fz12982.8%2F600x800&psig=AOvVaw3nNUocjoskwev9H_7dZZz6&ust=1608773930652000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKC2vYf84u0CFQAAAAAdAAAAABAD.jpg
import pygame
import random
import sys

pygame.init()
background = pygame.image.load('forestfinal.jpg')
pygame.display.set_caption('Tree Climber')

#defining various variables
WIDTH = 600
HEIGHT = 600

BLUE = (0,0,255)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (0,0,0)
BLACK = (0,0,0)

player_size = 50
player_pos = [200, HEIGHT-250]

enemy_size = 50
enemy_pos = [random.choice([0,200,400,550]), 0]
enemy_list = [enemy_pos]

SPEED = 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))

score = 0
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("hack", 35)

#creating multiple enemies
def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, YELLOW, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 3 and delay < 0.06:
		x_pos = random.choice([0,200,400,550])
		y_pos = 0
		enemy_list.append([x_pos, y_pos])
def update_enemy_positions(enemy_list, score):
	for enemy_pos in (enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED
		else:
			enemy_list.remove(enemy_pos)
			score += 1
	return score

#making the speed proportional to score
def set_level(score, SPEED):
	SPEED = score + 5
	return SPEED

#checking collision
def detect_collision(player_pos, enemy_pos):
	px = player_pos[0]
	py = player_pos[1]
	ex = enemy_pos[0]
	ey = enemy_pos[1]
	if (ex >= px and ex < (px + player_size)) or (px >= ex and px < (ex+enemy_size)):
		if (ey >= py and ey < (py + player_size)) or (py >= ey and py < (ey+enemy_size)):
			return True
	return False

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

game_over = False
while not game_over:

	screen.fill(BACKGROUND_COLOR)
	screen.blit(background, (0,0))

	#the main loop for the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT and x>=200:
				x -= 200
			if event.key == pygame.K_LEFT and x == 200:
				x-=180
			elif event.key == pygame.K_RIGHT and x<=400:
				x += 200
			elif event.key == pygame.K_RIGHT and x == 400:
				x+=130

			player_pos = [x,y]

	#calling all the fuctions
	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	SPEED = set_level(score, SPEED)

	text = "Score:" + str(score)
	label = myFont.render(text, 1, YELLOW,[0,0,0])
	screen.blit(label, (WIDTH-200, HEIGHT-40))

	if collision_check(enemy_list, player_pos):
		game_over=True
		break
	draw_enemies(enemy_list)
	pygame.draw.circle(screen, BLUE, (player_pos[0], player_pos[1]), (player_size)/2)
	clock.tick(30)
	pygame.display.update()
