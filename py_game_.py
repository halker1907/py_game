import pygame 
import sys

pygame.init()

#экран
screen_width = 8000 #ширина экрана в пикселях
screen_height = 6000 #высота экрана в пикселях
screen = pygame.display.set_mode((screen_width, screen_height)) #экран
pygame.display.set_caption("magic")

#игрок
player_color = (255, 0, 0) #RGB
player_width = 60
player_height = 70
player_x = screen_width // 2 - player_width // 2
player_y = screen_height // 2 - player_height // 2
player = pygame.Rect((player_x, player_y, player_width, player_height)) # x, y, ширина, высота


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
	if keys[pygame.K_UP]:
		player.y -= 10
		player_color = (2, 45, 34)
	if keys[pygame.K_DOWN]:
		player.y += 10
		player_color = (64, 4, 37)
	if keys[pygame.K_LEFT]:
		player.x -= 10
		player_color = (65, 77, 10)
	if keys[pygame.K_RIGHT]:
		player.x += 10
		player_color = (65, 77, 10)

	#отрисовка
	screen.fill((0, 0, 0))
	pygame.draw.rect(screen, player_color, player) #рисуем игрока
	pygame.display.flip() #обновляем экран
