#Questao 1 

def questao1 (tupla):
# 1 tuple -> 2 tuple

    nomes = ()
    idades = ()

    for i in range(0,len(tupla)):
        if i%2 == 0:

            nomes = nomes + (tupla[i],)
        
        else:
            idades = idades + ( tupla[i], ) 
    
    return (nomes,idades)


#print(questao1(('Luiza',18,'Rodrigo',20,'Arthur',44,'Ana',7)))
#print(questao1(('Joana',16)))
#print(questao1(()))


#Questao 2 

def questao2 (tupla_mae,time_mae):

# tuple of tuples, string -> int
# type(time_mae) = string 

    vitorias = 0 
    empates = 0 

    for resultado in tupla_mae:
    # ( 'time1', 'time2', 0 )
    # Achar a posicao do time
        if resultado[0].lower() != time_mae.lower()  and resultado[1].lower() != time_mae.lower():
            continue

        posicao_final = 0
   
        for posicao_time  in range(0,2):
             
            if resultado[posicao_time].lower()  == time_mae.lower() :
                posicao_final  += posicao_time

    #Achar o resultado do jogo 
        if posicao_final == resultado[2]:
            vitorias += 1
        elif resultado[2] == 2:
            empates += 1   
    
    pontuacao = ( 3 * vitorias + empates )
    
    return pontuacao 


'''print(questao2((('Bayern','Barcelona',0),('Liverpool','Bayern',1),('Liverpool','Real Madrid',0)),'Bayern'))
print(questao2((('Bayern','Barcelona',0),('Liverpool','bayern',1),('Bayern','Real Madrid',2),),'BAYERN'))
print(questao2((('Bayern','Barcelona',0),('Liverpool','Bayern',0),('Bayern','Real Madrid',2)),'bayern'))
print(questao2((('Bayern','Barcelona',0),('Liverpool','Bayern',0),('Bayern','Real Madrid',2)),'bArCeLoNa'))
print(questao2((('Bayern','Barcelona',0),('Liverpool','Bayern',0),('Bayern','Real Madrid',2)),'LiVeRpOol'))
'''

#Questao 3 

def questao3 (string):
    
# str -> tuple (2 elements)
#Contar a quantidade de caracteres diferentes de espaco em branco 
    qnt_caracter = 0
    qnt_palavras = 0
    for caracter in string:
        if caracter == ' ':
            continue
        qnt_caracter += 1
#Contar quantidade de palavras        
    for caracter2 in range(0,len(string)):
        if string[caracter2] == ' ' and caracter2 == 0:
            continue
        
        if string[caracter2] == string[-1] and string[caracter2] != ' ':
            qnt_palavras += 1
            
        if string[caracter2] == ' ' and string[caracter2 - 1] != ' ':
            qnt_palavras += 1
        
    
    return ( qnt_caracter, qnt_palavras)

'''    
print(questao3('Aqui temos 4 palavras.'))
print(questao3('  Ha dois espacos em branco no inicio dessa frase.'))
print(questao3('Tem 4 espacos em branco no final dessa string.    '))
print(questao3('$! ~() '))
print(questao3('  '))
print(questao3(' a '))
'''

#Questao 4 

def fatiar_lista (lista):
    
    pi = 0
    lista_fatiamento = []
    
    for letra in range(0,len(lista)):
     
        posicao_branco = 0    
        
        if lista[letra] == ' ':
            
            lista_fatiamento += [lista[pi:letra]]
            posicao_branco = letra
            pi = letra
        
        
        if letra == len(lista)-1 :
            lista_fatiamento += [lista[pi:letra+1]]
    
    return(lista_fatiamento)

def questao4(string1,string2):
# 2 str -> int
# Analisar o tamanho da string 2 para saber o fatiamento da string 1 
# Analisar se os caracteres em sequencias sao iguais. 

    recorrencia = 0
      
    lista_fatiamento = fatiar_lista(string1)
              
    for palavra in lista_fatiamento:

        x = 0
        pi = x 

        while x < len(palavra):
            
            if x == len(palavra)-1:
                break

            if palavra[pi:x+(len(string2))].lower() == string2.lower():
                recorrencia +=1

                x+= len(string2)
                pi = x
                continue

            x += 1
            pi = x  


            
            
    return recorrencia


    
#print(questao4('tres tigres tristes','t'))
#print(questao4('paralelepipedo','t'))
#print(questao4('Esssess ssão algunss tesstes', 'ss'))
#print(questao4('arara', 'ara'))
#print(questao4('arara', 'ar'))
#print(questao4('aaaaaaa','aa'))


    
#print(questao4('tres tigres tristes','t'))
#print(questao4('paralelepipedo','t'))
#print(questao4('Esssess ssão algunss tesstes', 'ss'))
#print(questao4('arara', 'ara'))
#print(questao4('arara', 'ar'))
#print(questao4('aaaaaaa','aa'))


#Questao 5

def questao5 ():

    lista_produtos = []


    for i in range(5):

        produto = str(input('Digite o nome do produto: '))
        quantidade = int(input('Digite a quantidade do produto: '))
        preco = float(input('Digite o preco do produto: '))

        l = [produto,quantidade,preco]

        lista_produtos += [l]
    
        

    menor_quantidade = []

    mais_caro = 0

    # Analisar a lista de produtos

    for produtos in lista_produtos:

        # Analisar quantos produtos possuem menos de 50 unidades

            qnt_produto = produtos[1]

            if qnt_produto < 50:
                
                menor_quantidade += [produtos[0]]

        #Analisar o produto mais caro

            preco_produto = produtos[2]

            if preco_produto > mais_caro:

                mais_caro = produtos[2]
                produto_mais_caro = produtos

    # Printar os argumentos na tela 

    qnt_menor_quantidade = len(menor_quantidade)
 

    print (f'Ha {qnt_menor_quantidade} produtos com menos de 50 unidades:' , end=' ')

    for e in menor_quantidade:

        print(e,end='; ')
    
    print(' ')

    nome_mais_caro = produto_mais_caro[0]
    preco_mais_caro = produto_mais_caro[2]

    print(f'O produto mais caro eh o {nome_mais_caro}, e ele custa {preco_mais_caro:.4} reais',end ='\n')

    print(' ')

    #Transformar a lista de produtos em uma tupla de tuplas
    
    x=0

    for listas in lista_produtos:

        listas = tuple(listas)
        lista_produtos[x] = listas
        x += 1 

    return tuple(lista_produtos)


print(questao5())
