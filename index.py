import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")

while True:
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    pygame.draw.rect(tela, (225, 0, 0), (200, 300, 40, 50))
    pygame.draw.circle(tela, (134, 233, 45), (300, 260), 40)
    pygame.draw.line(tela, (244, 120, 140), (390, 0), (390, 600), 5)
    pygame.display.update()