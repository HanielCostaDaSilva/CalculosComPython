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
    frequenciaTabela=[ [ array[0], 0] ] #Em seguida, criamos o array que conterá todos os dados: [Xi, fi]
    cursor=0 #O cursor será responsável por apontar a lista que deverá ser adicionado as informações
    
    for i in range(len(array)):    
        
        if len(array)== i + 1: #O último elemento do array é um caso que requer um tratamento diferente. Pois ele não irá acionar a condição anterior
            frequenciaRelativaSimples= f"{frequenciaTabela[cursor][1]}/{len(array)}" 
            frequenciaTabela[cursor].append(frequenciaRelativaSimples) 

        elif (array[i] > frequenciaTabela[cursor][0]): # Verifica se o elemento do array não é mais o mesmo do laço passado 
            
            frequenciaTabela.append([array[i],1])# A tabela de frequências irá adicionar, o novo valor na próxima linha.
            
            #antes de ir para próxima linha, será preciso calcular a frequência relativa.
            
            frequenciaRelativaSimples= f"{frequenciaTabela[cursor][1]}/{len(array)}" #Será entregue uma fração.
            
            frequenciaTabela[cursor].append(frequenciaRelativaSimples)     
            
            cursor+=1 # O cursor passará a apontar para este agora
            
        else:
            frequenciaTabela[cursor][1]+=1 #a Tabela irá incrementar 1 na quantidade de elementos desta amostra
            
        
    calcularFrequenciaAcumulativa(frequenciaTabela)#Calculado a frequencia absoluta e relativa simples, devemos agora calcular as Frequencias Acumulativas.
        
    return frequenciaTabela

        
array= [10.9,  12.2,  11.7,  12.5,  13.9,  12.3,  14.4,  13.6,  12.7,  12.6, 11.3, 11.7, 12.6, 13.4, 15.2, 13.2, 13.0, 16.9, 15.8, 14.7, 13.5,12.7, 12.3, 13.5, 15.4, 16.3, 15.2, 12.3, 13.7, 14.1 ]


frequenciaTabela=calcularfrequenciaSemClasse(array)


print(montarTabela(frequenciaTabela))