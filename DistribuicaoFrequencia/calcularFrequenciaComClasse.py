from ferramentas import *


def calcularFrequenciaComClasse(amostras:list,classeQuantidade:int)->list[list]:
    '''Este método recebe uma lista contendo extritamente valores numéricos, junto com a quantidade de classes. Em seguida retornará uma tabela de frequência com classes na seguinte ordem: valor amostrado, a frequência absoluta simples e a frequência relativa.
    exemplo de retorno:\n
    [   
        \n[20 |- 22, 3, 3/7, 3, 3/11],
        \n[22 |- 24, 1, 1/7, 4, 4/11],
        \n[24 |-|26, 4, 4/7, 11, [11/11]
    \n
    ]
    '''
    selectionSort(amostras)
    menorTermo=amostras[0]
    
    #maiorTermo=amostras[-1] #!!!!! Não funciona sem ter um acréscimo, pois o último valor será sempre excluído
    
    acrescimo=((amostras[-1] - menorTermo)/100)
    maiorTermo= (amostras[-1]+ acrescimo)
    intervalo= (maiorTermo - menorTermo)/classeQuantidade
    tabelaFrequencia=[]
    
    #maiorTermo=amostras[-1]+ (amostras[-1] - amostras[0]) #!!!!! há Chances de um dos 
    # termos serem ignorados
    inicioIntervalo=amostras[0]
    finalIntervalo= inicioIntervalo + intervalo

    for i in range(classeQuantidade): 
        tabelaFrequencia.append(__gerarFrequenciaSimples(amostras,inicioIntervalo,finalIntervalo))
        inicioIntervalo=finalIntervalo
        finalIntervalo+= intervalo
    
    calcularFrequenciaAcumulativa(tabelaFrequencia)
    return tabelaFrequencia
    
def __gerarFrequenciaSimples(array, inicioIntervalo:float, finalIntervalo:float):
    intervalo=f'{inicioIntervalo:.3f} |- {finalIntervalo:.3f}'
    
    frequenciaAbsolutaSimples=0
    
    for cursor in array:
        if cursor >= finalIntervalo:
            #print(f'{cursor}>= {finalIntervalo}')
            break
        elif cursor>= inicioIntervalo:
            frequenciaAbsolutaSimples+=1
    
    frequenciaRelativaSimples=f"{frequenciaAbsolutaSimples}/{len(array)}"
    return [intervalo,frequenciaAbsolutaSimples,frequenciaRelativaSimples]                       


array= [10.2,10.3,10.5,30.5,40.6,23.1,19.4,37.6,23.4,21.5,37.4,34.5]

frequenciaTabela=calcularFrequenciaComClasse(array,5)

print(montarTabela(frequenciaTabela))