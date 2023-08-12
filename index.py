import pygame
from pygame.locals import *
from sys import exit

pygame.init()

clock = pygame.time.Clock()

largura = 640
altura = 480

x = largura / 2
y = altura / 2

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")

while True:
    clock.tick(300)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        # if event.type == KEYDOWN:
        #     if event.key == K_a or event.key == K_LEFT:
        #         x -= 20    
                
        #     if event.key == K_d or event.key == K_RIGHT:
        #         x += 20
                
        #     if event.key == K_w or event.key == K_UP:
        #         y -= 20
                
        #     if event.key == K_s or event.key == K_DOWN:
        #         y += 20
        
        if pygame.key.get_pressed()[K_a]:
            x -= 20
        if pygame.key.get_pressed()[K_d]:
            x += 20
        if pygame.key.get_pressed()[K_w]:
            y -= 20
        if pygame.key.get_pressed()[K_s]:
            y += 20
              
    pygame.draw.rect(tela, (225, 0, 0), (x, y, 40, 50))
    pygame.display.update()