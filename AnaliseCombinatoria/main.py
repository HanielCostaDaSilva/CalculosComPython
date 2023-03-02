#== == == == bibliotecas
from AnaliseCombinatoria import * 
import os

#== == == == Funções
def MostrarOpcoes(Dicionario):
    Opcoes= ''
    for key in Dicionario.keys():
        Opcoes+= f'|{key}| {Dicionario[key]}\n'
    return Opcoes

#== == == == Váriaveis
separador='=+'*30
#== == == Dicionario e Lista contendo as possíveis operações Combinatorias
 
opcoesCabiveisDicionario={
    '1':'Permutação Simples',
    '2': 'Permutação Circular',
    '3': 'Arranjo Simples',
    '4': 'Arranjo com Repetição',
    '5': 'Combinação Simples',
    '-': 'Encerrar o programa'
}

opcoesCabiveisList= list(opcoesCabiveisDicionario.keys())
print(separador)
print("Bem vindo ao teste de combinações!")
#== == == == Main em execução
while True:

    try:
        print(separador,'\n')
        print(MostrarOpcoes(opcoesCabiveisDicionario)) # È mostrada todas as opções cabíveis ao usuário
        print(separador)
        
        escolha= input("\nescreva a operação desejada através do indíce: \n")
        print(f'opção: |{escolha}| {opcoesCabiveisDicionario[escolha]} foi escolhida.')
        
        if (escolha == opcoesCabiveisList[0]): #Permutação simples escolhida
            print(" ")
            n=int(input("Digite o número de elementos: (n) "))
            resultado=PermutacaoSimples(n)

        elif(escolha==opcoesCabiveisList[1]): #Permutação circular escolhida
            print(" ")
            n=int(input("Digite o número de elementos: (n) "))   
            resultado=PermutacaoCircular(n)

        elif(escolha== opcoesCabiveisList[2]): #Arranjo simples escolhida
            n=int(input("Digite o número de elementos: (n) "))
            p=int(input("Digite o número de termos do conjunto: (p) "))
            resultado=ArranjoSimples(n,p)

        elif(escolha==opcoesCabiveisList[3]): #Arranjo com repetição escolhida
            print(" ")
            n=int(input("Digite o número de elementos: (n) "))
            p=int(input("Digite o número de termos do conjunto: (p) "))
            resultado= ArranjoComRepeticao(n,p)
            

        elif(escolha==opcoesCabiveisList[4]): # Combinação Simples
            print(" ")
            n=int(input("Digite o número de elementos: (n) "))
            p=int(input("Digite o número de termos do conjunto: (p) "))
            resultado=CombinacaoSimples(n,p)
    
        else:
            break
        print(separador)
        print(f'o resultado da análise combinatória por {opcoesCabiveisDicionario[escolha]} foi: {resultado} ')
        print(separador)
        input('Pressione "Enter" para continuar')
        
    except IndiceInvalidException as IIE :
        print(separador)
        print(IIE)
        print(separador)
        input('Pressione "Enter" para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')

    except KeyError as KE :
        print(separador)
        print('O índice inserido não está presente nas escolhas cabíveis!')
        print(separador)
        input('Pressione "Enter" para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')

    except ValueError as VE:
        print(separador)
        print('O valor Digitado não foi um número inteiro!')
        print(separador)
        input('Pressione "Enter" para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')


    except Exception as E:
        print(separador)
        print(E)
        print(separador)
        input('Pressione "Enter" para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')


input("aperte a tecla 'Enter' para finalizar... ")