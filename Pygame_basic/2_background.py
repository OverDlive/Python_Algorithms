import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_hight = 640
screen = pygame.display.set_mode((screen_width, screen_hight)) # 게임 이름

background = pygame.image.load("/Users/donghyeok/Documents/Programming/파이썬/Pygame_basic/background.png")

pygame.display.set_caption("Game")

# 이벤트 목표
running = True# 게임이 진행중인가?
while running:
    for event in  pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    screen.blit(background, (0, 0)) #배경 그리기
    pygame.display.update() #게임화면을 다시 그리기

pygame.quit() # pygame 종료