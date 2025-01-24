import os 

os.system('cls')


meu_dicionario = ["Exaltasamba" , 
                  "Grupo revelação",
                  "Turma do pagode",
                  "Grupo Menos é Mais"]
print(meu_dicionario)


responda = str(input('Deseja acrescentar mais algum grupo de pagode(s/n)?: '))


if responda == "s":

    adicione = input('Entre com o nome que deseja adicionar: ')
    meu_dicionario.append(adicione)
    print(meu_dicionario)

else:
    print(F'Nada foi adicionado!')