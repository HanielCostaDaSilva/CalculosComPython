def selectionSort(array):

    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j

        array[min], array[i] = array[i], array[min]

array= [25, 27, 24, 27, 26, 26, 27, 25, 28, 24, 27, 25, 24, 27, 26, 27, 28, 28, 27, 25, 26, 24, 28, 28, ]

selectionSort( array )
print(array)
print(array.__len__())

frequencia=[[array[0], 0]]
cursor=0

for i in range( len(array) ):
    
    if array[i] > frequencia[cursor] [0]:
        frequencia.append([array[i],1])
        cursor+=1
    
    else:
        frequencia[cursor][1]+=1


for i in range(len(frequencia)):
    
    linha=frequencia[i]
    
    print(f"\nvalor: {linha[0]}  frequencia Absoluta simples: {linha[1]}, frequencia relativa simples: {linha[1]/len(array)}")
    print('-=-'*30)

print('')    