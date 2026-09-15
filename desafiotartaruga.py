from turtle import *
from random import randint

def corrida(n):
    tartarugas = []

    cores = ["red", "blue", "green", "yellow", "purple",
             "orange", "pink", "brown", "cyan", "black"]

    for i in range(n):
        t = Turtle()
        t.shape("turtle")
        t.speed(1)
        t.pu()
        t.color(cores[i % 10])
        t.goto(-200, 100 - i * 30)

        tartarugas.append(t)

    for num in range(30):
        for t in tartarugas:
            t.fd(randint(5, 10))


n = int(input("Digite o número de tartarugas: "))

corrida(n)

mainloop()

mainloop()
