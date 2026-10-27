import pygame
import sys
import random
from pygame.locals import QUIT

pygame.init()

#janela 
screen = pygame.display.set_mode((900, 400))
pygame.display.set_caption('Atividade 10 - Histogramas no Pygame')

#L1
lista_1 = [random.randint(10, 100) for _ in range(55)]
num_cat_1 = 5  #Categorias

#L2
lista_2 = [20, 25, 30, 25, 40, 20, 35, 45, 40, 22]
num_cat_2 = 3  
#L3
print("--- Configuração do Histograma 3 (Input do Usuário) ---")
num_input = int(input("Digite um número para adicionar à terceira lista: "))
lista_3 = [50, 60, 70, 80, 90, num_input]
num_cat_3 = 4  

#Contabilizar os totais de qualquer lista
def contabiliza_totais(nums, num_cat):
    num_min = min(nums)
    num_max = max(nums)
    # Evitar dividir por zero 
    if num_max == num_min:
        tam_cat = 1
    else:
        tam_cat = (num_max - num_min) / num_cat
        
    lista_total = [0] * num_cat

    for i in range(len(nums)):
        if nums[i] == num_max:
            lista_total[-1] += 1
            continue

        for i_cat in range(num_cat):
            lim_inf = num_min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            if lim_inf <= nums[i] < lim_sup:
                lista_total[i_cat] += 1
                break
    return lista_total
#Processar infos de três listas
totais_1 = contabiliza_totais(lista_1, num_cat_1)
totais_2 = contabiliza_totais(lista_2, num_cat_2)
totais_3 = contabiliza_totais(lista_3, num_cat_3)
#Desenhar os histogramas
def draw_histogram(screen, totais, pos_x, pos_y, cor, titulo):
    #Eixos X e Y 
    pygame.draw.line(screen, (0, 0, 0), (pos_x, pos_y), (pos_x + 220, pos_y), 2)  
    pygame.draw.line(screen, (0, 0, 0), (pos_x, pos_y), (pos_x, pos_y - 180), 2)  
    #Desenhar as marcações e as barras de cada categoria
    for i in range(len(totais)):
        x = pos_x + 20 + (i * 35)
        h = 12 * totais[i] #Altura barra
        
        #Desenha a barra do histograma
        pygame.draw.rect(screen, cor, (x, pos_y - h, 25, h))
        
        #Marcação no eixo X
        pygame.draw.line(screen, (0, 0, 0), (x + 12, pos_y), (x + 12, pos_y + 5), 2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Branco(COR DEFUNDO)
    screen.fill((255, 255, 255))

    #Desenha os 3histogramas 
    #Histograma 1(Aleatório-azul)
    draw_histogram(screen, totais_1, pos_x=50, pos_y=320, cor=(0, 0, 255), titulo="H1")
    #Histograma 2(Estático-verde)
    draw_histogram(screen, totais_2, pos_x=350, pos_y=320, cor=(0, 200, 0), titulo="H2")
    #Histograma 3(Input do Usuário-roxa)
    draw_histogram(screen, totais_3, pos_x=650, pos_y=320, cor=(150, 0, 150), titulo="H3")

    pygame.display.update()
