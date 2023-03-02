import os

from calcularFrequencia import * 

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
    '1':'Gerar tabela de Frequência sem classes',
    '2':'Gerar tabela de Frequência com classes',
    '3':'Instruções de Uso do programa',
    '-':'Finalizar o Programa'
}

opcoesCabiveisChaves= list(opcoesCabiveisDicionario.keys())

os.system('cls' if os.name == 'nt' else 'clear')

print(separador)
input("Bem vindo Ao gerador de Tabaleas de frequência!")
print(separador)

        
flag=True #variável responsável pelo laço do algorítimo

while flag:
    try: 
        print(MostrarOpcoes(opcoesCabiveisDicionario))

        escolha=input('Digite a opção que desejas execultar: ')
                        
        if escolha==opcoesCabiveisChaves[0]:#'1':'Gerar tabela de Frequência sem classes'
            arquivoDadosCaminho= os.path.expanduser('./dadosQuantitativosDiscretos.txt')
            #arquivoDadosCaminho= 'dadosQuantitativosDiscretos.txt'#os dados serão coletados de um arquivo de texto
            tabelaArquivoCaminho=os.path.expanduser('./tabelaFrequenciaSemClasses.txt')        
            
            print(separador)
            print('Por favor, digite os dados em um arquivo de texto no seguinte caminho: \n',arquivoDadosCaminho)
            input('Aperte "enter" quando tiver inserido todos os dados no arquivo em questão...')
            
            #== == !! !! Leitura dos dados quantitativos discretos
            dados=open(arquivoDadosCaminho,'r')
            dadosSeparados=dados.readlines()
            dados.close()
            #== == !! !! Criação da tabela
            tabela= calcularfrequenciaSemClasse(dadosSeparados)

            #== == Geração do arquivo contendo a tabela
            arquivoTabela=open(tabelaArquivoCaminho,'w')
            arquivoTabela.writelines(montarTabelaParaArquivos(tabela))
            arquivoTabela.close()
            
            print(separador)
            print(f'Sua tabela foi gerada com êxito!\nVocê pode acessar através do seguinte caminho: {tabelaArquivoCaminho}')
            print(separador)

            input('Aperte "Enter" para continuar')

        elif escolha==opcoesCabiveisChaves[1]:#'2':'Gerar tabela de Frequência com classes',
            arquivoDadosCaminho= os.path.expanduser('./dadosQuantitativosContinuos.txt')
            #arquivoDadosCaminho= f'dadosQuantitativosContinuos.txt'#os dados serão coletados de um arquivo de texto
            tabelaArquivoCaminho=os.path.expanduser('./tabelaFrequenciaComClasses.txt')
            print(separador)
            print('Por favor, digite os dados em um arquivo de texto no seguinte caminho: \n',arquivoDadosCaminho)
            print(separador)
            input('Aperte "enter" quando tiver inserido todos os dados no arquivo em questão...')
          
            #== == !! !! Leitura dos dados quantitativos continuos
            dados=open(arquivoDadosCaminho,'r')
            dadosSeparados=dados.readlines()
            dados.close()
            
            dadosFormatados=[]
            for i in dadosSeparados:
                dadosFormatados.append(float(i))
            
            #== == !! !! Criação da tabela
            classeQuantidade=int(input('Agora, Digite a quantidade de classes... '))
            tabela=calcularFrequenciaComClasse(dadosFormatados, classeQuantidade) 

            #== == Geração do arquivo contendo a tabela
            arquivoTabela=open(tabelaArquivoCaminho,'w')
            arquivoTabela.writelines(montarTabelaParaArquivos(tabela))
            arquivoTabela.close()
            
            print(separador)
            print(f'Sua tabela foi gerada com êxito!\nVocê pode acessar através do seguinte caminho: {tabelaArquivoCaminho}')
            print(separador)

            input('Aperte "Enter" para continuar')

        elif escolha==opcoesCabiveisChaves[-2]:#'3':'Instruções de Uso do programa',
            pass
        
        elif escolha==opcoesCabiveisChaves[-1]:#'-':'Finalizar o Programa'
            break
            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            input('Ops.... Escolha não encontrada!')
    
    except FileNotFoundError:
        print('Por favor, crie o arquivo da maneira na qual lhe foi pedido. ')
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        
    except ValueError:
        print('Parece que você colocou alguma letra no arquivo....')
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
     

print('Programa finalizado com Êxito!')