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
        
        if len(ocorrencias)== i + 1: #O último elemento do ocorrencias é um caso que requer um tratamento diferente. Pois ele não irá acionar a condição anterior
            frequenciaRelativaSimples= f"{frequenciaTabela[cursor][1]}/{len(ocorrencias)}" 
            frequenciaTabela[cursor].append(frequenciaRelativaSimples) 

        elif (ocorrencias[i] > frequenciaTabela[cursor][0]): # Verifica se o elemento do ocorrencias não é mais o mesmo do laço passado 
            
            frequenciaTabela.append([ocorrencias[i],1])# A tabela de frequências irá adicionar, o novo valor na próxima linha.
            
            #antes de ir para próxima linha, será preciso calcular a frequência relativa.
            
            frequenciaRelativaSimples= f"{frequenciaTabela[cursor][1]}/{len(ocorrencias)}" #Será entregue uma fração.
            
            frequenciaTabela[cursor].append(frequenciaRelativaSimples)     
            
            cursor+=1 # O cursor passará a apontar para este agora
            
        else:
            frequenciaTabela[cursor][1]+=1 #a Tabela irá incrementar 1 na quantidade de elementos desta amostra
            
        
    __calcularFrequenciaAcumulativa(frequenciaTabela)#Calculado a frequencia absoluta e relativa simples, devemos agora calcular as Frequencias Acumulativas.
        
    return frequenciaTabela
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
        tabelaFrequencia.append(__gerarFrequenciaSimplesComClasses(amostras,inicioIntervalo,finalIntervalo))
        inicioIntervalo=finalIntervalo
        finalIntervalo+= intervalo
    
    __calcularFrequenciaAcumulativa(tabelaFrequencia)
    return tabelaFrequencia
    
def __gerarFrequenciaSimplesComClasses(array, inicioIntervalo:float, finalIntervalo:float):
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


def montarTabela(Tabela:list[list])->str:
    s=f'{"Xi":^10}  |  {"fi":>10}  |  {"fri":>10}  |  {"Fi":>10}  |  {"Fri":>10}|\n{"==="*30}\n +-=A+' 
    
    for linha in Tabela:    
        Xi, fi, fri, Fi, Fri= linha   
        s+=f'{Xi:^10}  |   {fi:^10}  |  {fri:^10}  |  {Fi:^10}  |  {Fri:^10}|\n +-=A+'
    
    return s

def montarTabelaParaArquivos(Tabela:list[str])->list[str]:
    tabela=montarTabela(Tabela)
    tabelaLista= tabela.split('+-=A+')
    return tabelaLista
    
def selectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j

        array[min], array[i] = array[i], array[min]


def __calcularFrequenciaAcumulativa(Tabela:list[list[str]])->None:
    
    if len(Tabela[0])<5: #Checamos se a tabela possui os cinco campos: [Xi, fi, fri, Fi, Fri]
        for i in range(len(Tabela)):
            
            while len(Tabela[i])<5:
                if len(Tabela[i])==4:#Checa se a coluna da vez é a Fri
                    Tabela[i].append('0/0')
                
                else: # Checa se é coluna qualquer
                    Tabela[i].append(0)
                            
    for j in range(len(Tabela)):
        
        friSimplesAtual=Tabela[j][2].split("/")
        friAcumulativaAnterior=Tabela[j-1][-1].split("/")
        
        if j==0: # A primeira ocorrência é um caso diferente.
            Tabela[j][3]= Tabela[j][1]
            Tabela[j][4]= Tabela[j][2]
        
        else: #Caso seja os outros casos Será preciso somar a Frequencia Acumulativa do caso anterior com a frequencia Simples da amostra atual.
            Tabela[j][3]= Tabela[j-1][3] + Tabela[j][1]
            Tabela[j][4]= f"{int(friSimplesAtual[0])+ int(friAcumulativaAnterior[0])}/{int(friSimplesAtual[1])}" 
    
    return Tabela