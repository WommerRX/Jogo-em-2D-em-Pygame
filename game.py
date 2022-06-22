import pygame
import random
import os
os.system("cls")
pygame.init()
largura = 1600  
altura = 900
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("go MARIO go!")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("assets/MarioIco.ico")
pygameDisplay.set_icon(gameIcon)
os.system("cls")
nome = input("Qual o seu nome?")
email = input("Qual seu email:")
arquivo = open("historico.txt","a")
arquivo.write(f'Nome > {nome}\n')
arquivo.write(f'Email > {email}\n')
arquivo.write('\n')
arquivo.close
bg = pygame.image.load("assets/fundo.png")
gameOvertela = pygame.image.load("assets/gameover.jpeg")


morteMario = pygame.mixer.Sound("assets/mortemario.mp3")
morteMario.set_volume(0.5)
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
gameEvents = pygame.event


def dead(pontos):
    gameDisplay.blit(gameOvertela, (0, 0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(morteMario)
    fonte = pygame.font.Font("freesansbold.ttf", 50)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 25)
    texto = fonte.render("Você Perdeu com "+str(pontos) +
                         " pontos!", True, black)
    textoContinue = fonteContinue.render(
        "Press enter to continue...", True, white)
    gameDisplay.blit(textoContinue, (100, 400))
    gameDisplay.blit(texto, (400, 100))
    pygameDisplay.update()


def jogo():
    posicaoX = 0
    posicaoY = random.randrange(0, altura)
    direcao = True
    velocidade = 5
    posicaoXMario = 500
    posicaoYMario = 100
    movimentoXMario = 0
    movimentoYMario = 0
    pontos = 0
    bowser = pygame.image.load("assets/bowser.png")
    mariovoador = pygame.image.load("assets/mariovoaa.png")
    bowser = pygame.transform.flip(bowser, True, False)
    pygame.mixer.music.load("assets/trilha.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    bowsersom = pygame.mixer.Sound("assets/sombowser1.wav")
    bowsersom.set_volume(0.02)
    pygame.mixer.Sound.play(bowsersom)

    alturaMario = 180
    larguraMario = 90
    alturaBowser = 150
    larguraBowser = 100
    dificuldade = 29
    jogando = True
    while True:
        # aqui é lido os eventos da tela
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jogo()
                if event.key == pygame.K_LEFT:
                    movimentoXMario = - 10
                elif event.key == pygame.K_RIGHT:
                    movimentoXMario = 10
                elif event.key == pygame.K_UP:
                    movimentoYMario = -10
                elif event.key == pygame.K_DOWN:
                    movimentoYMario = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXMario = 0
                    movimentoYMario = 0

        if jogando == True:
            # travando o movimento na tela
            posicaoXMario = posicaoXMario + movimentoXMario
            posicaoYMario = posicaoYMario + movimentoYMario
            if posicaoXMario < 0:
                posicaoXMario = 0
            elif posicaoXMario >= largura - larguraMario:
                posicaoXMario = largura - larguraMario

            if posicaoYMario < 0:
                posicaoYMario = 0
            elif posicaoYMario >= altura - alturaMario:
                posicaoYMario = altura - alturaMario

            # aqui termina a leitura de eventos
            # gameDisplay.fill(pink)
            gameDisplay.blit(bg, (0, 0))

            if direcao == True:
                if posicaoX < largura-150:
                    posicaoX = posicaoX + velocidade
                else:
                    pygame.mixer.Sound.play(bowsersom)
                    direcao = False
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    bowser = pygame.transform.flip(bowser, True, False)
                    pontos = pontos + 1
            else:
                if posicaoX >= 0:
                    posicaoX = posicaoX - velocidade
                else:
                    pygame.mixer.Sound.play(bowsersom)
                    direcao = True
                    posicaoY = random.randrange(0, altura)
                    velocidade = velocidade + 1
                    bowser = pygame.transform.flip(bowser, True, False)
                    pontos = pontos + 1

            gameDisplay.blit(bowser, (posicaoX, posicaoY))
            gameDisplay.blit(mariovoador, (posicaoXMario, posicaoYMario))
            # pygame.draw.circle(
            #    gameDisplay, black, [posicaoX, posicaoY], 20, 0)
            fonte = pygame.font.Font("freesansbold.ttf", 20)
            texto = fonte.render("Pontos: "+str(pontos), True, white)
            gameDisplay.blit(texto, (20, 20))

            # análise de colisão (modelo 1)
            '''
            naveRect = mariovoador.get_rect()
            naveRect.x = posicaoXMario
            naveRect.y = posicaoYMario

            missileRect = bowser.get_rect()
            missileRect.x = posicaoX
            missileRect.y = posicaoY

            if naveRect.colliderect(missileRect):
                dead(pontos)
            else:
                print("ainda vivo...")
            '''
            # análise de colisão (modelo 2)

            pixelsYNave = list(
                range(posicaoYMario, posicaoYMario + alturaMario+1))
            pixelsXNave = list(
                range(posicaoXMario, posicaoXMario + larguraMario+1))

            pixelsYMissel = list(range(posicaoY, posicaoY+alturaBowser+1))
            pixelsXMissel = list(range(posicaoX, posicaoX+larguraBowser+1))

            # comparar e mostrar elementos iguais em duas listas
            # print(len(list(set(pixelsYMissel) & set(pixelsYNave))))

            if len(list(set(pixelsYMissel) & set(pixelsYNave))) > dificuldade:
                if len(list(set(pixelsXMissel) & set(pixelsXNave))) > dificuldade:
                    jogando = False
                    dead(pontos)

        pygameDisplay.update()
        clock.tick(60)


jogo()