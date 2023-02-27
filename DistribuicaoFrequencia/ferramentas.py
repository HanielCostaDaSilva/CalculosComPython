def montarTabela(Tabela:list[list])->str:
    s=f'{"Xi":^10}  |  {"fi":>10}  |  {"fri":>10}  |  {"Fi":>10}  |  {"Fri":>10}|\n' +"==="*30
    for linha in Tabela:    
        Xi, fi, fri, Fi, Fri= linha 
        
        s+=f'\n {Xi:>10}  |   {fi:>10}  |  {fri:>10}  |  {Fi:>10}  |  {Fri:>10}|'
    
    return s

def selectionSort(array):

    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j

        array[min], array[i] = array[i], array[min]


def calcularFrequenciaAcumulativa(Tabela:list[list[str]])->None:
    
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
