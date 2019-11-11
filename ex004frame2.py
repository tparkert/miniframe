import os
from math import hypot, sqrt
def boasVindas():
    print('')
    print('####################################')
    print('##  Bem Vindo ao Peter Framework  ##')
    print('####################################')
    print('')
    os.system('PAUSE')
    os.system('cls')

def calculadora():
    os.system('cls')
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    soma = float(n1)+float(n2)
    sub = float(n1)-float(n2)
    mult = float(n1)*float(n2)
    div = float(n1)/float(n2)
    exp = float(n1)**float(n2)
    mod = float(n1)%float(n2)
    med = (float(n1)+float(n2)/2)

    os.system('cls')
    print('A soma entre {} e {} é: {}'.format(n1,n2,soma))
    print('A subtração entre {} e {} é: {}'.format(n1,n2,sub))
    print('A multiplicaão entre {} e {} é: {}'.format(n1,n2,mult))
    print('A divisão entre {} e {} é: {}'.format(n1,n2,div))
    print('A exponenciação entre {} e {} é: {}'.format(n1,n2,exp))
    print('A divisão de módulo entre {} e {} é: {}'.format(n1,n2,mod))
    print('A média aritimética entre {} e {} é: {}'.format(n1,n2,med))

    print('')

def help():
    os.system('cls')
    print('Os comandos disponíveis são: ')
    print('')
    mostrarComandos()

def mostrarComandos():
    print("'help' - Comandos disponíveis")
    print("'calculadora' - Calculadora com multi resultados")
    print("'pitagoras' - Teorema de Pitágoras")
    print("'raiz' - Raiz Quadrada")
    
    print("'exit' - Sair")
    print('')
    

def comando():
    cmd = input('Digite o comando: ')
    split = cmd.split()
    return split

def limparTela():
    os.system('cls')

def pitagoras():
    os.system('cls')
    print('1. Sim')
    print('2. Não')
    print('')
    hipQuestion = input('Você tem o valor da hipotenusa? (valor de a): ')
    limparTela()

    if hipQuestion == '1':
        a = float(input('Digite o valor da hipotenusa: '))
        b = float(input('Digite o valor de um dos catetos: '))
        r = (a**2 - b**2) ** (1/2)
        os.system('cls')
        print('O valor do segundo cateto é: {0:.2f}'.format(r))
        
    elif hipQuestion == '2':
        b = input('Digite o valor do primeiro cateto ')
        c = input('Digite o valor do segundo cateto ')
        r = hypot(float(b), float(c))
        print(r)
    else:
        print('opção incorreta')

def raizQuadrada():
    a = float(input('Diga o valor para saber sua raiz quadrada: '))
    r = sqrt(a)
    limparTela()
    print('A raiz quadrada de {} é: {}'.format(a,float(r)))

boasVindas()
mostrarComandos()

while True:
    
    cond = comando()
    if cond[0] == 'help':
        help()
    elif cond[0] == 'exit':
        os.system('exit')
        exit()
    elif cond[0] == 'calculadora':
        calculadora()
    elif cond[0] == 'pitagoras':
        pitagoras()
    elif cond[0] == 'raiz':
        raizQuadrada()
    else:
        print('Comando incorreto')
        print('')


