def selectionSort(array):

    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j

        array[min], array[i] = array[i], array[min]

array= [10.9,  12.2,  11.7,  12.5,  13.9,  12.3,  14.4,  13.6,  12.7,  12.6, 11.3, 11.7, 12.6, 13.4, 15.2, 13.2, 13.0, 16.9, 15.8, 14.7, 13.5,12.7, 12.3, 13.5, 15.4, 16.3, 15.2, 12.3, 13.7, 14.1 ]

totalElementosArray=len(array)

#print(array)
selectionSort( array )
print(array)
print(array.__len__())



while True:
    inicio=float(input('Digite o início do intervalo: '))
    inicioIndice=0
    limite=float(input('Digite o valor final do intervalo: '))
    limiteIndice=0
    
    for i in range(len(array)):
        
        if array[i] >= inicio:
            inicioIndice= i
            
            break
    
    for j in range(len(array)):
        
        if array[j]>=limite:
            limiteIndice= j
            break
        
        if j+1 == len(array):
            limiteIndice= j
        
    dominio= array[inicioIndice : limiteIndice] #!!!!!! o programa possui um problema quando vai adicionar o último elemento...
    
    for i in array:
        print(f'|{i}', sep='|')
    print('')    
    
    print('*/*' *30)
    print('-=-' *30)
    print('foi ordenado para limitar de : ',inicio)
    print('e para se encerrar em: ',limite)
    print('-=-' *30)
    print('o domínio se inicia em: ', array[inicioIndice])
    print('o domínio vai até o valor: ', array[limiteIndice])
    
    print(f' o domínio é este: {dominio}, \n são {len(dominio)} elementos. ')
    
    print('*/*' *30)
   
    input()