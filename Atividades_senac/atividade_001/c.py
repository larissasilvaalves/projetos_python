#imports
import os

os.system ('cls')

print('-'*70)
print('NOTA DOS ALUNOS')
print('='*70)

nota1 = float(input(' 1° nota: ' ))
nota2 = float(input(' 2° nota: ' ))
nota3 = float(input(' 3° nota: '))
nota4 = float (input(' 4 nota: '))

#processamento
media = nota1 + nota2 + nota3 + nota4 / 4
media_correta = (nota1 + nota2 + nota3+ nota4) / 4

print( '----notas-----')
print(f'nota1 : {nota1} | nota 2 {nota2} |'
      f'' )
print('-'*70)
print(f'MEDIA DE NOTAS : {media} ')
print(f'MEDIA CORRETA DAS NOTAS: {media_correta}')
print('='*70)
