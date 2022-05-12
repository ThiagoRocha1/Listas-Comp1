# Questao 1 

def fatorial (x):
    fat = 1 
    while x>1 :
        fat = fat * x
        x = x-1 
    return fat

#print(fatorial(3))
#print(fatorial(4))

def questao1 (x,m):

# Essa funcao retorna o expoencial de um numero a partir
# da quantidade de termos que se deseja somar 
    soma = 0
    n=0
    if x == 0:
        return soma + 1   
    while n<=m:
        termo = (x**n)/(fatorial(n))
        soma = soma + termo
        n = n + 1

    return soma

#print(questao1(0,3))
#print(questao1(0,5)) 
#print(questao1(1,3))      
#print(questao1(1,5))
#print(questao1(1,10))
#print(questao1(2,10))

#Questao 2 
def questao2 (minimo,maximo,m1,m2):

#Essa funcao receber 4 numeros inteiros e positivos como argumentos, onde os 2 primeiros# sao o limite minimo e maximo de uma sequencia, respectivamente, e os 2 ultimos repre-
# sentam os multiplos a serem analisados
# Ela retorna,respecitivamente, na faixa considerada
# Qnt de num multiplos do 3 mas n do 4
# Qnt de num multiplos do 4 mas n do 3 
# Qnt de num multiplos do 3 e do 4 
    
    multiploM1 = 0
    multiploM2 = 0
    multiploM1M2 = 0
    while minimo <= maximo:
        if minimo%m1 == 0  and minimo%m2 != 0:
            multiploM1 += 1 

        elif minimo%m2 == 0 and minimo%m1 !=0:
            multiploM2 += 1 
       
        elif minimo%m1 == 0 and minimo%m2 == 0:
            multiploM1M2 += 1

        minimo += 1

    return multiploM1,multiploM2, multiploM1M2


#print(questao2(1,10,1,5))
#print(questao2(5,10,2,7))
#print(questao2(1,50,3,7))
#print(questao2(10,50,2,3))




#Questao3 
def questao3 (pi,a,f,maxTentativa):
# Essa funcao retorna, respectivamente, um inteiro representando o numero de tentativas # e um booleano que representa se a pessoa atingiu o alvo em ate o numero maximo de ten-# tativas. 
# A funcao recebe como argumento, respectivamente, posicao inicial do peso, posicao do 
# alvo, constante f e numero max de tentativas 
