import pygame

pygame.init()

#화면 크기 설정
screen_width = 480
screen_hight = 640
screen = pygame.display.set_mode((screen_width, screen_hight))

pygame.display.set_caption("Game")

running = True
while running:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #프로그램 종료

pygame.quit()