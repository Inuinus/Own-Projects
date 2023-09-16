import pygame

#initialize pygame
pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

x = 1
y = 1
rectangle_size = 50

#game variables
game_paused = False

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x ,y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#visuals
player = pygame.Rect((x,y,rectangle_size,rectangle_size))

#While run is true the screen will always be running, until USER says EXIT
#e.g Game Loop
run = True
while run:
    screen.fill((52, 78, 91))

    #check if game is paused
    if game_paused == True:
        pass
        #display menu
        pygame.draw.rect(screen, (255,100,100), player)
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            player.move_ip(-1, 0)
        if key[pygame.K_d] == True:
            player.move_ip(1, 0)
        if key[pygame.K_s] == True:
            player.move_ip(0, 1)
        if key[pygame.K_w] == True:
            player.move_ip(0, -1)
    else:
        draw_text("Press SPACE to pause", font , TEXT_COL, 150, 250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()