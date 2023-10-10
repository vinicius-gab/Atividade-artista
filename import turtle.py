import turtle
leo = turtle.Turtle()
 
# desenhar quadrado
def desenhar_quadrado():
    for _ in range(4):
        leo.forward(10)
        leo.right(90)

desenhar_quadrado()