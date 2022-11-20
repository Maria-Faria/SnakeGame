import pygame

from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')

xSnake = largura/2
ySnake = altura/2

xControle = 10
yControle = 0

xApple = randint(40, 600)
yApple = randint(50, 430)

pontos = 0

fonte = pygame.font.SysFont('lucidasans', 30, False, False)
relogio = pygame.time.Clock()
controle = False
corpo = []
comprimentoIni = 3
flag = False
flagLeft = False
flagRight = False
flagUp = False
flagDown = False

def crescer(corpo):
    for XeY in corpo:
        if flag:
            corpinho = pygame.draw.rect(tela, (75, 0, 130), (XeY[0], XeY[1], 30, 30))

while True:
    relogio.tick(20)
    tela.fill((34, 139, 34))

    mensagem = f'Pontuação: {pontos}'
    msgFormatada = fonte.render(mensagem, True, (255, 255, 255))

    perdeu = 'VOCÊ PERDEU!'
    perdeuFormatado = fonte.render(perdeu, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        '''if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                if xSnake > 0 and controle == False:
                    xControle = -10
                    yControle = 0

            if event.key == K_d or event.key == K_RIGHT:
                if xSnake < largura - 45 and controle == False:
                    xControle = 10
                    yControle = 0

            if event.key == K_w or event.key == K_UP:
                if ySnake > 0 and controle == False:
                    yControle = -20
                    xControle = 0

            if event.key == K_s or event.key == K_DOWN:
                if ySnake < altura - 45 and controle == False:
                    yControle = 20
                    xControle = 0'''
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        if xSnake > 0 and controle == False and flagRight == False:
            xSnake -= 10
            flagLeft = True
            flagDown = False
            flagUp = False

    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        if xSnake < largura - 45 and controle == False and flagLeft == False:
            xSnake += 10
            flagRight = True
            flagDown = False
            flagUp = False

    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP] and flagDown == False:
        if ySnake > 0 and controle == False:
            ySnake -= 10
            flagUp = True
            flagLeft = False
            flagRight = False

    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN] and flagUp == False:
        if ySnake < altura - 45 and controle == False:
            ySnake += 10
            flagDown = True
            flagLeft = False
            flagRight = False

    '''xSnake += xControle
    ySnake += yControle'''
    snake = pygame.draw.rect(tela, (75, 0, 130), (xSnake, ySnake, 30, 30))
    apple = pygame.draw.rect(tela, (139, 0, 0), (xApple, yApple, 20, 20))

    if snake.colliderect(apple):
        xApple = randint(40, 600)
        yApple = randint(50, 430) 
        comprimentoIni += 1
        pontos += 1
        flag = True

    cabeca = []
    cabeca.append(xSnake)
    cabeca.append(ySnake)
    corpo.append(cabeca)

    if len(corpo) > comprimentoIni:
        del corpo[0]

    crescer(corpo)

    if xSnake > largura - 45 or xSnake == 0 or ySnake > altura - 45 or ySnake == 0:
        controle = True
        tela.blit(perdeuFormatado, (200, 200))

    tela.blit(msgFormatada, (420, 40))
    pygame.display.update()
