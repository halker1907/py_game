import pygame 
import sys


pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#экран
screen_width = 800 #ширина экрана в пикселях
screen_height = 600 #высота экрана в пикселях
screen_color = (255, 250, 240) #цвет экрана
screen = pygame.display.set_mode((screen_width, screen_height)) #экран
pygame.display.set_caption("magic")


#игрок 1 
player_one_width = 10
player_one_height = 50
player_one_x = 50
player_one_y = screen_height // 2 - player_one_height // 2
player_one = pygame.Rect(player_one_x, player_one_y, player_one_width, player_one_height) # x, y, ширина, высота

#игрок 2
player_two_width = 10
player_two_height = 50
player_two_x = screen_width - player_one_x
player_two_y = screen_height // 2 - player_two_height // 2
player_two = pygame.Rect(player_two_x, player_two_y, player_two_width, player_two_height)

#мяч
ball_width = 10
ball_height = 10
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_height // 2
ball = pygame.Rect(ball_x, ball_y, ball_width, ball_height) 

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
	if keys[pygame.K_w]:
		player_one.y -= 1
		if player_one.y < 0:
			player_one.y = 0

	if keys[pygame.K_UP]:
		player_two.y -= 1
		if player_two.y < 0:
			player_two.y = 0

	if keys[pygame.K_s]:
		player_one.y += 1
		if player_one.y > screen_height - player_one_height:
			player_one.y = screen_height - player_one_height

	if keys[pygame.K_DOWN]:
		player_two.y += 1
		if player_two.y > screen_height - player_two_height:
			player_two.y = screen_height - player_two_height

	ball.x += 1
	ball.y += 1
	if ball.y > screen_height - ball_height:
		ball.y = screen_height - ball_height

	#отрисовка
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, player_one) #рисуем игрока
	pygame.draw.rect(screen, WHITE, player_two) #рисуем игрока
	pygame.draw.rect(screen, WHITE, ball) 	
	pygame.display.flip() #обновляем экран