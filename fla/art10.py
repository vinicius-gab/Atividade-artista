import turtle
leo = turtle.Turtle()
def desenho():
    for i in range(5):
        for i in range(2):
            leo.forward(75)
            leo.back(50)
            leo.right(60)
            leo.forward(50)
desenho()