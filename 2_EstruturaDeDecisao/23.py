"""
23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma
função de arredondamento.
"""

n = float(input('Digite um número: '))
if n == round(n):
    print('É um número inteiro!')
else:
    print('É um decimal!')