import os 

os.system('cls')

#dicionario

material_escolar = {
    
    'caderno' : 'utilizado para fazer registros de atividades dentro de sala.',
    'Lápis' : 'é um instrumento utilizado para escrever, desenhar, pintar.',
    'bolsinha' : 'ela serve para armazenar objetos, itens; como canetas, lápis e marcadores.',
    'borracha' : 'ela é usada para apagar anotações, desemhos ou outos tipos de coisas',
    'régua'    : 'Usada para medir, traçar linhas retas e medir distâncias pequenas'
                 }


print('')
print('-'*70)
print(f'Lista de material escolares: {material_escolar}')
print('-')

#menu
print('')

while True:

    print('-'*70)
    print('\nMenu de opções')
    print('1.Trocar a descrição de algum, objeto')
    print('2.Ordenar o dicionário em ordem alfabetica')
    print('3.Criar um relatorio sobre o dicionário')
    print('4.Sair')
    print('='*70)


    opcao = input('Escolha umas das opções(1-4): ')



    if opcao == '1':

        chave = input('Escolha um dos itens para mudar na lista: ')

        nova_descrição = input('Escreva a nova decrição: ')


        if chave in material_escolar:

                material_escolar[chave] = nova_descrição

                print(f'sua lista foi atualizada: {material_escolar}')
        
        else:
             print('sua cor não foi encontrada')

    if opcao == '2':
         
            chaves_alfabeticas = sorted(material_escolar.items())
            print(chaves_alfabeticas)

    
    if opcao == '3':
           
        print('Saiu do programa!')
        break
          

          
        
        
          







    
    

