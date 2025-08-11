import pygame
from sys import exit

pygame.init()

#define screen size
screen = pygame.display.set_mode((800,400))

#give game name pass string
pygame.display.set_caption("Haha")
#control timing
clock = pygame.time.Clock()
#create regular surface
#surface1 =  pygame.Surface((100,200))
#surface1.fill('Blue')
surface1 = pygame.image.load('Assets/ground.png').convert()
surface2 = pygame.image.load('Assets/Sky.png').convert()

text = pygame.font.Font('Assets/Blazeberg.otf', 30)
textsurf = text.render('Score', False, 'Black')
textrect = textsurf.get_rect(center = (350,50))


enemy = pygame.image.load('Assets/snail1.png').convert_alpha()
enemyrect = enemy.get_rect(midbottom = (700,300))
#enemymov = pygame.image.load('Assets/snail2.png').convert_alpha()

enemy1 = pygame.image.load('Assets/Fly1.png').convert_alpha()
enemy1rect = enemy1.get_rect(midtop = (700, 150))
#enemy1mov = pygame.image.load('Assets/Fly2.png').convert_alpha()

hero = pygame.image.load('Assets/playerwalk1.png').convert_alpha()
herorect = hero.get_rect(midbottom = (80,300))

enemyxpos = 750

while True:
    #draw elements and update everything

    #event loop to check player inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(surface2,(0,0))
    screen.blit(surface1,(0,300))

    screen.blit(textsurf,textrect)

    #enemy dynamics
    screen.blit(enemy,enemyrect)
    enemyrect.left -= 4
    if enemyrect.right < 0: enemyrect.left = 800

    screen.blit(enemy1,enemy1rect)
    enemy1rect.left -= 2
    if enemy1rect.right < 0: enemy1rect.left = 800

    #hero dynamics
    herorect.left += 1
    if herorect.right > 800: herorect.left = 0
    screen.blit(hero,herorect)

    #update display contents
    pygame.display.update()
    #max frame rate
    clock.tick(60)

    #collision check
    #if herorect.colliderect(enemyrect): print("coll")

    mouse1 = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if mouse1[0]:
        herorect.top = 150
    else:
        herorect.bottom = 300

    

