from turtle import *
from random import randint

t = Turtle()

def draw_quadrado(x, y, lado):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.color("black")

    cor = textinput("Escolha da cor", "Digite a cor da próxima forma:")
    t.fillcolor(cor)

    t.begin_fill()

    for cont in range(4):
        t.fd(lado)
        t.lt(90)

    t.end_fill()


x = randint(100, 300)
y = randint(0, 350)

draw_quadrado(x, y, 100)

def draw_quadrado2(x, y, lado):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.color("black")

    cor = textinput("Escolha da cor", "Digite a cor da próxima forma:")
    t.fillcolor(cor)

    t.begin_fill()

    for cont in range(4):
        t.fd(lado)
        t.lt(90)

    t.end_fill()


x = randint(-300, -100)
y = randint(0, 350)

draw_quadrado2(x, y, 100)

def draw_quadrado3(x, y, lado):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.color("black")

    cor = textinput("Escolha da cor", "Digite a cor da próxima forma:")
    t.fillcolor(cor)

    t.begin_fill()

    for cont in range(4):
        t.fd(lado)
        t.lt(90)

    t.end_fill()


x = randint(-300, -100)
y = randint(-350, 0)

draw_quadrado3(x, y, 100)

def draw_quadrado4(x, y, lado):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.color("black")

    cor = textinput("Escolha da cor", "Digite a cor da próxima forma:")
    t.fillcolor(cor)

    t.begin_fill()

    for cont in range(4):
        t.fd(lado)
        t.lt(90)

    t.end_fill()


x = randint(100, 300)
y = randint(-350, 0)

draw_quadrado4(x, y, 100)



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







