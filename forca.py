## Júlia Wonsick Pazzinatto RA: 1136562  e Isabelle Waltrick Pozzobon RA: 1136872 -  Jogo da Forca

import os,time
os.system("cls")
while True:

    #criando váriaveis 
    palavraSecreta = ""
    letrasCorretas = []
    letrasErradas = []
    dicas = []
    erros = 0 

    # dar boas vindas e pedir o nome e do competidor 
    print("Seja bem vindo ao Jogo da Forca!")
    
    input("Pressione qualquer tecla para continuar...")
    os.system("cls")

    nomeDesafiante = input("Nome do desafiante: ")
    nomeCompetidor = input("Nome do competidor: ")
    time.sleep(3)
    os.system("cls")

    #informações do desafiante
    palavra = input("Digite a palavra secreta: ")
    palavraSecreta = "* " * len(palavra)

    vezesDicas = 1
    
    while vezesDicas <= 3:
        dica = input(f"Informe a dica número {vezesDicas}: ")
        dicas.append(dica)
        vezesDicas += 1

    os.system("cls")

    # iniciando o loop do jogo
    while palavraSecreta != palavra:
        print("Palavra secreta: ", palavraSecreta)

        opcao = int(input("Escolha entre jogar: 1 ou pedir dica 2: "))
        print("")
        if opcao == 1: 
            letra = input("Digite uma letra para verificar se está na palavra secreta: ").lower()
            if letra in palavra:
                print("Parabéns! Você acertou a letra!")
                print("")

                letrasCorretas.append(letra)
                # Atuliza a palavra secreta com as letras corretas adivinhas
                palavraSecreta = "".join([letra if letra in letrasCorretas else "_ " for letra in palavra ])
            else:
                print("Ops!Letra errada")
                letrasErradas.append(letra)
                s = "-"
                erros = erros + 1
                print(s.join(letrasErradas))
                if erros == 6:
                    print("Você perdeu!")
                    break
        elif opcao == 2:
            if len(dicas) > 0:
                print("Dica:", dicas.pop(0))
            else:
                print("Você utilizou todas as dicas disponíveis!")
        else:
            print("Opção inválida!")

    if palavraSecreta == palavra: 
        print(f"Parabéns {nomeCompetidor}! Você descobriu a palavra secreta {palavraSecreta}!")
        print(f"{nomeDesafiante} não foi dessa vez!")
    else:
        print(f"Que pena! {nomeCompetidor}! Você não descobriu a palavra secreta, a palavra era: {palavraSecreta}!")
        print(f"{nomeDesafiante} você é o vencedor!")


    opcoesFinais = input("Digite 1 para jogar novamente ou 2 para sair: ")
    if opcoesFinais == "1" :
        print("Reiniciando o jogo...")
        time.sleep(3)
        os.system("cls")

    else:
        opcoesFinais == "2" 
        quit()
