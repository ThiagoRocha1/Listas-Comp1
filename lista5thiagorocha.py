#Questao1

def questao1 (lista):
# Essa funcao drecebe uma lista e retorna outra com os valores da primeira
# multiplicada por 2
# list -> list
    lista2 = []
    for i in lista:
        lista2.append(i*2)
    return lista2

#print(questao1([]))
#print(questao1([1]))
#print(questao1([1.2,2]))
#print(questao1([-1,2,3,4,5.5]))

#Questao2 

def questao2(lista,n):
    lista2=[]
    for i in lista:
        if i <= n:
            lista2.append(0)
        else:
            lista2.append(1)
    
    return lista2 

#print(questao2([1,2,3,4,5],3))
#print(questao2([10,10,10,10],10))
#print(questao2([4.3,-2.3,5.8],-1.5))
#print(questao2([13.6,12.9],13.5))

#Questao3

def questao3 (lista1,lista2):
    lista_final=[]
    for i in range(0,len(lista1)):

        lista_final.append(lista1[i])
        lista_final.append(lista2[i])
    
    return lista_final

#print(questao3([1,1,1],[2,2,2]))
#print(questao3([-3.2,-4.5,-9.9,-6.3],[1.7,8.9,10.3,7.5]))
#print(questao3(['a',True,17,4.2,'c'],[20.1,'teste',False,5.7,True]))

#Questao4

def questao4 (lista):

    soma_pares  = 0
    soma_impares = 0 


    for i in range(len(lista)):
        if i%2 == 0:
            soma_pares += lista[i]
        else:
            soma_impares+= lista[i]


    return soma_impares - soma_pares

print(questao4([4,3,6,7,1,9]))
print(questao4([1,3,2,2,3,1]))
print(questao4([4,-4,7,-7]))
print(questao4([-2.22,4.12,10.75,-6.98,2.14,9.74,-0.17]))

#Questao5 

def questao5 (lista_mae):
    lista_resposta=[]
    for lista in lista_mae:
        for i in range(0,len(lista)):
            if i == 0:
                if lista[i] < lista[1]+lista[2]:
                    aux1=True
                else:
                    aux1=False
                    
                                            
            if i == 1:
                if lista[i] < lista[0]+lista[2]:
                    aux2=True
                else:
                    aux2 = False
                    
            if i == 2:
                if lista[i] < lista[0]+lista[1]:
                    aux3=True
                else:
                    aux3=False

        if aux1 == True and aux2 == True and aux3 == True:
            lista_resposta.append(True)
        else:
            lista_resposta.append(False)
            
            
 
    return lista_resposta


#print(questao5([[6,8,10],[5,12,13],[4,10,15],[7,20,10]]))
#print(questao5([[3,3,3],[2,4,6],[18,20,22]]))


#Questao6 

def questao6(lista_mae):
#Cada sublista possui 2 numeros (int ou float): o primeiro, kg e o valor por kilo
#funcao retorna o preco total a ser pago 
    
    total_final = 0 

    for lista in lista_mae:
        peso = lista[0]
        preco = lista[1]

        produto = peso * preco

        total_final += produto
            
    
    
    return total_final  

#print(questao6([]))
#print(questao6([[1.5,2]]))
#print(questao6([[1.5,2],[4,1]]))
#print(questao6([[1.2,1],[2.1,3],[4.4,2],[0.5,4]]))

#Questao7 

def questao7 (lista_mae):

    lista_resposta = [0]*20
    
    for i in lista_mae:
        lista_resposta[i] += 1
    
    return lista_resposta

#print(questao7([6,1,0,1,18]))
#print(questao7([0,1,1,2,2,2,3,3,3,3,4,4,4,4,4]))
#print(questao7([19,10,6,3,7,0,15,6,6,19]))
#print(questao7([15,14,6,14,10,1,7,3,14,9,18,6,0,11,1,4,8,13,11,17]))

#Questao8 

def questao8 (lista):
#list -> int 
    m = 1
    diferenca = lista[0]-lista[1]

    for i in range(0,len(lista)):
        if i == len(lista)-1:
            break

        if lista[i]-lista[i+1] == diferenca:
            continue
        else:
            m+=1
            diferenca = lista[i]-lista[i+1]

    return m     


#print(questao8([1,1,1,3,5,4,8,12]))
#print(questao8([11,-106,-223,-340,-457]))
#print(questao8([100,1100,2075,-1919,790,3499,6208,829,8130,491]))
#print(questao8([31,32,33,34,35,36,37,38,38,38]))
