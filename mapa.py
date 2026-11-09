#ARQUIVOS NA PASTA IMAGENS E AUDIO
import pygame
import sys
import os
from pygame.locals import QUIT


os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

LARGURA, ALTURA = 800, 600
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Mapa')

clock = pygame.time.Clock()

#Criaçao da "matriz"
matriz_mapa = []
with open("mapa.txt", "r") as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip()
        if linha_limpa:
            #linha do txt virando sublista dentro da matriz
            sublista = list(linha_limpa)
            matriz_mapa.append(sublista)

#dimensões da matriz
linhas = len(matriz_mapa)
colunas = len(matriz_mapa[0]) if linhas > 0 else 0

#Enquadrar
tamanho_por_largura = LARGURA // colunas
tamanho_por_altura = ALTURA // linhas
tile_size = min(tamanho_por_largura, tamanho_por_altura)

largura_mapa_px = colunas * tile_size
altura_mapa_px = linhas * tile_size
offset_x = (LARGURA - largura_mapa_px) // 2
offset_y = (ALTURA - altura_mapa_px) // 2

try:
    #1. Interior (Grama verde - tile_0028)
    tile_grama = pygame.transform.scale(pygame.image.load("tile_0028.png").convert_alpha(), (tile_size, tile_size))

    #Pontas do mapa (rotacionados a partir do tile_0000)
    canto_base = pygame.image.load("tile_0000.png").convert_alpha()
    tile_canto_esq_sup = pygame.transform.scale(canto_base, (tile_size, tile_size))
    tile_canto_dir_sup = pygame.transform.scale(pygame.transform.rotate(canto_base, 270), (tile_size, tile_size))
    tile_canto_dir_inf = pygame.transform.scale(pygame.transform.rotate(canto_base, 180), (tile_size, tile_size))
    tile_canto_esq_inf = pygame.transform.scale(pygame.transform.rotate(canto_base, 90), (tile_size, tile_size))

    #Bordas do mapa (rotacionadas a partir do tile_0001)
    borda_base = pygame.image.load("tile_0001.png").convert_alpha()
    tile_borda_topo = pygame.transform.scale(borda_base, (tile_size, tile_size))
    tile_borda_baixo = pygame.transform.scale(pygame.transform.rotate(borda_base, 180), (tile_size, tile_size))
    tile_borda_esq = pygame.transform.scale(pygame.transform.rotate(borda_base, 90), (tile_size, tile_size))
    tile_borda_dir = pygame.transform.scale(pygame.transform.rotate(borda_base, 270), (tile_size, tile_size))

    # 4. Arbusto com colisão física ('B') - tile_0346
    tile_arbusto = pygame.transform.scale(pygame.image.load("tile_0346.png").convert_alpha(), (tile_size, tile_size))

    # 5. Sprites direcionais do personagem careca
    sprite_esquerda = pygame.transform.scale(pygame.image.load("tile_0347.png").convert_alpha(), (tile_size, tile_size))
    sprite_baixo = pygame.transform.scale(pygame.image.load("tile_0348.png").convert_alpha(), (tile_size, tile_size))
    sprite_cima = pygame.transform.scale(pygame.image.load("tile_0349.png").convert_alpha(), (tile_size, tile_size))
    sprite_direita = pygame.transform.scale(pygame.image.load("tile_0350.png").convert_alpha(), (tile_size, tile_size))

#Inicio: personagem olhar para baixo
sprite_jogador = sprite_baixo

#posição inicial segura do jogador dentro do mapa (livre no interior)
pos_x = offset_x + (tile_size * 2)
pos_y = offset_y + (tile_size * 2)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    dt = clock.get_time()

    #guarda a posição anterior para barrar o movimento na colisão
    old_pos_x = pos_x
    old_pos_y = pos_y

    #movimentação nas 4 direções e troca dinâmica do sprite conforme a direção
    keys = pygame.key.get_pressed()
    velocidade = 0.25
    
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        pos_x += velocidade * dt
        sprite_jogador = sprite_direita
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        pos_x -= velocidade * dt
        sprite_jogador = sprite_esquerda
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        pos_y -= velocidade * dt
        sprite_jogador = sprite_cima
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        pos_y += velocidade * dt
        sprite_jogador = sprite_baixo

    #restrição da borda
    limite_esq = offset_x + tile_size
    limite_dir = offset_x + largura_mapa_px - (tile_size * 2)
    limite_cima = offset_y + tile_size
    limite_baixo = offset_y + altura_mapa_px - (tile_size * 2)

    if pos_x < limite_esq: pos_x = limite_esq
    if pos_x > limite_dir: pos_x = limite_dir
    if pos_y < limite_cima: pos_y = limite_cima
    if pos_y > limite_baixo: pos_y = limite_baixo

    #cor de fundo da janela
    screen.fill((56, 203, 171))

    #hitbox do jogador
    collider_jogador = pygame.Rect(pos_x, pos_y, tile_size, tile_size)
    colideres_obstaculos = []

    # renderiza percorrendo matriz
    for i in range(linhas):
        for j in range(colunas):
            tipo_bloco = matriz_mapa[i][j]
            
            bx = offset_x + (j * tile_size)
            by = offset_y + (i * tile_size)
            rect_bloco = pygame.Rect(bx, by, tile_size, tile_size)

            #renderiza cantos e bordas exteriores com base na posição da matriz
            if i == 0 and j == 0:
                screen.blit(tile_canto_esq_sup, (bx, by))
                colideres_obstaculos.append(rect_bloco)
            elif i == 0 and j == colunas - 1:
                screen.blit(tile_canto_dir_sup, (bx, by))
                colideres_obstaculos.append(rect_bloco)
            elif i == linhas - 1 and j == 0:
                screen.blit(tile_canto_esq_inf, (bx, by))
                colideres_obstaculos.append(rect_bloco)
            elif i == linhas - 1 and j == colunas - 1:
                screen.blit(tile_canto_dir_inf, (bx, by))
                colideres_obstaculos.append(rect_bloco)
            elif i == 0:
                screen.blit(tile_borda_topo, (bx, by))
                colideres_obstaculos.append(rect_bloco)
            elif i == linhas - 1:
                screen.blit(tile_borda_baixo, (bx, by))
                colideres_obstaculos.append(rect_bloco)
            elif j == 0:
                screen.blit(tile_borda_esq, (bx, by))
                colideres_obstaculos.append(rect_bloco)
            elif j == colunas - 1:
                screen.blit(tile_borda_dir, (bx, by))
                colideres_obstaculos.append(rect_bloco)
            else:
                #interior da matriz baseado nas letras do mapa.txt
                if tipo_bloco == "G":
                    screen.blit(tile_grama, (bx, by))
                elif tipo_bloco == "B":
                    screen.blit(tile_grama, (bx, by)) #Grama de fundo
                    screen.blit(tile_arbusto, (bx, by)) #arbusto por cima com colisão
                    colideres_obstaculos.append(rect_bloco)
                else:
                    screen.blit(tile_grama, (bx, by))

    #verificar colisao
    for obs in colideres_obstaculos:
        if collider_jogador.colliderect(obs):
            pos_x = old_pos_x
            pos_y = old_pos_y
            break
    #personagem
    screen.blit(sprite_jogador, (pos_x, pos_y))

    pygame.display.update()
