#====Exception
#===Exception caso o usuário escolha um valor não cadastrado no menu de opções
class IndiceInvalidException(Exception): 
    def __init__(self, msg) -> None:
        super().__init__(msg)
        

def PermutacaoSimples(n:int):
    try:
        assert n >= 1, 'Não é possível fazer Permutação com valores menores que 1 !'
        resultado = 1
        multiplicador = 2
        while multiplicador <= n:
            resultado = resultado*multiplicador
            multiplicador +=1
        return resultado
    
    except AssertionError as Ae:
        raise IndiceInvalidException(Ae)
    
    except ValueError:
        raise IndiceInvalidException(f' O valor digitado não foi um número inteiro!')
    except Exception as E:
        raise IndiceInvalidException(E)
        



def PermutacaoCircular(n:int):
    try:
        assert n >= 1, 'Não é possível fazer Permutação com valores menores que 1 !'
        n -= 1
        resultado=1
        multiplicador=2

        while (multiplicador<=n):
            resultado= resultado* multiplicador
            multiplicador+= 1
        
        return resultado
    
    except AssertionError as Ae:
        raise IndiceInvalidException(Ae)
    except ValueError:
        raise IndiceInvalidException(f' O valor digitado não foi um número inteiro!')
    except Exception as E:
        raise IndiceInvalidException(E)

def ArranjoSimples(n:int,p:int):
    try:
        assert n >= 1, 'Não é possível fazer Permutação com valores menores que 1 !'
        assert n >= p, "o número de termos do conjunto é maior que o número de elementos!"
        
        resultadoN=1
        multiplicador=2
        b=n-p
        multiplicadorB=2
        resultadoB=1
        
        while(multiplicador<=n):
            resultadoN=resultadoN*multiplicador
            multiplicador +=1

        if(b==0 or b==1):
            b=1
                
        while(multiplicadorB<=b):
            resultadoB= resultadoB*multiplicadorB
            multiplicadorB +=1
        resultadoFinal= resultadoN//resultadoB
        
        return resultadoFinal
    
    except AssertionError as Ae:
        raise IndiceInvalidException(Ae)

    except ValueError:
        raise IndiceInvalidException(f' O valor digitado não foi um número inteiro!')
    except Exception as E:
        raise IndiceInvalidException(E)

    
def ArranjoComRepeticao(n:int,p:int):
    try:
        assert n >= 1, 'Não é possível fazer Permutação com valores menores que 1 !'
        assert n >= p, "o número de termos do conjunto é maior que o número de elementos!"
        resultadoFinal= n**p
        return resultadoFinal
    except AssertionError as Ae:
        raise IndiceInvalidException(Ae)
    
    except ValueError:
        raise IndiceInvalidException(f' O valor digitado não foi um número inteiro!')
    except Exception as E:
        raise IndiceInvalidException(E)
    
def CombinacaoSimples(n:int,p:int):

    resultadoN=1
    multiplicadorN=2
    
    resultadoP=1
    multiplicadorP=2
    
    multiplicadorB=2
    resultadoB=1

    try:
        assert n >= 1, 'Não é possível fazer Permutação com valores menores que 1 !'
        assert n >= p, "o número de termos do conjunto é maior que o número de elementos!"
        
        b=n-p
    

        while(multiplicadorN<=n): # n!
            resultadoN=resultadoN*multiplicadorN
            multiplicadorN +=1
            
        if b>1: # (n-p)!
            while(multiplicadorB<=b):
                resultadoB= resultadoB* multiplicadorB
                multiplicadorB +=1
            
        while(multiplicadorP<=p): # p!
            resultadoP=resultadoP*multiplicadorP
            multiplicadorP +=1

        produto= resultadoP*resultadoB
        resultadoFinal= (resultadoN//produto)

        return resultadoFinal #n! / p!(n-p)!
    
    except AssertionError as Ae:
        raise IndiceInvalidException(Ae)
     
    except ValueError:
        raise IndiceInvalidException(f' O valor digitado não foi um número inteiro!')
    except Exception as E:
        raise IndiceInvalidException(E)