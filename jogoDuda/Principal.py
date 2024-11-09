import pygame
from random import randint

pygame.init()
relogio = pygame.time.Clock()

tamanhoTela = (1280, 720)
tela = pygame.display.set_mode(tamanhoTela)

pygame.display.set_caption("Fairytrans")
dt = 0 


# Carrega o arquivo de música de fundo
pygame.mixer.music.load("MusicaFundo/BoxCat Games - Tricks (1).mp3")


# Carrega a fonte a ser usada no jogo
fonteTempo = pygame.font.Font("Fonts/Energy Station.ttf", 80)

# Carrega a personagem para nosso projeto

listFramesIdle = [
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__IDLE_000.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__IDLE_001.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__IDLE_002.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__IDLE_003.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__IDLE_004.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__IDLE_005.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__IDLE_006.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__IDLE_007.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__IDLE_008.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__IDLE_009.png").convert_alpha()
]

listFramesFLY = [
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__FLY_000.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__FLY_001.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__FLY_002.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__FLY_003.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__FLY_004.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__FLY_005.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__FLY_006.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__FLY_007.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__FLY_008.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__FLY_009.png").convert_alpha()
]

listFramesJump = [
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__JUMP_000.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__JUMP_001.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__JUMP_002.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__JUMP_003.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__JUMP_004.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__JUMP_005.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__JUMP_006.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__JUMP_007.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__JUMP_008.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__JUMP_009.png").convert_alpha()
]

listFramesRunn = [
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__WALK_000.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__WALK_002.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__WALK_003.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__WALK_003.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__WALK_004.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__WALK_005.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__WALK_006.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__WALK_007.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__WALK_008.png").convert_alpha(),
pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__WALK_009.png").convert_alpha(),
]

listFramesDead = [
    pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__DIE_000.png").convert_alpha(),
    pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__DIE_001.png").convert_alpha(),
    pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__DIE_002.png").convert_alpha(),
    pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__DIE_003.png").convert_alpha(),
    pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__DIE_004.png").convert_alpha(),
    pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__DIE_005.png").convert_alpha(),
    pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__DIE_006.png").convert_alpha(),
    pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__DIE_007.png").convert_alpha(),
    pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__DIE_008.png").convert_alpha(),
    pygame.image.load("craftpix-733001-2d-fantasy-fairy-free-character-sprite/_PNG/1/Fairy_01__DIE_009.png").convert_alpha(),
]

#Tamanho imagem
for i in range(len(listFramesIdle)):
    listFramesIdle[i] = pygame.transform.scale(listFramesIdle[i], (800,425))

for i in range(len(listFramesFLY)):
    listFramesFLY[i] = pygame.transform.scale(listFramesFLY[i], (800,425))

for i in range(len(listFramesRunn)):
    listFramesRunn[i] = pygame.transform.scale(listFramesRunn[i], (800,425))

for i in range(len(listFramesJump)):
    listFramesJump[i] = pygame.transform.scale(listFramesJump[i], (800,425))

for i in range(len(listFramesDead)):
    listFramesDead[i] = pygame.transform.scale(listFramesDead[i], (800,425))


# Variaveis da animação do personagem parado
indexFrameIdle= 0 # Controla qual imagem está sendo mostrada na tela
tempoAnimacaoIdle= 0.0 # Controla quanto tempo se passou desde a última troca de frame
velocidadeAnimacaoIdle = 5 # Controlar o tempo de animação em relação ao tempo real (1 / velocidadeAnimacaoIdle)

# Variaveis da animação do personagem andando
indexFrameFLY = 0
tempoAnimacaoFLY = 0.0
velocidadeAnimacaoFLY = 10

# Variaveis da animação do personagem pulando
indexFrameJump = 0
tempoAnimacaoJump = 0.0
velocidadeAnimacaoJump = 5

# Variaveis da animação do personagem correndo
indexFrameRunn = 0
tempoAnimacaoRunn = 0.0
velocidadeAnimacaoRunn = 10

# Variaveis da animação do personagem morto
indexFrameDead = 0
tempoAnimacaoDead = 0.0
velocidadeAnimacaoDead = 3

# Retangulo do personagem na tela para melhor controle e posicionamento do personagem
personagemRect = listFramesIdle[0].get_rect(midbottom=(250, 480))
personagemColisaoRect = pygame.Rect(personagemRect.x, personagemRect.y, 80, 120)

