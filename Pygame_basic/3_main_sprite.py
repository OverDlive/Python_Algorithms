import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_hight = 640
screen = pygame.display.set_mode((screen_width, screen_hight)) # 게임 이름

background = pygame.image.load("/Users/donghyeok/Documents/Programming/파이썬/Pygame_basic/background.png")

#캐릭터 불러오기
character = pygame.image.load("/Users/donghyeok/Documents/Programming/파이썬/Pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_hgith = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_hight - character_hgith #화면 세로 크기 가장 아래에 해당하는 곷에 위치

pygame.display.set_caption("Game")

# 이벤트 목표
running = True# 게임이 진행중인가?
while running:
    for event in  pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    screen.blit(background, (0, 0)) #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() #게임화면을 다시 그리기

pygame.quit() # pygame 종료