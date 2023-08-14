import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - Tricks.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smb_coin.wav')

largura = 640
altura = 480

x_snake = int(largura / 2)
y_snake = int(altura / 2)

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont("Arial", 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
clock = pygame.time.Clock()

lista_snake = []
comprimento_inicial = 5
morreu = False

def increase_snake(lista_snake):
    for XeY in lista_snake:
       pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))
       
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_snake, y_snake, lista_snake, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_snake = int(largura / 2)
    y_snake = int(altura / 2)
    lista_snake = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

while True:
    clock.tick(20)
    tela.fill((0, 0, 0))
    
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
                
            if event.key == K_d or event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
                
            if event.key == K_w or event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
                                
            if event.key == K_s or event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
                
    x_snake += x_controle
    y_snake += y_controle
              
    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    
    if snake.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial += 1
        
    lista_cabeca = []
    lista_cabeca.append(x_snake)
    lista_cabeca.append(y_snake)
    
    lista_snake.append(lista_cabeca)
    
    if lista_snake.count(lista_cabeca) > 1:
        font2 = pygame.font.SysFont('Arial', 20, True, True)
        mensagem = "Game Over! Pressione a tecla R para reicinicar o jogo"
        texto_formatado = font2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        
        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()
            
    if x_snake > largura:
        x_snake = 0
    if x_snake < 0:
        x_snake = largura
    if y_snake > altura:
        y_snake = 0
    if y_snake < 0:
        y_snake = altura
    
    if len(lista_snake) > comprimento_inicial:
        del lista_snake[0]
        
    increase_snake(lista_snake)
        
    tela.blit(texto_formatado, (450, 40))
    
    pygame.display.update()