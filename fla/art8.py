import turtle
leo = turtle.Turtle()
def jump(a):
    leo.up()
    leo.forward(a)
    leo.down()
def desenha_flor():
    for _ in range(6):
        for _ in range(8):
            leo.forward(20)
            leo.right(30)
        leo.right(60)
for i in range(3):
    desenha_flor()
    jump(150)

