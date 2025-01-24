import os 
os.system('cls')

print('-'*70)
print('fatiamento de strings')
('='*70)

frase = "amo meu cacheado"

#exibindo a string original 
print(f'string original: {frase}')

#fatiiamento : acessando partes especificas de string
#primeiro cinco caracteres 
primeiros_cinco = frase [:5]
print(f'primeiros cinco caracteres: {primeiros_cinco}')

# ultimos dez caracteres
ultimo_dez = frase [-10:]
print(f'ultimos dez caracteres: {ultimo_dez}')

#do quarto ao décimo caractere
quarto_ao_decimo = frase [3:10]
print(f'do qaurto ao décimo caractere: {quarto_ao_decimo}')

# a cada dois caracteres 
a_cada_dois = frase [::2]
print(f'A cada dois caracteres: {a_cada_dois}')

# invertendo a string
invertida = frase [::-1]
print(f'string invertida : {invertida}')
print()