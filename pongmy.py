import pygame
import sys
from degrees_to_velocity import degrees_to_velocity
import random

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



def player_to_center():
	player_1.x = screen_width * 0.1
	player_1.y = screen_height // 2 - player_1_height // 2
	player_2.x = screen_width * 0.9 - player_2_width
	player_2.y = screen_height // 2 - player_2_height // 2


player_x = 800
player_y = 0
player_color_1 = WHITE
player_color_2 = WHITE
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen_color = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN) # экран
pygame.display.set_caption("Моя программа")

player_1_width = 20
player_1_height = 150
player_1_score = 0
player_1 = pygame.Rect((0, 0, player_1_width, player_1_height))
player1_y_prav = player_1.y
player_1_speed = 8
player_2_width = 20
player_2_height = 150
player_2_score = 0
player_2 = pygame.Rect((0, 0, player_2_width, player_2_height))
player2_y_prav = player_2.y
player_2_speed = 8


player_to_center()


def ball_to_center():
	ball.x = screen_width // 2 - ball_width // 2
	ball.y = screen_height // 2 - ball_height // 2
def rotate_ball():
	if random.randint(0, 1) == 0:
	    direction = random.randint(225, 315)
	else:
	    direction = random.randint(90, 135) 
	velocity = degrees_to_velocity(direction, 7)
	return (velocity[0], velocity[1], direction)

ball_width = 15
ball_height = 15
velocity = rotate_ball()
ball_speed_x = velocity[0]
ball_speed_y = velocity[1]
ball_direction = velocity[2]



ball = pygame.Rect((0, 0, ball_height, ball_width))
ball_to_center()
clock = pygame.time.Clock()


score_right = pygame.font.Font(None, 60)
score_left = pygame.font.Font(None, 60)

game = True
while game: # главный цикл
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        pygame.quit()
	        sys.exit()

	    if event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_ESCAPE:
	            pygame.quit()
	            sys.exit()

	keys = pygame.key.get_pressed()
	"""
	if keys[pygame.K_UP]:
	    player_2.y -= player_1_speed
	    if player_2.y < 0:
	        player_2.y = 0
	if keys[pygame.K_DOWN]:
	    player_2.y += player_1_speed
	    if player_2.y > screen_height - player_2_height:
	        player_2.y = screen_height - player_2_height
	"""
	if keys[pygame.K_w]:
	    player_1.y -= player_2_speed
	    if player_1.y < 0:
	        player_1.y = 0
	if keys[pygame.K_s]:
	    player_1.y += player_2_speed
	    if player_1.y > screen_height - player_1_height:
	        player_1.y = screen_height - player_1_height

	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if player_1.y > player1_y_prav:
		print("еду вниз")
	elif player_1.y < player1_y_prav:
		print("еду вверх")
	player1_y_prav = player_1.y

	if ball.x < 0:
	    player_2_score += 1
	    ball_to_center()
	    velocity = rotate_ball()
	    ball_speed_x = velocity[0]
	    ball_speed_y = velocity[1]

	if ball.x > screen_width - ball_width:
	    player_1_score += 1
	    ball_to_center()
	    velocity = rotate_ball()
	    ball_speed_x = velocity[0]
	    ball_speed_y = velocity[1]  

	if ball.y < 0:
	    ball_speed_y *= -1
	if ball.y > screen_height - ball_height:
	    ball_speed_y *= -1

	if ball.colliderect(player_1) or ball.colliderect(player_2):
	    ball_speed_x *= -1
	    
	    ball.x += ball_speed_x
	    ball.y += ball_speed_y

	if ball.centery < player_2.centery:
	    player_2.y -= player_2_speed

	if ball.centery > player_2.centery:
	    player_2.y += player_2_speed


	# отрисовка
	screen.fill(screen_color)                                               
	pygame.draw.rect(screen, WHITE, player_1)
	pygame.draw.rect(screen, WHITE, player_2)
	pygame.draw.rect(screen, WHITE, ball)
	score_left_img = score_left.render(str(player_1_score), True, WHITE)
	score_right_img = score_right.render(str(player_2_score), True, WHITE)
	screen.blit(score_left_img, (screen_width * 0.25, 20))
	screen.blit(score_right_img, (screen_width * 0.75, 20))
	line = pygame.draw.line(
	    screen,
	    WHITE, 
	    [screen_width // 2, 0], 
	    [screen_width // 2, screen_height],
	    5)

	pygame.display.flip()

clock.tick(100)
