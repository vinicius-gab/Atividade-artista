import turtle
leo = turtle.Turtle()
def jump(a):
    leo.up()
    leo.forward(a)
    leo.down()
def forma():
    for i in range(6):
        leo.forward(25)
        leo.right(60)
for i in range(6):
    for i in range(2):
        for i in range(4):
            forma()
            jump(75)
        leo.back(25)
        leo.right(60)
        jump(25)
        leo.right(120)
    leo.back(25)
    leo.left(60)
    jump(50)
    leo.right(60)    