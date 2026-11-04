import pygame
import sys
import os
from pygame.locals import QUIT, KEYDOWN

#resolvendo erro de diretorio
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#cria relogi 
clock = pygame.time.Clock()
#carregar imagem 
hero_img = pygame.image.load("assets/assets/Hero_Walk_01.png")
#frame animação 
curr_frame = 0
#tempo
anim_time = 0
#Lista com frames do herói
hero_walk_list = []
#Carregando 16 frames da pasta assets/assets/
for i in range(16):
    hero_walk_list.append(pygame.image.load(f"assets/assets/Hero_Walk_{i+1:02d}.png"))
#Variáveis de controle usando spritesheet
run_animation = False        #Controla se a animação do Megaman deve rodar ou não
curr_frame_mm = 0            #Frame atual na spritesheet
anim_time_mm = 0             #Acumulador de tempo 
megaman_spritesheet = pygame.image.load("megaman_spritesheet.png") #Carrega a imagem da spritesheet

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

#Loop principal
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Verse teclas do teclado foram pressionadas
        if event.type == KEYDOWN:
            #Se a tecla pressionada foi a BARRA DE ESPAÇO
            if event.key == pygame.K_SPACE:
                run_animation = True  #ativa a flag para rodar a animação

    #Limita a rodar no máximo a 60FPS
    clock.tick(60)
    dt = clock.get_time()

    #acumular o tempo para atualizar a animação do herói
    anim_time = anim_time + dt
    #tempo acumulado em segundos
    anim_time_sec = anim_time/1000
    #0.15 segundos, avança para o próximo frame da animação do herói
    if anim_time_sec > 0.15:
        curr_frame = curr_frame + 1
        #caso ultrapasse o último frame disponível na lista, reinicia o loop 
        if curr_frame > len(hero_walk_list) - 1:
            curr_frame = 0
        anim_time = 0  #resetar temporizador do frame
    
    #se a animação estiver ativada, gerenciar tempo
    if run_animation:
        anim_time_mm = anim_time_mm + dt
        anim_time_mm_sec = anim_time_mm/1000

        #a cada 0.1 segundos, avança o frame da animação
        if anim_time_mm_sec > 0.1:
            curr_frame_mm = curr_frame_mm + 1
            #Se passar do limite de frames da spritesheet (10 frames, de 0 a 9)
            if curr_frame_mm > 9:
                curr_frame_mm = 0       #resetar o frame
                run_animation = False   #desativa a animação ao completar o ciclo
            anim_time_mm = 0            #reseta o temporizador

    #cor branca 
    screen.fill((255, 255, 255))
    #frame atual da animação do herói na coordenada (0, 0)
    screen.blit(hero_walk_list[curr_frame], (0, 0))
    #Recorte da spritesheet do Megaman na posição (200, 200)
    screen.blit(megaman_spritesheet, (200, 200), (60*(curr_frame_mm%5), 60*(curr_frame_mm//5), 60, 60))

    pygame.display.update()
