import pygame 
from degrees_to_velocity import degrees_to_velocity
import sys
from random import randint


pygame.init()

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
#экран
screen_width = 800 #ширина экрана в пикселях
screen_height = 600 #высота экрана в пикселях
screen_color = (255, 250, 240) #цвет экрана
screen = pygame.display.set_mode((screen_width, screen_height)) #экран
pygame.display.set_caption("magic")


#игрок 1 
player_one_width = 15
player_one_height = 70
player_one_x = 50
player_one_y = screen_height // 2 - player_one_height // 2
player_one_score = 0
p1_speed = 10
player_one = pygame.Rect(player_one_x, player_one_y, player_one_width, player_one_height) # x, y, ширина, высота


#игрок 2
player_two_width = 15
player_two_height = 70
player_two_x = screen_width - player_one_x
player_two_y = screen_height // 2 - player_two_height // 2
player_two_score = 0
p2_speed = 10
player_two = pygame.Rect(player_two_x, player_two_y, player_two_width, player_two_height)

#мяч
ball_width = 10
ball_height = 10
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_height // 2
velocity = degrees_to_velocity(45, 10)
ball_speed_x = velocity[0]
ball_speed_y = velocity[1]
ball = pygame.Rect(ball_x, ball_y, ball_width, ball_height)


#табло
score_left = pygame.font.Font(None, 60)
score_right = pygame.font.Font(None, 60)


#сбрасывает мач 
def ball_to_center():
	ball.x = ball_x
	ball.y = ball_y
	if random.randint(0, 1) == 0: 
		velocity = degrees_to_velocity(random.randint(45, 135), 10)
	else:
		velocity = degrees_to_velocity(random.randint(215, 305), 10)
		ball_speed_x = velocity[0]
		ball_speed_y = velocity[1]


while True: #гл. цикл
	#события
	for event in pygame.event.get(): #собираем события
		if event.type == pygame.QUIT: #обработка события
			pygame.quit() #выгрузили модули pygame из памяти
			sys.exit() #закрыли программу
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: #нажатая клавиша
				pygame.quit()
				sys.exit()



	keys = pygame.key.get_pressed()

	#клавиши вверх
	if keys[pygame.K_w]:
		player_one.y -= p1_speed
		if player_one.y < 0:
			player_one.y = 0

	if keys[pygame.K_UP]:
		player_two.y -= p2_speed
		if player_two.y < 0:
			player_two.y = 0

	#клавиши вниз
	if keys[pygame.K_s]:
		player_one.y += p1_speed
		if player_one.y > screen_height - player_one_height:
			player_one.y = screen_height - player_one_height

	if keys[pygame.K_DOWN]:
		player_two.y += p2_speed
		if player_two.y > screen_height - player_two_height:
			player_two.y = screen_height - player_two_height

	#секретные клавиши (не пользоваться!)
	if keys[pygame.K_u]:
		ball.y -= 5
		if ball.y < 0:
			ball.y = 0
	
	if keys[pygame.K_j]:
		ball.y += 5
		if ball.y > screen_height - ball_height:
			ball.y = screen_height - ball_height

	if keys[pygame.K_h]:
		ball.x -= 5

	if keys[pygame.K_k]:
		ball.x += 5


	#логика
	ball.x += ball_speed_x #мяч всегда движется со скоростью
	ball.y += ball_speed_y

	if ball.x < 0:
		player_two_score += 1
		ball_to_center()

	if ball.x > screen_width - ball_width:
		player_one_score += 1
		ball_to_center()

	if ball.y < 0:
		ball_speed_y *= -1
	if ball.y > screen_height - ball_height:
		ball_speed_y *= -1

	#отскок от ракетки

	if ball.colliderect(player_one) or ball.colliderect(player_two):
		ball_speed_x *= -1



	#отрисовка
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, player_one) #рисуем игрока
	pygame.draw.rect(screen, WHITE, player_two) #рисуем игрока
	pygame.draw.rect(screen, WHITE, ball) 
	score_left_img = score_left.render(str(player_one_score), True, WHITE,)
	score_right_img = score_right.render(str(player_two_score), True, WHITE,)
	screen.blit(score_left_img, (screen_width * 0.25, 20))	
	screen.blit(score_right_img, (screen_width * 0.75 - 0.25, 20))
	band = pygame.draw.line(screen, WHITE, [screen_width // 2, 30], [screen_width // 2, screen_height], 5)

	pygame.display.flip() #обновляем экран

	clock.tick(FPS)