#Importação das funções utilizadas no código
from random import randint
from time import sleep

print('{:=^40}'.format('JOKENPÔ'))

#Definindo os itens
itens = ('Pedra', 'Papel', 'Tesoura')

#Jogada do computador
computador = randint(0, 2)

#Apresentar as opções ao jogador
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

#Jogador faz a jogada
jogador = int(input('Sua jogada: '))
if jogador not in (0, 1, 2): #Se o jogador jogar algo diferente de 1, 2 ou 3 o programa para e mostra a mensagem abaixo
    print('Jogada inválida, tente novamente!')
    exit()

#Programa simula um Jokenpô digital, como nós acostumamos a falar: (JO-KEEEEEN-PÔ!)
print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PÔ')
sleep(0.6)
print('-=' * 14)

#Mostrando o que cada um jogou
print('Computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}' .format(itens[jogador]))
print('-=' * 14)

#Montar as estruturas condicionais para vitória de um dos lados ou empate
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Ganhou!')
    elif jogador == 2:
        print('Perdeu!')

if computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('Perdeu!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Ganhou!')

if computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('Ganhou!')
    elif jogador == 1:
        print('Perdeu!')
    elif jogador == 2:
        print('Empate!')
