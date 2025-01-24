import os 

os.system('cls')

def quiz_carro():
    print("Bem-vindo ao quiz Amor, vamos testar seu conhecimento sobre carros!\n")
    
   
    print("Vamos testar seus conhecimentos sobre como um carro funciona!\n")
    
    # Pergunta 1: Função do motor
    resposta_1 = input("Qual é a principal função do motor de um carro? \n(a) Gerar eletricidade \n(b) Movimentar o carro \n(c) Controlar a temperatura do carro\nEscolha a opção correta (a, b, c): ").lower()
    if resposta_1 == "b":
        print("Correto! O motor tem a função principal de movimentar o carro, gerando energia mecânica a partir da queima de combustível ou eletricidade.")
    else:
        print("Errado! A função principal do motor é movimentar o carro.\n")
    
    # Pergunta 2: Sistema de transmissão
    resposta_2 = input("\nO que é a transmissão de um carro? \n(a) Sistema que controla os faróis \n(b) Sistema que ajuda o carro a mudar de marcha \n(c) Sistema de controle de temperatura\nEscolha a opção correta (a, b, c): ").lower()
    if resposta_2 == "b":
        print("Correto! A transmissão é responsável por transferir a potência do motor para as rodas, permitindo que o carro mude de marcha e se movimente a diferentes velocidades.")
    else:
        print("Errado! A transmissão é o sistema que ajuda o carro a mudar de marcha e transferir potência para as rodas.\n")
    
    # Pergunta 3: Tipos de combustível
    resposta_3 = input("\nQual dos seguintes combustíveis é usado em carros elétricos? \n(a) Gasolina \n(b) Etanol \n(c) Eletricidade\nEscolha a opção correta (a, b, c): ").lower()
    if resposta_3 == "c":
        print("Correto! Carros elétricos usam eletricidade para alimentar motores elétricos, ao invés de combustível tradicional.")
    else:
        print("Errado! Carros elétricos usam eletricidade como combustível.\n")
    
    # Pergunta 4: Função dos freios
    resposta_4 = input("\nQual é a principal função do sistema de freios? \n(a) Melhorar o desempenho do motor \n(b) Diminuir a velocidade ou parar o carro \n(c) Ajustar a suspensão\nEscolha a opção correta (a, b, c): ").lower()
    if resposta_4 == "b":
        print("Correto! O sistema de freios é responsável por diminuir a velocidade ou parar o carro, aplicando força nas rodas para desacelerar o veículo.")
    else:
        print("Errado! O sistema de freios tem a função de diminuir a velocidade ou parar o carro.\n")
    
    # Pergunta 5: Função da suspensão
    resposta_5 = input("\nO que é a função da suspensão de um carro? \n(a) Suavizar o impacto com o solo e melhorar o conforto\n(b) Controlar a temperatura do motor\n(c) Ajudar na direção do carro\nEscolha a opção correta (a, b, c): ").lower()
    if resposta_5 == "a":
        print("Correto! A suspensão ajuda a suavizar os impactos com o solo, proporcionando uma condução mais confortável e controlada.")
    else:
        print("Errado! A suspensão serve para suavizar os impactos com o solo e proporcionar mais conforto.\n")
    
    print("\nFim do quiz! Espero que tenha aprendido mais sobre o funcionamento dos carros. Até a próxima!")

    resposta_6 = input('\nO que faz o sensor de oxigênio no sistema de escapamento de um carro? \n(a) Controla a quantidade de combustível injetado no motor\n(b)Mede a eficiência do catalisador\nDetecta falhas no sistema de ignição').lower()
    if resposta_6 == 'a':
        print('Correto! O sensor de oxigênio mede a quantidade de oxigênio nos gases de escapamento e ajusta a quantidade de combustível injetado no motor.')
    else:
        print('Errado! Errado! O sensor de oxigênio controla a quantidade de combustível injetado no motor.\n')

    resposta_7 = input('\nO que é o "turbo lag" em um carro com motor turboalimentado? \n(a) O atraso entre a aceleração e o aumento de potência do motor \n(b) A demora no acionamento do ar-condicionado \n(c)O tempo que leva para o motor parar quando o carro desliga\nEscolha a opção correta (a, b, c): ')
    if resposta_7 == "a":
        print("Correto! O turbo lag é o atraso entre a aceleração e o aumento de potência, devido ao tempo necessário para o turbo atingir a pressão ideal.")
    else:
          print("Errado! O 'turbo lag' é o atraso entre a aceleração e o aumento de potência do motor.\n")

    
# Chama a função para iniciar o quiz
quiz_carro()
