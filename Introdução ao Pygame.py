from pygame import *

#Estrutura padrão para toda vez que for rodar PyGame
init()
screen =  display.set_mode((800, 600))

#Inicio da nuvem
nuvem_x = 430
#ESPAÇO DO RECURSOS (BATMAN)
#ev é a nova variável event, pq o event já existe
running = True
while running == True:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

   #desenhar os elementos na tela
   #screen.fill((151, 209, 250))
    screen.fill("#97D1FA")


    #sixtaxe linha(espessa): (aonde(tela), cor, começo(x,y), raio)
    #RAIOS DE SOL
    draw.line(screen, "#FFF251", (20,20),(180,180), 8)
    draw.line(screen,"#FFF251", (20,180),(180,20), 8)
    draw.line(screen,"#FFF251", (100,5),(100,195), 8)
    draw.line(screen,"#FFF251", (5,100),(195,100), 8)
    #SOL
    draw.circle(screen, "#FFF251",(100,100),50)
    #sintaxe círculo: (aonde(tela), cor, centro(x,y), raio)
    #sintaxe retângulo: (x, y, largura, altura):
    #GRAMA
    draw.rect(screen, "#489D25", (0,500,800,100))
    #CASA
    draw.rect(screen, "#646464", (100, 300, 200, 200))
    #JANELA AZUL
    draw.rect(screen, "#0D1764", (120, 380, 50, 70))
    #PORTA MARROM
    draw.rect(screen, "#784D1A", (200, 360, 70, 140))
    #MAÇANETA
    draw.circle(screen,"#000000",(215,430),7)
    #TELHADO
    draw.polygon(screen, "#F2883B",((100,300),(200,200),(300,300)))
    #MADEIRA DA ÁRVORE
    #draw.rect(screen,"#784D1A",(400,405),50,95)
    draw.rect(screen, "#784D1A", (510, 355, 50, 145))
    #FOLHAS DA ÁRVORE
    draw.circle(screen,"#479C25",(535,320),80)
    #sintaxe polígono: (aonde(tela), cor, centro(x,y), raio)
    #imagens
    # NUVEM
    draw.circle(screen, "#FFFFFF", (int(nuvem_x), 100), 45)
    draw.circle(screen, "#FFFFFF", (int(nuvem_x) + 50, 100), 45)
    draw.circle(screen, "#FFFFFF", (int(nuvem_x) + 100, 100), 45)
    draw.circle(screen, "#FFFFFF", (int(nuvem_x) + 150, 100), 45)

    #Movimentar a nuvem
    nuvem_x += 0.2

    # TELEPORTE: Volta para a posição inicial (430) assim que sai da tela (800)
    if nuvem_x > 800:
        nuvem_x = 430

    
    display.update()

#para retângulo é preciso (x,y, width, height)
#pyGame, (0,0) em cima na esquerda, e y cresce pra baixo
#sixtaxe linha(espessa): (aonde(tela), cor, começo(x,y), raio)
