
def questao1(lista_numeros,tipo_media='A'):#Achar a media de valores a partur de uma lista
    
    #Tratamento de erros
    if tipo_media != 'A' and tipo_media != 'G' and tipo_media != 'H':
        return -1
    
    if tipo_media == 'A':#Media aritmetica
        soma_dos_numeros = 0 
        for numero in lista_numeros:
            soma_dos_numeros += numero
        
        media=soma_dos_numeros/len(lista_numeros) #Media final
        return media
    
    elif tipo_media == 'G':#Media Geometrica
        
        #Multiplicar os valores da lista
        multiplicacao_dos_valores = 1

        for numero in lista_numeros:# Acessar a lista
            multiplicacao_dos_valores *= numero

        media = (multiplicacao_dos_valores)**(1/len(lista_numeros))
        
        return media

    else:#Media harmonica
        
        soma = 0 
        for numero in lista_numeros:#Acessar a lista
            numero = 1/numero# Fazer o inverso do numero 
            soma+= numero
            
        harmonica = len(lista_numeros)/(soma)

        return harmonica

#print(questao1([25, 5]))
#print(questao1([25, 5], 'A'))
#print(questao1([3, 6, 9, 27], 'G'))
#print(questao1([2, 2, 4, 4, 4, 4], 'H'))
#print(questao1([1, 2, 3, 4, 5], 'B'))


def questao2 (lista1,lista2):#-> Irá retornar uma nova lista com a média dos valores elemento a elemento

    lista_final=[]#Lista com a media,elemento a elemento, dos termos percorridos até a posição que ele se encontra 
    elemento=0
    try:
        
        while elemento < len(lista1):

            media=(lista1[elemento]+lista2[elemento])/2
            lista_final.append(media)
            elemento+=1

        
    except TypeError:
        return -1

    except IndexError:
        return lista_final

    else:
        return lista_final

#print(questao2([1, 2, 3],[3, 4, 5]))
#print(questao2([1, 2, 3],[3, 4]))
#print(questao2([1, 2],[3, 4, 5]))
#print(questao2([1, 2, 3],[3, '4', 5]))
#print(questao2(['1', 2, 3],[3, 4, 5]))

def questao3 (arquivo_temperaturas):
    '''Recebe o nome de um arquivo que contém as temperaturas de um dia e retorna a temperatura máxima'''
    try:#Analisar o arquivo
        temperaturas=open(arquivo_temperaturas,'r')#Abrir o arquivo

        linhas_arquivo=temperaturas.readlines()#Separar o arquivo em linhas
        temperaturas_float=[]#Salvar as linhas de temperaturas convertidas
        pos = 0

        while pos < len(linhas_arquivo):#Abrir uma lista com lista de varios dados
            numero=float(linhas_arquivo[pos])#Converter os números
            temperaturas_float.append(numero)#Adicionar na lista de temperaturas
            pos+=1


        maximo = 0

        for temp in temperaturas_float:#Analisar a maior temperatura
            if temp > maximo :#Comparacaco
                maximo = temp

        return maximo
        
    except FileNotFoundError:#Erro de Arquivp
        print('Arquivo não encontrado')
        return -1

    except ValueError:#Erro de valor inválido

        print(f'Não foi possível converte a linha {pos}')#Linha do erro
        print(f'Valor: {linhas_arquivo[pos]} não pode ser convertido para string')#Tipo não convertido
        pos+=1
        while pos < len(linhas_arquivo):#Abrir uma lista com lista de varios dados
            numero=float(linhas_arquivo[pos])#Converter os números
            temperaturas_float.append(numero)#Adicionar na lista de temperaturas
            pos+=1

        maximo = 0

        for temp in temperaturas_float:#Analisar a maior temperatura
            if temp > maximo :#Comparacaco
                maximo = temp

        return maximo
         
#print(questao3('temp0.txt'))
#print(questao3('temp.txt'))
#print(questao3('temp2.txt'))

def questao4():

    '''Recebe uma sequencia de valores por input que representam dados de times (nome,pontuacao e media de gols) e retorna um dicionario com as
    chaves Campeao e Melhor media de Gols. A media de gols é uma lista que pode ter mais de um time com a mesma média'''

    #Fazer uma lista de listas com as informacoes dos times. Nome, pontuacao e media de gols
    
    lista_de_times=[]

    #Insercao de dados pelo usuario

    for rep in range(0,5):

        print('Interacao {}'.format(rep+1))

        nome_time=input('Digite o nome do time: ')

        #Analisar as condicoes da pontuacao do time
        
        while True:

            try:
                pontuacao=int(input('Digite a pontuacao do time: '))

                if pontuacao < 0 or pontuacao>24: #Verificar se a pontuacao está entre os limites
                    raise ValueError
                
                break

            except ValueError:
                print('Pontuacao deve ser um inteiroentre 0 e 24')
                continue
        

        #Analisar as condicoes de media de gols
        while True:
            
            try:
                media_de_gols=float(input('Digite a media de gols do time: '))

                if media_de_gols <0:
                    raise ValueError
            
                break #Caso nao tenha nenhum problema,para o loop

            except ValueError:
                print('Media de gols deve ser um float maior ou igual a 0')
                continue

        
        lista_de_times.append([nome_time,pontuacao,media_de_gols]) # Adicionar os dados do time na lista de times
 
    #Analisar o time campeao

    time_campeao=''#Saber o time campeao

    lista_disputa_podium=[]#Verificar times com mesma pontuacao

    maior_pontuacao=0#Maior pontuacao

    maior_saldo_campeao=0
    
    goleadores=[]#Verificar times com maior saldo de gols

    nome_goleadores=[]

    maior_saldo=0 #Verificar Maior Saldo

    #Verificara a maior pontuacao do time
    for time in lista_de_times:
        if time[1] > maior_pontuacao:
            maior_pontuacao = time[1]

    #Adicionar o time para a lista de campeoes
    for time in lista_de_times:#Acessar a lista de times

        if time[1] == maior_pontuacao:#Comparar com a maior pontuacao

            lista_disputa_podium.append(time)#Adicionar na lista de disputa

    #Adicionar lista maior saldo de gols
    for time in lista_de_times: # Acessar a lista
        if time[2] > maior_saldo: #Verificar maior saldo
            maior_saldo = time[2] # Definir maior saldo

    #Adicionar lista de maiores saldos
    for time in lista_de_times:
        if time[2] == maior_saldo:
            goleadores.append(time)

    #Adicionar o nome dos goleadores
    for goleador in goleadores:
        nome_goleadores.append(goleador[0])
    
    #Verificar o campeao
    for time in lista_disputa_podium:#Verificar dentro da lista de campeoes
        if time[2] > maior_saldo_campeao:#Verificar o campeao
            time_campeao = time[0]
    

    dicionario_final={'Campeao':time_campeao,'Melhor media gols':nome_goleadores}

    return dicionario_final

#print(questao4())


        




        

            







        



    


