import pygame

pygame.init()

relogio = pygame.time.Clock()

tamanho = (1200, 500)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Homeless Walker")
dt = 0 

folhaSpritesIdle = pygame.image.load("assets/Homeless_1/Idle.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_1/Walk.png").convert_alpha()

framesIdle = []
for i in range(6):
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale(frame, (256, 256))
    framesIdle.append(frame)

indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 10

personagemRect = framesIdle[0] .get_rect(midbottom = (100, 480))

gravidade = 1

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    tela.fill((255, 255, 255))

    tempoAnimacaoIdle += dt

    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        indexFrameIdle = (indexFrameIdle + 1 ) % len(framesIdle)
        tempoAnimacaoIdle = 0.0
        
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        personagemRect.x -= 200 * dt
    if teclas[pygame.K_RIGHT]:
        personagemRect.x += 200 * dt
    if teclas[pygame.K_SPACE]:
        if personagemRect.centery == 330:
            gravidade = -30
    gravidade += 3
    personagemRect.y += gravidade

    if personagemRect.centery > 330:
        personagemRect.centery = 330

    

    tela.blit(framesIdle[indexFrameIdle], personagemRect)

    #pygame.draw.rect(tela, (0, 0, 0), personagemRect, 2)

    pygame.display.update()
    dt = relogio.tick(60) / 1000