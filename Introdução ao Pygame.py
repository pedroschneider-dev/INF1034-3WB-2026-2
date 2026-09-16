from pygame import *

#Estrutura padrão para toda vez que for rodar PyGame
init()
screen =  display.set_mode((800, 600))

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
    
   


    #GRAMA
    draw.rect(screen, "#489D25", (0,500,800,100))
    draw.circle(screen, "#FFF251",(100,100),50)
    #sintaxe círculo: (aonde(tela), cor, centro(x,y), raio)
    draw.polygon(screen, "#F2883B",((100,300),(200,200),(300,300)))
    #sintaxe polígono: (aonde(tela), cor, centro(x,y), raio)
    #imagens
    
    display.update()


#para retângulo é preciso (x,y, width, height)
#pyGame, (0,0) em cima na esquerda, e y cresce pra baixo
#sixtaxe linha(espessa): (aonde(tela), cor, começo(x,y), raio)