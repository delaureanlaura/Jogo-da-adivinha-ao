import random
def jogar_adivinhacao():
    print('**********************************', end= '\n')
    print('Bem vindo/a ao jogo de adivinhação', end= '\n')
    print('**********************************', end= '\n')
    nmr_secreto = random.randrange(1,100)
    int(nmr_secreto)

    total_de_tentativas= 0
    ponto_total = 1000

    print('Qual nível de dificuldade você deseja? ', end="\n")
    print('(1) Fácil')
    print('(2) Mediano')
    print('(3) Difícil')
    dificuldade = int(input('Digite o nível de dificuldade: '))


    if(dificuldade == 1):
        total_de_tentativas = 20
    elif(dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print('tentativa {0} de {1}'.format(rodada, total_de_tentativas))
        numero = input('Digite sua alternativa para numero secreto: ')
        numero = int(numero)

        if(numero > 100 or numero < 1):
            print('INVALIDO NUMEROS MENORES QUE 1 E MAIORES QUE 100')
            continue

        if(numero == nmr_secreto):
            print('parabéns!!!, você acertou e fez {} pontos!!!'.format(ponto_total))
            break
        else:
            if(numero < nmr_secreto):
                print('Você digitou um numero menor')
            elif(numero > nmr_secreto):
                print('Você digitou um numero maior')
        pontos_perdidos = abs(nmr_secreto - numero)
        ponto_total = ponto_total - pontos_perdidos

if(__name__ == '__main__'):
    jogar_adivinhacao()
