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




##Questao3 

def questao3 (pi,a,f,maxTentativas):

# Essa funcao retorna, respectivamente, um inteiro representando o numero de tentativas # e um booleano que representa se a pessoa atingiu o alvo em ate o numero maximo de ten-# tativas. 

# A funcao recebe como argumento, respectivamente, posicao inicial do peso, posicao do 

# alvo, constante f e numero max de tentativas. O peso atinge o alvo caso a distancia final P (A-P) e o Alvo seja menor ou igual a 0.1 metros.

    tentativas = 1

    p = pi - ((f) * (pi-a))

    deltaPA = p - a

    

    while abs(deltaPA) > 0.1 and tentativas < maxTentativas:

        tentativas += 1

        pi=p

        p=pi-((f)*(pi-a))

        deltaPA = p-a 

        

        

    # Analisa o resultado do return da funcao 

    if abs(deltaPA) <= 0.1 and tentativas <= maxTentativas:

        return tentativas,True

    elif abs(deltaPA)<= 0.1 and tentativas > maxTentativas:

        return tentativas,False

    else:

        return tentativas,False

print((questao3(10,5,1,50)))

print((questao3(10,5,2,50)))

print((questao3(0,2,0.5,5)))

print((questao3(-2,3,0.1,40))) 

#Questao4 

def questao4(x):

    i = 1

    soma = 0

    

    while i < x:

        if x%i == 0:

            soma = soma + i

            i += 1 

        else:

            i+= 1 

    if soma == x:

        return True

    else:

        return False 

print(questao4(28))

print(questao4(496))

print(questao4(8))

print(questao4(11))

#Questao 5 

def questao5a (x):

    # Retorna o quociente e resto da divisao por 10 

    q = x//10 

    r = x%10

    

    return q, r

    

def questao5b(x,y):

    contagem = 0

    q,r = questao5a(x)

    while q > 0:

        if r == y:

            contagem += 1

            q = q/10

        elif q != y:

            contagem = contagem

            q= q/10

    

    return contagem

#Questao 5 

def questao5a (x):

    # Retorna o quociente e resto da divisao por 10 

    q = x//10 

    r = x%10

    

    return q, r

    

def questao5b (x,y):

    contagem = 0 
    quociente,resto = questao5a(x)
    while quociente > 0 or resto !=0 :
        if resto ==  y:
            contagem += 1
            resto = quociente%10
            quociente = quociente//10 
        elif resto != y:
            contagem =contagem
            resto = quociente%10
            quociente = quociente//10 


    

    return contagem

#Questao 5 

def questao5a (x):

    # Retorna o quociente e resto da divisao por 10 

    q = x//10 

    r = x%10

    

    return q, r

    

def questao5b (x,y):

    contagem = 0 
    quociente,resto = questao5a(x)
    while quociente > 0 or resto !=0 :
        if resto ==  y:
            contagem += 1
            resto = quociente%10
            quociente = quociente//10 
        elif resto != y:
            contagem =contagem
            resto = quociente%10
            quociente = quociente//10 


    

    return contagem

#5A

#print(questao5a(3296))

#print(questao5a(8765421))

#print(questao5a(10101))

#5B

print(questao5b(934172665,6))

print(questao5b(4544660,3))

print(questao5b(111223,1))

print(questao5b(17970747,7))

print(questao5b(765,5))
