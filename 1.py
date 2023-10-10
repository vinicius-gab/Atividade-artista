import turtle 
num_lados = int(input("Digite um número:"))
if num_lados < 3:
    print("Digite um número maior ou igual a 3")
else:
    angulos = 360 / num_lados
    vic = turtle.Turtle()
for i in range(num_lados):
    vic.forward(100)
    vic.left(angulos)