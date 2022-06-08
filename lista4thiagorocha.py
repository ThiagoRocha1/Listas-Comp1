# Questao1 
def questao1 (lista):
#Essa funcao recebe uma lista como entrada e retorna o maior numero dessa lista
# list -> int

    x= 0 
    maximo = lista[x]

    while x < len(lista):
        if maximo < lista[x]:
            maximo = lista[x]
        x += 1 

    return maximo 

#print(questao1([-7,-2,-5]))
#print(questao1([4,10,5,10,6,10]))
#print(questao1([0.7,4.1,0.5,2.2]))



#Questao2 

def questao2(lista):
#Essa funcao recebe uma lista e retorna apenas aqueles elementos que sejam do tipo inteiro
# list -> list
    x=0
    l_inteiros = []
    while x< len(lista):
        if type(lista[x]) == int:
            l_inteiros += [lista[x]]
        x += 1 

    return l_inteiros

#print(questao2([1.0,4,'5',True,8,10]))
#print(questao2([2,2.0,5.2,False]))
#print(questao2(['abc',2.2,-7,4.5,9]))


#Questao3 

def questao3 (lista1,lista2):
# Essa funcao recebe 2 listas, com o mesmo tamanho ,que recebe por argumento e retorna uma nova lista na qual possui o resultado da 
# expoenciacao elemento a elemento da lista 1 com a lista 2. Ex: posicao 0 lista 1 elevado a elemento 0 lista2
# list -> list

    x = 0
    l_resultado = [] 
    while x < len(lista1):
        i = lista1[x]**lista2[x]
        l_resultado += [i]
        x+= 1

    return l_resultado

#print(questao3([4,5,6],[2,2,2]))
#print(questao3([81,3,10],[1/2,3,2]))
#print(questao3([2,2,9,10],[-1,10,0,-2]))



#Questao4 

def questao4(lista):
#Essa funcao recebe uma lista por argumento e retorna uma outra lista que representa a media dos elementos até
#a determinada posicao dos elementos
# list -> list

    x = 0   
    l_media = []
    aux = 1
    soma = 0 
    while x < len(lista):
        i = lista[x]
        soma += lista[x] 
        acum = soma/aux 
        l_media += [acum]
        x+=1
        aux += 1  


    return l_media


#print(questao4([1,3,5,7,9])) 
#print(questao4([-2,2,3,-3])) 
#print(questao4([-3,2,4,-5,10]))
#print(questao4([1.5,-2.7,3.3,6.8,7.9,-12.1]))

#Questao5 

def questao5 (lista): 
# Essa funcao recebe numeros inteiros nao negativos e retorna uma lista ordenada onde os primeiros numeros sao pares e estao ordenados
# na ordem que apareceem e os ultimos numeros sao impares ordenados tambem na ordem que aparecem
# list   - > list 

    x = 0 
    pares = []
    impares = [] 
    while x< len(lista):
        if lista[x]%2 == 0:
            pares += [lista[x]]

        else:
            impares += [lista[x]]

        x+= 1 

    return pares + impares

#print(questao5([1,2,3,4,5,6,7,8]))
#print(questao5([0,10,9,1]))
#print(questao5([5,3,7,1,10,8,12]))
#print(questao5([5,5,1,3,6,7,14,6,5,3]))


#Questao6 

def questao6(lista):

# Essa funcao recebe como argumento uma lista de numeros inteiros positivos e retorna quantos divisores os numeros da lista possuem
# list -> list

    x=0 
    l_divisores = []

    while x < len(lista):

        y = 1 
        cont = 0 
        while y <= lista[x]:
            if lista[x]%y == 0:
                cont += 1
            y += 1 

        l_divisores += [cont]

        x+=1 

    return l_divisores


#print(questao6([2,3,4,5,6,7]))
#print(questao6([6,21,10,49,121]))
#print(questao6([1,10,100]))
