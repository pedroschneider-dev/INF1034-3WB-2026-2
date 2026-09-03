from turtle import *
from random import randint

# Plano cartesiano
def draw_plano_cartesiano():
    t.pu()
    t.color("gray")
    t.goto(-400, 0)      # eixo X
    t.pd()
    t.goto(400, 0)
    t.pu()
    t.goto(0, -400)      # eixo Y
    t.pd()
    t.goto(0, 400)
    t.pu()
    t.color("black")

#Função genérica para polígonos
def draw_poligono(x, y, lado, n_lados, cor):
    angulo = 360 / n_lados
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color("black")
    t.fillcolor(cor)
    t.begin_fill()
    for cont in range(n_lados):
        t.fd(lado)
        t.lt(angulo)
    t.end_fill()

# ---------- Função genérica: círculo (centro = x, y) ----------
def draw_circulo(x, y, raio, cor):
    t.pu()
    t.goto(x, y - raio)   
    t.pd()
    t.color("black")
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

# ---------- Desenha o plano ----------
draw_plano_cartesiano()

lado = 60  # lado pequeno o suficiente que cabe em cada quadrante

# Quadrante 1 (x>0, y>0): pentágono
x = randint(50, 200)
y = randint(50, 200)
draw_poligono(x, y, lado, 5, "red")

# Quadrante 2 (x<0, y>0): hexágono
x = randint(-300, -150)
y = randint(50, 200)
draw_poligono(x, y, lado, 6, "blue")

# Quadrante 3 (x<0, y<0): heptágono
x = randint(-300, -150)
y = randint(-300, -150)
draw_poligono(x, y, lado, 7, "green")

# Quadrante 4 (x>0, y<0): octógono
x = randint(50, 200)
y = randint(-300, -150)
draw_poligono(x, y, lado, 8, "orange")


# FUNÇAO ANTIGA 
t.pu()
t.goto(0,0)
t.pd()

t.pu()
t.goto(-400, 0)
t.pd()
t.goto(400, 0)
t.stamp()

t.pu()
t.goto(0, -400)
t.pd()
t.goto(0, 400)
t.lt(90)
t.stamp()
t.rt(90)

t.goto(0,0)
for cont in range(4):
    print(cont)
    t.fd(100)
    t.lt(90)



mainloop()
