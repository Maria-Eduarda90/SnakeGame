import pygame
from pygame.locals import *
from sys import exit

pygame.init()

clock = pygame.time.Clock()

largura = 640
altura = 480

x = largura / 2
y = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")

while True:
    clock.tick(300)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    if y >= altura:
        y = 0
            
    y += 1
    pygame.draw.rect(tela, (225, 0, 0), (x, y, 40, 50))
    pygame.display.update()