"""4. Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

try:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a quarta nota: '))
    media = (n1 + n2 + n3 + n4) / 4
    print(media)
except (ValueError, NameError):
    print('Por favor, digite um valor inteiro ou real')