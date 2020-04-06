# -*- coding: utf-8 -*-

import turtle

def main():
    window = turtle.Screen()
    mauricio = turtle.Turtle()

    make_square(mauricio)

    turtle.mainloop()

def make_square(mauricio):
    length = int(input("Tamaño de cuadrado: "))
    
    for i in range(4):
        make_line_and_turn(mauricio, length)

def make_line_and_turn(mauricio, length):
    mauricio.forward(length)
    mauricio.left(90)

if __name__=="__main__":
    main()
    