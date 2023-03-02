from ferramentas import *

def calcularfrequenciaSemClasse(ocorrencias:list)->list[list]:
    '''Este método recebe uma lista contendo valores numéricos ou caractéres, e em seguida retornará uma tabela de frequência sem classe: na seguinte ordem: valor amostrado, a frequência absoluta simples e a frequência relativa.
    exemplo de retorno:
    [
        [20, 3, 3/4, 3, 3/4],
        [22, 1, 1/4, 4, 1]
    ]
    !!!!!! A Frequencia relativa é entregue em formato de fração
    '''
    
    selectionSort(ocorrencias) #primeiro, ordenamos a lista contendo as amostras coletadas
    frequenciaTabela=[ [ ocorrencias[0], 0] ] #Em seguida, criamos o ocorrencias que conterá todos os dados: [Xi, fi]
    cursor=0 #O cursor será responsável por apontar a lista que deverá ser adicionado as informações
    
    for i in range(len(ocorrencias)):    
        
        '''
        '''
        if (ocorrencias[i] > frequenciaTabela[cursor][0]): # Verifica se o elemento do ocorrencias não é mais o mesmo do laço passado 
            
            frequenciaTabela.append([ocorrencias[i],1])# A tabela de frequências irá adicionar, o novo valor na próxima linha.
            
            #antes de ir para próxima linha, será preciso calcular a frequência relativa.
            
            frequenciaRelativaSimples= f"{frequenciaTabela[cursor][1]}/{len(ocorrencias)}" #Será entregue uma fração.
            
            frequenciaTabela[cursor].append(frequenciaRelativaSimples)     
            
            cursor+=1 # O cursor passará a apontar para este agora

        else:
            frequenciaTabela[cursor][1]+=1 #a Tabela irá incrementar 1 na quantidade de elementos desta amostra
        
        if len(ocorrencias)== i + 1: #O último elemento do ocorrencias é um caso que requer um tratamento diferente. Pois ele não irá acionar a condição anterior
            frequenciaRelativaSimples= f"{frequenciaTabela[cursor][1]}/{len(ocorrencias)}" 
            frequenciaTabela[cursor].append(frequenciaRelativaSimples) 
            
            
            
        
    calcularFrequenciaAcumulativa(frequenciaTabela)#Calculado a frequencia absoluta e relativa simples, devemos agora calcular as Frequencias Acumulativas.
        
    return frequenciaTabela

        
array= [
10,
10,
10,
19,
21,
23,
23,
30,
37,
37,
40
]


frequenciaTabela=calcularfrequenciaSemClasse(array)

print(montarTabela(frequenciaTabela))