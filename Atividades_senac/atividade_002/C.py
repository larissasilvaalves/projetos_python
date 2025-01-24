# A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de velocidade 
#para ajudar a promover a segurança nas estradas. Eles precisam de um programa que 
#Permita aos usuários inserir a velocidade de um carro e, em seguida, exibir na tela uma 
#mensagem adequada com base na velocidade fornecida. O objetivo principal é alertar os 
#motoristas caso ultrapassem o limite de velocidade de 60 km/h, incentivando-os a dirigir
# dentro dos limites legais e, assim, reduzir o risco de acidentes.

import os

os. system('cls')

velocidade =float(input('introduza a velocidade do veículo: '))

if 60 > velocidade :
    resposta = f'{velocidade} não ultrapassou {60}'
    
if 60 < velocidade :
    resposta = f'{velocidade} não ultrapasou o limite de {60}'
#saída
    print('-'*70)
    print(resposta)