gravidade = 1 # Gravidade do jogo, valor que aumenta a cada frame
direcaoPersonagem = 1 # Direção que o personagem está olhando (1 = Direita, -1 = Esquerda)
estaAndando = False # Define se o personagem está andando ou não

# ASSETS PARA OS OBSTÁCULOS
listaImagensObstaculos = [
    pygame.image.load(f"Obstaculos/Armas/Icon28_{i:02d}.png").convert_alpha() for i in range(1, 40)
] # Lista de obstáculos que aparecerão na tela

# Loop que redimensiona as imagens dos obstáculos
for i in range(len(listaImagensObstaculos)):
    # Redimensiona a imagem para 50x50 pixels
    listaImagensObstaculos[i] = pygame.transform.scale(listaImagensObstaculos[i], (50, 50))
    # Inverte a imagem no eixo X
    listaImagensObstaculos[i] = pygame.transform.flip(listaImagensObstaculos[i], True, False)
    # Rotaciona a imagem em 35 graus
    listaImagensObstaculos[i] = pygame.transform.rotate(listaImagensObstaculos[i], 35)

# ICONES
iconeVida = pygame.image.load("icon/Icon12.png").convert_alpha()
iconeVida = pygame.transform.scale2x(iconeVida)

# ASSETS PARA O PLANO DE FUNDO
# Importa as imagens do plano de fundo
listBgImages = [
    pygame.image.load("craftpix-665532-free-fairy-tale-game-backgrounds/_PNG/4/7.png").convert_alpha(),
    pygame.image.load("craftpix-665532-free-fairy-tale-game-backgrounds/_PNG/4/6.png").convert_alpha(),
    pygame.image.load("craftpix-665532-free-fairy-tale-game-backgrounds/_PNG/4/5.png").convert_alpha(),
    pygame.image.load("craftpix-665532-free-fairy-tale-game-backgrounds/_PNG/4/4.png").convert_alpha(),
    pygame.image.load("craftpix-665532-free-fairy-tale-game-backgrounds/_PNG/4/3.png").convert_alpha(),
    pygame.image.load("craftpix-665532-free-fairy-tale-game-backgrounds/_PNG/4/2.png").convert_alpha(),
    pygame.image.load("craftpix-665532-free-fairy-tale-game-backgrounds/_PNG/4/1.png").convert_alpha(),
]

listaBgVelocidades = [1, 3, 7, 9, 10, 15, 20] # Velocidades de cada imagem do plano de fundo

listaBgPosicoes = [0 for _ in range(len(listBgImages))] # Posições de cada imagem do plano de fundo

# Loop que redimensiona as imagens do plano de fundo
for i in range(len(listBgImages)):
    listBgImages[i] = pygame.transform.scale(listBgImages[i], tamanhoTela)

ALTURA_CHAO = 500
velocidadePersonagem = 30
vidas = 3
GameOver = False
tempoJogo = 0

listaObstaculos = [] # Lista de obstáculos que aparecerão na tela

AUMENTA_DIFICULDADE = pygame.USEREVENT + 1 # Evento para aumentar a dificuldade do jogo
pygame.time.set_timer(AUMENTA_DIFICULDADE, 10000) # Aumenta a dificuldade a cada 10 segundos

tempoMaximoEntreObstaculos = 3000
ADICIONA_OBSTACULO = pygame.USEREVENT + 2 # Evento para adicionar um obstáculo na tela
pygame.time.set_timer(ADICIONA_OBSTACULO, randint(500, tempoMaximoEntreObstaculos)) # Adiciona um obstáculo a cada 1 segundo
estaTocandoMusica = True


