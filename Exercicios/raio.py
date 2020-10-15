'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
from math import pi

raio = float(input("Entre com o raio "))

area = pi*(raio**2)

print(f'{area:.3f}')
print(pi)
