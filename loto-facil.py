# Módulos
from random import randint
from time import sleep

# Lista
lista = list()

# Jogos
jogos = list()

# Titulo
print('-' * 30)
print('         JOGA NA LOTO FÁCIL         ')
print('-' * 30)

# Pergunta
quantidade = int(input('Quantos jogos quer sortear? '))
""" Quantidade de jogos. """
total = 1

# Sorteio
while total <= quantidade:
    contagem = 0
    """ Contagem de jogos. """
    while True:
        """ Sorteio de números. """
        numero = randint(1, 25)
        if numero not in lista:
            """ Verifica se o número já existe. """
            lista.append(numero)
