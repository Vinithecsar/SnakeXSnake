import pygame, random
from pygame.locals import *

CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3


um_jogador = False
dois_jogadores =  False

# determinar a posição da fruta em pixels múltiplos de 10

def grid_random():
  x = random.randint(0,440)
  y = random.randint(0,440)
  return ((x//10) * 10, (y//10) * 10)

# colisao fruta e cabeça da cobra
def colisao(c1, c2):
  return (c1[0] == c2[0]) and (c1[1] == c2[1])

def movimento(snake, direcao):

  if direcao == CIMA:
   snake[0] = (snake[0][0], snake[0][1] - 10)
  if direcao == BAIXO:
   snake[0] = (snake[0][0], snake[0][1] + 10)
  if direcao == DIREITA:
   snake[0] = (snake[0][0] + 10, snake[0][1])
  if direcao == ESQUERDA:
   snake[0] = (snake[0][0] - 10, snake[0][1])
  return snake[0]

def colisao_entre_snakes(snake1, snake2):
  perdeu = False

  for pos in snake2:
    if (snake1[0][0] == pos[0]) and (snake1[0][1] == pos[1]):
      perdeu = True
  for pos in snake1:
    if (snake2[0][0] == pos[0]) and (snake2[0][1] == pos[1]):
      perdeu = True

  return perdeu


# Iniciar pygame, definir tamanho da janela

pygame.init()

screen = pygame.display.set_mode((600,450))

pygame.display.set_caption('Snake X Snake')

# Definir posição da fruta e características

fruit_pos = grid_random()

fruit = pygame.Surface((10,10))

fruit.fill((255,0,0)) #Vermelho

# Definir posição da cobra etc

snake_1 = [(200,150),(210,150),(220,150)]
snake_2 = [(400,150),(390,150), (380,150)]

snake_1_skin = pygame.Surface((10,10))
snake_2_skin = pygame.Surface((10,10))

snake_1_skin.fill((0,128,0)) #Verde
snake_2_skin.fill((255,255,0)) #Amarelo

direcao_1 = ESQUERDA
direcao_2 = DIREITA

relogio = pygame.time.Clock()

menu = pygame.image.load('menu1.png')
tutorialjg1 = pygame.image.load('jogador1tutorial.png')
tutorialjg2 = pygame.image.load('jogador2tutorial.png')
regras1 = pygame.image.load('regras1.png')
regras2 = pygame.image.load('regras2.png')
pause = pygame.image.load
game_over = pygame.image.load('game_over.png')
pausado = pygame.image.load('tela pausado.png')
logoif = pygame.image.load('logo_ifrn.png')

som_1 = pygame.mixer.Sound('pontos.wav')
som_2 = pygame.mixer.Sound('pontos2.wav')
musica = pygame.mixer.Sound('musicajogo.wav')

fonte = pygame.font.Font('freesansbold.ttf', 18)

pontuacao_1 = 0
pontuacao_2 = 0

while True:

 running = False
 while not running:
 
   screen.blit(menu, (0,0))
   screen.blit(logoif, (10,420))
 
   for event in pygame.event.get():
 
     if event.type == QUIT:
       pygame.quit()
     
     if event.type == KEYDOWN:
       if event.key == K_1:
 
         um_jogador = True
         running = True
 
       if event.key == K_2:
 
         dois_jogadores = True
         running = True
 
       if event.key == K_ESCAPE:
         pygame.quit()
     
   pygame.display.update()

 if um_jogador:
 
  tutorial = False
  while not tutorial:
 
   screen.blit(tutorialjg1,(0,0))
   screen.blit(logoif, (10,420))
 
   for event in pygame.event.get():
 
     if event.type == QUIT:
       pygame.quit()
 
     if event.type == KEYDOWN:
       if event.key == K_RETURN:
 
         tutorial = True
 
       if event.key == K_ESCAPE:
         pygame.quit()
 
   pygame.display.update()
 
  

# tutorial das regras

  tutorial2 = False
  while not tutorial2:
 
   screen.blit(regras1,(0,0))
   screen.blit(logoif, (10,420))
 
   for event in pygame.event.get():
 
     if event.type == QUIT:
       pygame.quit()
 
     if event.type == KEYDOWN:
       if event.key == K_RETURN:
 
         tutorial2 = True
 
       if event.key == K_ESCAPE:
         pygame.quit()
 
   pygame.display.update()
 
  pygame.mixer.Sound.play(musica)

  PAUSADO = 4
  RODANDO = 5

  jogo = RODANDO

  fim_de_jogo = False

  while not fim_de_jogo:
 
    relogio.tick(10)
 
    for event in pygame.event.get():
     if event.type == QUIT:
         pygame.quit()
 
     if event.type == KEYDOWN:

       if event.key == K_ESCAPE:
         pygame.quit()

 
    # controlar direção da cobra



     if event.type == KEYDOWN:
 
       if direcao_1 == CIMA or direcao_1 == BAIXO:
         if event.key == K_a:
           direcao_1 = ESQUERDA
 
         if event.key == K_d:
           direcao_1 = DIREITA
           

       if event.key == K_SPACE:

           if jogo != PAUSADO:  
            jogo = PAUSADO
            pygame.mixer.pause()
            screen.blit(pausado, (90,50))
           else:
             jogo = RODANDO
             pygame.mixer.unpause()

 
       if direcao_1 == ESQUERDA or direcao_1 == DIREITA:
         if event.key == K_w:
           direcao_1 = CIMA

         if event.key == K_s:
           direcao_1 = BAIXO

    if jogo == PAUSADO:
     pygame.display.flip()

     continue

    # Se a cobra come a fruta
    if colisao(snake_1[0], fruit_pos):
 
     fruit_pos = grid_random()
     snake_1.append((0,0))
     pontuacao_1 += 1
     pygame.mixer.Sound.play(som_1)
 
    # definir a posição do pedaço que surgiu ao comer a fruta
    for i in range(len(snake_1) - 1, 0, -1):
     snake_1[i] = (snake_1[i-1][0], snake_1[i-1][1])
 
    # movimentar a posição da cobra
    movimento(snake_1, direcao_1)

    # Se a cobra bate na parede, o jogo fecha
    if snake_1[0][0] > 600 or snake_1[0][0] < 0 or snake_1[0][1] > 450 or snake_1[0][1] < 0:
 
     pygame.mixer.Sound.stop(musica)

     reiniciar = False
     while not reiniciar:
 
       screen.blit(game_over,(0,0))
       screen.blit(logoif, (10,420))

       for event in pygame.event.get():
        if event.type == QUIT:
         pygame.quit()
 
        if event.type == KEYDOWN:
         if event.key == K_ESCAPE:
          pygame.quit()
         if event.key == K_RETURN:

          snake_1 = [(200,150),(210,150),(220,150)]
          pontuacao_1 = 0
          fruit_pos = grid_random()
          direcao_1 = ESQUERDA
          pygame.mixer.Sound.play(musica)
          reiniciar = True
 
         if event.key == K_SPACE :
           snake_1 = [(200,150),(210,150),(220,150)]
           pontuacao_1 = 0
           direcao_1 = ESQUERDA

           reiniciar = True
           fim_de_jogo = True
           running = False
           um_jogador = False
           
          
       screen.blit(fonte.render('Final score: {}'.format(pontuacao_1), True, (0, 200, 0)), (230, 320))
       screen.blit(fonte.render('Pressione Enter para jogar novamente', True, (173,255,47)), (120, 360))
       screen.blit(fonte.render('Pressione Esc para fechar o jogo',True, (255,100,100)), (145,410))
       screen.blit(fonte.render('Pressione espaço para voltar ao menu principal', True, (255,255,255)), (90, 385))

       pygame.display.update()
 
    #se a cobra bate nela mesma
    if snake_1[0] in snake_1[1:]:
 
      pygame.mixer.Sound.stop(musica)
 
      reiniciar = False
      while not reiniciar:
 
       screen.blit(game_over,(0,0))
       screen.blit(logoif, (10,420))
 
       for event in pygame.event.get():
        if event.type == QUIT:
         pygame.quit()
 
        if event.type == KEYDOWN:
         if event.key == K_ESCAPE:
          pygame.quit()
 
         if event.key == K_RETURN:

          snake_1 = [(200,150),(210,150),(220,150)]
          pontuacao_1 = 0
          fruit_pos = grid_random()
          direcao_1 = ESQUERDA
          pygame.mixer.Sound.play(musica)
          reiniciar = True

         if event.key == K_SPACE:
           snake_1 =  [(200,150),(210,150),(220,150)]
           pontuacao_1 = 0
           direcao_1 = ESQUERDA

           reiniciar = True
           fim_de_jogo = True
           running = False
           um_jogador = False

       screen.blit(fonte.render('Final score: {}'.format(pontuacao_1), True, (0, 200, 0)), (230, 320))
       screen.blit(fonte.render('Pressione Enter para jogar novamente', True, (173,255,47)), (120, 360))
       screen.blit(fonte.render('Pressione Esc para fechar o jogo',True, (255,100,100)), (145,410))
       screen.blit(fonte.render('Pressione espaço para voltar ao menu principal', True, (255,255,255)), (90, 385))
 
       pygame.display.update()
 
   # colorindo e desenhando na tela
    screen.fill((0,0,0))
    screen.blit(logoif, (10,420))
    screen.blit(fruit, fruit_pos)
 
    for pos in snake_1:
     screen.blit(snake_1_skin,pos)
 
    for x in range(0, 600, 10):
     pygame.draw.line(screen, (10, 10, 10), (x, 0), (x, 450))
 
    for y in range(0, 450, 10): 
     pygame.draw.line(screen, (10, 10, 10), (0, y), (600, y))
   
    screen.blit(fonte.render('Score: {}'.format(pontuacao_1), True, (0, 200, 0)), (15 , 20))

    pygame.display.update()
 
 #  Dois jogadores
 if dois_jogadores:
 
  tutorial = False
  while not tutorial:
 
   screen.blit(tutorialjg2,(0,0))
   screen.blit(logoif, (10,420))
 
   for event in pygame.event.get():
     if event.type == QUIT:
       pygame.quit()
 
     if event.type == KEYDOWN:
       if event.key == K_RETURN:
        tutorial = True
 
       if event.key == K_ESCAPE:
         pygame.quit()
 
   pygame.display.update()
 
  

# tutorial das regras

  tutorial2 = False
  while not tutorial2:
 
   screen.blit(regras2,(0,0))
   screen.blit(logoif, (10,420))
 
   for event in pygame.event.get():
 
     if event.type == QUIT:
       pygame.quit()
 
     if event.type == KEYDOWN:
       if event.key == K_RETURN:
 
         tutorial2 = True
 
       if event.key == K_ESCAPE:
         pygame.quit()
 
   pygame.display.update()

  pygame.mixer.Sound.play(musica)

  PAUSADO = 4
  RODANDO = 5

  jogo = RODANDO

  fim_de_jogo = False
  while not fim_de_jogo:
 
   relogio.tick(10)

   for event in pygame.event.get():

     # fechar o jogo
     if event.type == QUIT:
       pygame.quit()

   # controlar direção da cobra
     if event.type == KEYDOWN:

       if event.key == K_ESCAPE:
         pygame.quit()

       if event.key == K_SPACE:           
          if jogo != PAUSADO:
           jogo = PAUSADO
           screen.blit(pausado, (90,50))
           pygame.mixer.pause()

          else:
            jogo = RODANDO
            pygame.mixer.unpause()
 
       if direcao_1 == CIMA or direcao_1 == BAIXO:
         if event.key == K_a:
           direcao_1 = ESQUERDA
 
         if event.key == K_d:
           direcao_1 = DIREITA
 
       if direcao_1 == ESQUERDA or direcao_1 == DIREITA:
         if event.key == K_w:
           direcao_1 = CIMA
 
         if event.key == K_s:
           direcao_1 = BAIXO
 
       if direcao_2 == CIMA or direcao_2 == BAIXO:
         if event.key == K_LEFT:
           direcao_2 = ESQUERDA
 
         if event.key == K_RIGHT:
           direcao_2 = DIREITA
       
       if direcao_2 == DIREITA or direcao_2 == ESQUERDA:
         if event.key == K_UP:
           direcao_2 = CIMA
 
         if event.key == K_DOWN:
           direcao_2 = BAIXO

   if jogo == PAUSADO: 
    pygame.display.flip()

    continue
 
 
  # Se a cobra come a fruta
   if colisao(snake_1[0], fruit_pos):
 
     fruit_pos = grid_random()
     snake_1.append((0,0))
     pontuacao_1 += 1
     pygame.mixer.Sound.play(som_1)
 
   if colisao(snake_2[0], fruit_pos):
 
     fruit_pos = grid_random()
     snake_2.append((0,0))
     pontuacao_2 += 1
     pygame.mixer.Sound.play(som_2)
 
  # definir a posição do pedaço que surgiu ao comer a fruta
   for i in range(len(snake_1) - 1, 0, -1):
     snake_1[i] = (snake_1[i-1][0], snake_1[i-1][1])
 
   for i in range(len(snake_2) - 1, 0, -1):
     snake_2[i] = (snake_2[i-1][0], snake_2[i-1][1])
 
  # movimentar a posição da cobra
   movimento(snake_1, direcao_1)
   movimento(snake_2, direcao_2)

   # Se a cobra bate na parede, o jogo fecha
   if snake_1[0][0] > 600 or snake_1[0][0] < 0 or snake_1[0][1] > 450 or snake_1[0][1] < 0 or snake_2[0][0] > 600 or snake_2[0][0] < 0 or snake_2[0][1] > 450 or snake_2[0][1] < 0:
 
      pygame.mixer.Sound.stop(musica)
 
      reiniciar = False
      while not reiniciar:
 
       screen.blit(game_over,(0,0))
       screen.blit(logoif, (10,420))
 
       for event in pygame.event.get():
        if event.type == QUIT:
         pygame.quit()
 
        if event.type == KEYDOWN:
         if event.key == K_ESCAPE:
          pygame.quit()
 
         if event.key == K_RETURN:

          snake_1 = [(200,150),(210,150),(220,150)]
          snake_2 = [(400,150),(390,150), (380,150)]
          pontuacao_1 = 0
          pontuacao_2 = 0
          direcao_1 = ESQUERDA
          direcao_2 = DIREITA
          fruit_pos = grid_random()
 
          pygame.mixer.Sound.play(musica)
         
          reiniciar = True

         if event.key == K_SPACE:

           snake_1 =  [(200,150),(210,150),(220,150)]
           snake_2 =  [(400,150),(390,150), (380,150)]
           pontuacao_1 = 0
           pontuacao_2 = 0
           direcao_1 = ESQUERDA
           direcao_2 = DIREITA

           reiniciar = True
           fim_de_jogo = True
           running = False
           dois_jogadores = False
         
 
       screen.blit(fonte.render('Final score: {}'.format(pontuacao_1), True, (0, 200, 0)), (125, 325))
       screen.blit(fonte.render('Final score: {}'.format(pontuacao_2), True, (255,255,0)), (320, 325))
       screen.blit(fonte.render('Pressione Enter para jogar novamente', True, (173,255,47)), (120, 360))
       screen.blit(fonte.render('Pressione Esc para fechar o jogo',True, (255,100,100)), (145,410))
       screen.blit(fonte.render('Pressione espaço para voltar ao menu principal', True, (255,255,255)), (90, 385))
 
       pygame.display.update()
 
  #se a cobra bate nela mesma
   if snake_1[0] in snake_1[1:] or snake_2[0] in snake_2[1:]:

     pygame.mixer.Sound.stop(musica)
 
     reiniciar = False
     while not reiniciar:
 
       screen.blit(game_over,(0,0))
       screen.blit(logoif, (10,420))
 
       for event in pygame.event.get():
        if event.type == QUIT:
         pygame.quit()
 
        if event.type == KEYDOWN:
         if event.key == K_ESCAPE:
          pygame.quit()
 
         if event.key == K_RETURN:
 
          snake_1 = [(200,150),(210,150),(220,150)]
          snake_2 = [(400,150),(390,150), (380,150)]
          pontuacao_1 = 0
          pontuacao_2 = 0
          direcao_1 = ESQUERDA
          direcao_2 = DIREITA
          fruit_pos = grid_random()
 
          pygame.mixer.Sound.play(musica)
         
          reiniciar = True

         if event.key == K_SPACE:

          snake_1 = [(200,150),(210,150),(220,150)]
          snake_2 = [(400,150),(390,150), (380,150)]
          pontuacao_1 = 0
          pontuacao_2 = 0
          direcao_1 = ESQUERDA
          direcao_2 = DIREITA

          reiniciar = True
          fim_de_jogo = True
          running = False
          dois_jogadores = False

       screen.blit(fonte.render('Final score: {}'.format(pontuacao_1), True, (0, 200, 0)), (125, 325))
       screen.blit(fonte.render('Final score: {}'.format(pontuacao_2), True, (255,255,0)), (320, 325))
       screen.blit(fonte.render('Pressione Enter para jogar novamente', True, (173,255,47)), (120, 360))
       screen.blit(fonte.render('Pressione Esc para fechar o jogo',True, (255,100,100)), (145,410))
       screen.blit(fonte.render('Pressione espaço para voltar ao menu principal', True, (255,255,255)), (90, 385))

       pygame.display.update()
 
  #se a cobra bate uma na outra
   if colisao_entre_snakes(snake_1, snake_2):
 
     pygame.mixer.Sound.stop(musica)

     reiniciar = False
     while not reiniciar:
 
       screen.blit(game_over,(0,0))
       screen.blit(logoif, (10,420))
 
       for event in pygame.event.get():
        if event.type == QUIT:
         pygame.quit()
 
        if event.type == KEYDOWN:
         if event.key == K_ESCAPE:
          pygame.quit()
 
         if event.key == K_RETURN:
 
          snake_1 = [(200,150),(210,150),(220,150)]
          snake_2 = [(400,150),(390,150), (380,150)]
          pontuacao_1 = 0
          pontuacao_2 = 0
          direcao_1 = ESQUERDA
          direcao_2 = DIREITA
          fruit_pos = grid_random()
 
          pygame.mixer.Sound.play(musica)
         
          reiniciar = True

         if event.key == K_SPACE:

          snake_1 = [(200,150),(210,150),(220,150)]
          snake_2 = [(400,150),(390,150), (380,150)]
          pontuacao_1 = 0
          pontuacao_2 = 0
          direcao_1 = ESQUERDA
          direcao_2 = DIREITA

          reiniciar = True
          fim_de_jogo = True
          running = False
          dois_jogadores = False
 
 
       screen.blit(fonte.render('Final score: {}'.format(pontuacao_1), True, (0, 200, 0)), (125, 325))
       screen.blit(fonte.render('Final score: {}'.format(pontuacao_2), True, (255,255,0)), (320, 325))
       screen.blit(fonte.render('Pressione Enter para jogar novamente', True, (173,255,47)), (120, 360))
       screen.blit(fonte.render('Pressione Esc para fechar o jogo',True, (255,100,100)), (145,410))
       screen.blit(fonte.render('Pressione espaço para voltar ao menu principal', True, (255,255,255)), (90, 385))

       pygame.display.update()
 
  # colorindo e desenhando na tela
   screen.fill((0,0,0))
   screen.blit(logoif, (10,420))
   screen.blit(fruit, fruit_pos)
 
   for pos in snake_1:
     screen.blit(snake_1_skin,pos)
 
   for pos in snake_2:
     screen.blit(snake_2_skin,pos)
 
   for x in range(0, 600, 10):
    pygame.draw.line(screen, (10, 10, 10), (x, 0), (x, 450))
 
   for y in range(0, 450, 10):
    pygame.draw.line(screen, (10, 10, 10), (0, y), (600, y))
 
   screen.blit(fonte.render('Score: {}'.format(pontuacao_1), True, (0, 200, 0)), (15, 20))
   screen.blit(fonte.render('Score: {}'.format(pontuacao_2), True, (255,255,0)), (520 ,20))
 
   pygame.display.update()
