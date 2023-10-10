import turtle
leo = turtle.Turtle()
def desenha_flor():
    for i in range(12):
        for i in range(2):
            leo.forward(60)
            leo.right(30)
            leo.forward(60)
            leo.right(150)
        leo.right(30)    
desenha_flor()