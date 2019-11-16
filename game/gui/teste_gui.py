import pygame

initial_x = initial_y = 50
size_square = 500
end_x = initial_x + size_square
end_y = initial_y + size_square
parts = 10
part = size_square//parts
white = (200,200,200)

pygame.init()
WIDTH = initial_x + size_square + 100
HEIGHT = initial_y + size_square + 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('GeeksForGeeks', True, (255,255,255), (0,0,0))
textRect = text.get_rect()
textRect.center = (WIDTH // 2, 25)  

imgs = [pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/monster.png'), pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/monster.png')]
imgs = [pygame.transform.scale(img, (part-1,part-1)) for img in imgs]
img_x = initial_x + (part * 3)
img_y = end_y - (part * 2) - part

speed_down_img = pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/speed.png')
speed_down_img = pygame.transform.scale(speed_down_img, (part-1,part-1))

speed_up_img = pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/speed.png')
speed_up_img = pygame.transform.rotate(speed_up_img,180)
speed_up_img = pygame.transform.scale( speed_up_img, (part-1,part-1))

current_img = 0

clock = pygame.time.Clock()

while True:
    screen.fill((50,150,50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN: img_y = (img_y + part) if (img_y + part) < end_y else img_y
            if event.key == pygame.K_RIGHT: img_x = (img_x + part) if (img_x + part) < end_x else img_x
            if event.key == pygame.K_LEFT: img_x = (img_x - part) if (img_x - part) >= initial_x else img_x
            if event.key == pygame.K_UP: img_y = (img_y - part) if (img_y - part) >= initial_y else img_y


        

    pygame.draw.line(screen, white, (initial_x, initial_y), (initial_x , end_y), 2)
    pygame.draw.line(screen, white, (initial_x, initial_y), (end_x, initial_y), 2)

    for i in range(parts):
        pygame.draw.line(screen, white, (initial_x, initial_y  + (part * (i+1))),  (end_x,  initial_y  + (part * (i+1))), 4)

    for i in range(parts):
        pygame.draw.line(screen, white, (initial_x  + (part * (i+1)), initial_y),  (initial_x  + (part * (i+1)), end_y), 2)

    screen.blit(imgs[current_img], (img_x, img_y))
    screen.blit(text, textRect) 
    screen.blit(speed_up_img, (WIDTH-50, 25)) 
    screen.blit(speed_down_img, (WIDTH-100, 25)) 
    current_img = 0 if current_img == 1 else 1
    pygame.display.update()
    clock.tick(10)