import pygame
#Inicializar o pygame
pygame.init()

#cria uma tela com tamanho especificado
tamanho = (900, 500)
tela = pygame.display.set_mode(tamanho)

#define o titulo da janela
pygame.display.set_caption("Hello Games!")

#define um relógio para controlar o FPS
relogio = pygame.time.Clock()

posicaoBola = pygame.Vector2(450, 250)
dt = 0
direcaoY = 1
direcaoX = 1


while True:
    #lida com os eventos da aplicação
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit() #Fechamento o pygame

    #preenche a tela com uma cor
    tela.fill((100, 200, 255)) 

    #Desenha um circulo na tela
    pygame.draw.circle(tela, (200, 150, 200), posicaoBola, 50)

    posicaoBola.y += 100 * direcaoY * dt
    posicaoBola.x += 100 * direcaoX * dt

    if posicaoBola.y >= 450 or posicaoBola.y <= 50:
        direcaoY *= -1

    if posicaoBola.x >= 850 or posicaoBola.x <= 50:
        direcaoX *= -1


    #elif posicaoBola.y <= 50:
    # direcaoY += 1
        
    #Atualiza a tela
    pygame.display.update()
    dt = relogio.tick(60) / 250 #Define a quantidade de FPS

    #Define a quantidade de FPS
    #relogio.tick(60)       