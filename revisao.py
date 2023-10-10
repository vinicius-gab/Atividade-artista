import turtle 
leo=turtle.Turtle
vars =input("digite um numero para a quantidade de lados do poligono: ")
def desenhar_poligono(vars):
    for _ in range(vars):
        for _ in range(vars):
            leo.forward(50)
            leo.right(60)
            leo.forward(50)
