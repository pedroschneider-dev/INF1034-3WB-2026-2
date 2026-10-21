from turtle import *
from random import randint
t = Turtle()

#Retornar cor aleatória
def randomColor():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

#desenhar quadrado
def drawSquare(t, size):
    # t.goto(x, y) 
    t.pd()
    t.begin_fill() 
    t.fillcolor(randomColor()) 
    for i in range(4):  #4 lados
        t.fd(size) 
        t.right(90) 
    t.end_fill() 
    t.pu() 

#desenhar o fractal de chifre
def drawSquareFractal(t, size, step=50):
    if step < 0 or size < 1: 
        return
    t.pd()
    t.fd(size / 1.5) #reduzindo o passo
    t.lt(10) 
    drawSquare(t, size) #desenhar o quadrado na posição atual
    drawSquareFractal(t, size - 1, step - 1) #diminuindo o tamanho e os passos

# desenhar uma espiral geométrica
def drawSpiral(t):
    for i in range(40): # 40 voltas
        t.fd(i * 1.5) # compactar a espiral
        t.lt(15) # curvar a espiral



#fractal de árvore
def treeFractal(t, size, angle, nivel):
    if size < 40: 
        return
    t.pd() 
    t.fd(size) 
    #ramo direito da árvore
    t.rt(angle) 
    t.fd(size) 
    treeFractal(t, size * 0.8, angle, nivel - 1) 
    t.back(size) #tartaruga na base do galho 

    pencolor(0, 255 // nivel, 0) #cor da caneta variando com o nível da árvore

    #esquerdo 
    t.lt(2 * angle)
    t.fd(size) 
    treeFractal(t, size * 0.8, angle, nivel - 1)
    t.back(size) 
    pencolor(0, 255 // nivel, 0) 
    t.lt(-angle) 
    t.back(size) #tartaruga na origem do tronco principal

colormode(255)
t.speed(0) #Velocidade máxima 
t.pu() 

#desenhando o chifre 
t.goto(-350, -200) 
t.pd() 
drawSquareFractal(t, 40, 35) # Tamanho e passos reduzidos
t.pu() 

## Desenhando a árvore central (Maior e destacada)
t.goto(0, -100) 
t.setheading(90) 
treeFractal(t, 100, 35, 15) 
t.pu()

#Desenhando a espiral 
t.goto(250, -150) 
t.pd() 
drawSpiral(t) 
t.pu()

#corrigi o bug de uma setinha perdida no meio da tela
t.hideturtle()

mainloop()