# LOOP PRINCIPAL
while True:
    # Verifica se a música de fundo está tocando
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

    # Loop que verifica todos os eventos que acontecem no jogo
    for event in pygame.event.get():

        # Verifica se o evento é de fechar a janela
        if event.type == pygame.QUIT:
            pygame.quit() # Fecha o jogo
            exit() # Fecha o programa

        if not GameOver:
            if event.type == AUMENTA_DIFICULDADE:
                velocidadePersonagem += 4

                if tempoMaximoEntreObstaculos > 1100:
                    tempoMaximoEntreObstaculos -= 300
                    
                pygame.time.set_timer(ADICIONA_OBSTACULO, randint(800, tempoMaximoEntreObstaculos))

            if event.type == ADICIONA_OBSTACULO:
                obstaculoImage = listaImagensObstaculos[randint(0, len(listaImagensObstaculos) - 1)]
                posicaoX = randint(1280, 1500)
                obstaculoRect = obstaculoImage.get_rect(midbottom=(posicaoX, 620))

                obstaculo = {
                    "rect": obstaculoRect,
                    "image": obstaculoImage
                }

                listaObstaculos.append(obstaculo)

    tela.fill((255, 255, 255)) # Preenche a tela com a cor branca

    # Verifica se o jogador perdeu todas as vidas
    if vidas <= 0:
        GameOver = True

    # Percorre todas as imagens do plano de fundo para movimentar
    for i in range(len(listBgImages)):
        if estaAndando:
            listaBgPosicoes[i] -= listaBgVelocidades[i] * velocidadePersonagem * dt * direcaoPersonagem # Move a imagem para a esquerda

        # Verifica se a imagem saiu da tela para a esquerda
        if listaBgPosicoes[i] <= -tamanhoTela[0]:
            listaBgPosicoes[i] = 0 # Retorna a imagem para a posição inicial

        # Verifica se a imagem saiu da tela para a direita
        if listaBgPosicoes[i] >= tamanhoTela[0]:
            listaBgPosicoes[i] = 0

    # Desenha o plano de fundo
    for i in range(len(listBgImages)):
        # Desenha a imagem do plano de fundo que está na tela
        tela.blit(listBgImages[i], (listaBgPosicoes[i], 0))

        # Desenha a imagem do plano de fundo que está fora da tela na direita
        tela.blit(listBgImages[i], (listaBgPosicoes[i] + tamanhoTela[0], 0))

        # Desenha a imagem do plano de fundo que está fora da tela na esquerda
        tela.blit(listBgImages[i], (listaBgPosicoes[i] + -tamanhoTela[0], 0))

    # Atualiza o tempo de jogo
    if not GameOver:
        
        tempoJogo += dt

    # Cria o texto para o tempo de jogo
    textoTempo = fonteTempo.render(str(int(tempoJogo)), False, (255, 255, 255))

    # Desenha o tempo de jogo na tela
    tela.blit(textoTempo, (tamanhoTela[0] / 2, 30))

    # Cria o texto para as vidas do jogador
    for i in range(vidas):
        tela.blit(iconeVida, (20 + i * iconeVida.get_width(), 20))

    # DESENHA O MENU DE REINICIAR O JOGO
    if GameOver:
        if estaTocandoMusica:
            pygame.mixer.music.stop()
            estaTocandoMusica = False

        # Cria o texto para o menu de reiniciar o jogo
        textoGameOver = fonteTempo.render("JAH ERA!", False, (255, 255, 255))
        textoReiniciar = fonteTempo.render("APERTE ENTER PARA REINICIAR", False, (255, 255, 255))

        # Desenha o menu de reiniciar o jogo na tela
        tela.blit(textoGameOver, (484, 260))
        tela.blit(textoReiniciar, (84, 360))


    # DESENHA OS OBSTÁCULOS NA TELA
    for obstaculo in listaObstaculos:
        obstaculo["rect"].x -= 30 * velocidadePersonagem * dt

        # Verifica se o obstáculo saiu da tela
        if obstaculo["rect"].right < 0:
            listaObstaculos.remove(obstaculo)

        tela.blit(obstaculo["image"], obstaculo["rect"])

        # Verifica se houve colisão entre o personagem e o obstáculo
        if personagemColisaoRect.colliderect(obstaculo["rect"]):
            listaObstaculos.remove(obstaculo)
            vidas -= 1

    # Soma o tempo que se passou desde o último frame
    tempoAnimacaoIdle += dt

    # Verifica se o tempo de animação do personagem parado é maior ou igual ao tempo de animação
    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        # Atualiza o frame do personagem parado de acordo com a lista de frames
        indexFrameIdle = (indexFrameIdle + 1) % len(listFramesIdle)
        tempoAnimacaoIdle = 0.0 # Reseta o tempo entre os frames

    # Atualiza a animação do personagem andando
    tempoAnimacaoFLY += dt
    
    # Verifica se o tempo de animação do personagem andando é maior ou igual ao tempo de animação
    if tempoAnimacaoFLY >= 1 / velocidadeAnimacaoFLY:
        # Atualiza o frame do personagem andando
        indexFrameFLY = (indexFrameFLY + 1) % len(listFramesFLY)
        tempoAnimacaoFLY = 0.0

    # Atualiza a animação do personagem pulando
    tempoAnimacaoJump += dt

    # Verifica se o tempo de animação do personagem pulando é maior ou igual ao tempo de animação
    if tempoAnimacaoJump >= 1 / velocidadeAnimacaoJump:
        # Atualiza o frame do personagem pulando
        indexFrameJump = (indexFrameJump + 1) % len(listFramesJump)
        tempoAnimacaoJump = 0.0

    # Atualiza a animação do personagem correndo
    tempoAnimacaoRunn += dt

    # Verifica se o tempo de animação do personagem correndo é maior ou igual ao tempo de animação
    if tempoAnimacaoRunn >= 1 / velocidadeAnimacaoRunn:
        # Atualiza o frame do personagem correndo
        indexFrameRunn = (indexFrameRunn + 1) % len(listFramesRunn)
        tempoAnimacaoRunn = 0.0

    # Atualiza a animação do personagem morto
    if GameOver and indexFrameDead != len(listFramesDead) - 1:
        tempoAnimacaoDead += dt

    # Verifica se o tempo de animação do personagem morto é maior ou igual ao tempo de animação
    if tempoAnimacaoDead >= 1 / velocidadeAnimacaoDead:
        # Atualiza o frame do personagem morto
        indexFrameDead = (indexFrameDead + 1) % len(listFramesDead)
        tempoAnimacaoDead = 0.0

    # Verifica se o personagem está andando
    estaAndando = False

    # Pega as teclas que foram pressionadas
    listTeclas = pygame.key.get_pressed()

    if not GameOver:
        if listTeclas[pygame.K_LEFT]: # Verifica se a tecla esquerda foi pressionada
            direcaoPersonagem = -1 # Define a direção do personagem para a esquerda
            estaAndando = True # Define que o personagem está andando

        if listTeclas[pygame.K_RIGHT]:
            direcaoPersonagem = 1
            estaAndando = True

        if listTeclas[pygame.K_SPACE]: # Verifica se a tecla espaço foi pressionada
            if personagemRect.centery == ALTURA_CHAO: # Verifica se o personagem está no chão
                gravidade = -35 # Define como negativo para o personagem subir
                indexFrameJump = 0 # Reseta o frame do pulo
    else:
        # Reinicia o jogo
        if listTeclas[pygame.K_RETURN]:
            vidas = 3
            GameOver = False
            tempoJogo = 0
            velocidadePersonagem = 30
            tempoMaximoEntreObstaculos = 3000
            listaObstaculos = []
            indexFrameDead = 0

            # Reinicia  a Música de fundo
            pygame.mixer.music.play()
            pygame.mixer.music.stop()
            
          

    # Gravidade Aumenta
    gravidade += 2

    # Atualiza a posição Y do personagem de acordo com a gravidade
    personagemRect.y += gravidade

    # Verifica se o personagem está no chão
    if personagemRect.centery >= ALTURA_CHAO:
        personagemRect.centery = ALTURA_CHAO

    personagemColisaoRect.midbottom = personagemRect.midbottom

    # Desenha o personagem
    if not GameOver:
        if gravidade < 0: # Verifica se o personagem está subindo
            frame = listFramesJump[indexFrameJump]
        else:
            if estaAndando: # Verifica se o personagem está andando
                if velocidadePersonagem < 40:
                    frame = listFramesFLY[indexFrameFLY]
                if velocidadePersonagem < 50:
                    frame = listFramesRunn[indexFrameRunn]
                elif velocidadePersonagem < 70:
                    velocidadeAnimacaoRunn = 30
                    frame = listFramesRunn[indexFrameRunn]
                else:
                    velocidadeAnimacaoRunn = 40
                    frame = listFramesRunn[indexFrameRunn]
                
            else: # Caso contrário, o personagem está parado
                frame = listFramesIdle[indexFrameIdle]
    else:
        frame = listFramesDead[indexFrameDead]

    if direcaoPersonagem == -1: # Verifica se o personagem está olhando para a esquerda e inverte a imagem
        frame = pygame.transform.flip(frame, True, False) # Inverte a imagem

    tela.blit(frame, personagemRect) # Desenha o personagem na tela

    pygame.display.update() # Atualiza a tela

    dt = relogio.tick(60) / 1000 # Define o tempo de cada frame em segundos