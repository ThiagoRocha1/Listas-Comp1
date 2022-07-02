import datetime as dt

def realizar_venda(produtos_preco,produtos_estoque,valores_das_compras):

    
    total=0
    

    while True:
        
        #Saber qual produto sera comprado

        produto_comprado=input('Digite o nome do produto comprado: ').lower()


        if produto_comprado not in produtos_preco:#Verificar se existe o produto

            print('Esse produto nâo existe')
            escolha2=input('Deseja comprar outro produto s/n ?')

            if escolha2.lower()== 's':#Verificar se o usuário quer continuar 
                continue

            elif escolha2.lower()=='n':#Calcula e imprime o total da compra
                

                valores_das_compras1+= (total,) # Adicionar na lista valores_das_compras
                

                print(f'O total da compra foi de {total} reais.')
                
                return valores_das_compras

        else: #O produto existe, saber a quantidade

            quantidade_comprar = int(input('Digite a quantidade de produto que deseja comprar: '))
            
            #Verificar a quantidade no estoque


            if quantidade_comprar>produtos_estoque[produto_comprado]:#Analisar a quantidade

                print('Quantidade acima da máxima!')
                print('Deseja continuar comprando?(s/n): ') 
                escolha3=input('Digite sua escolha: ')#Saber se vai continuar no sistema
                
                if escolha3 == 's':
                    continue

                elif escolha3 =='n':


                    valores_das_compras += (total,)# Adicionar na lista valores_das_compras

                    #Atualizar o dicionario do estoque
                    produtos_estoque[produto_comprado] -= quantidade_comprar

                    print(f'O total da compra foi de {total} reais.')

                    return valores_das_compras
                    
            else:

                total+= produtos_preco[produto_comprado]*quantidade_comprar

                print('Deseja continuar comprando?(s/n): ') 
                escolha3=input('Digite sua escolha: ')#Saber se vai continuar no sistema
                
                if escolha3 == 's':
                    continue

                elif escolha3 =='n':

                    valores_das_compras += (total,)# Adicionar na lista valores_das_compras

                    #Atualizar o dicionario do estoque
                    produtos_estoque[produto_comprado] -= quantidade_comprar

                    print(f'O total da compra foi de {total} reais.')

                    return valores_das_compras  

def alterar_preco_produto(produtos_preco):

            produto_alterar=input('Digite o nome do produto que deseja alterar: ').lower()

            if produto_alterar.lower() not in produtos_preco: # Analisar se o produto está cadastrado
                print('Esse produto ainda não foi cadastrado, cadastre-o primeiro')
                

            else:
                novo_preco=float(input('Digite o valor do novo produto: '))
                
                for produto in produtos_preco:
                    if produto == produto_alterar:
                        produtos_preco[produto] = novo_preco
                        print('Produto Alterado com sucesso!')

def alterar_quantidade_produto(produtos_estoque):

    produto_alterar=input('Digite o nome do produto que deseja alterar: ').lower()

    if produto_alterar.lower() not in produtos_estoque: # Analisar se o produto está cadastrado
        print('Esse produto ainda não foi cadastrado, cadastre-o primeiro')
        

    else:#Produto existe

        nova_quantidade=int(input('Digite a quantiadde do produto: '))
        
        for produto in produtos_estoque:# Acessar Lista do Estoque
            if produto == produto_alterar:
                produtos_estoque[produto] = nova_quantidade
                print('Item modificado com sucesso')

def adicionar_produto(produtos_estoque,produtos_preco):

            produto_adicionar=input('Digite o nome do produto que deseja adicionar: ').lower()

            if produto_adicionar.lower() not in produtos_estoque: # Analisar se o produto está cadastrado
                
                preco = float(input('Digite o preco de produto que deseja adicionar: '))
                quantidade = int(input('Digite a quantidade do produto que deseja adicionar'))

                produtos_preco[produto_adicionar]=preco
                produtos_estoque[produto_adicionar]=quantidade
                print('Produto Cadastrado!')

            else: #Produto existe
                print('Produto já Cadastrado!')

def imprimir_relatorio_de_vendas(arquivo_historico):

    total_vendas = 0

    dia=int(input('Digite o dia do relatório:'))#Dia
    mes=int(input('Digite o mes do relatório:'))#Mes
    ano=int(input('Digite o ano do relatório:'))#Ano

    
    data_analisar = f'{ano}'+'-'+f'{mes}'+'-'+f'{dia}' #Formatar a data para analisar no banco de dados

    historico = open(arquivo_historico,'r')

    linhas_historico = historico.readlines()#Separar o Arquivo em Linhas
    
    for data in linhas_historico: # Acessar a lista de linhas
        
        data_dividir = data.split(',') # Seprar em strings

        data_linha = data_dividir[0] #Data de venda dos sistemas
        vendas = data_dividir[1:-1] #Valores das vendas 

        if data_linha == data_analisar:
            print(f'{data}')
            for i in vendas:#Trasnformar os caracteres em strings para somar e dar o valor total
                i = float(i) #Transformar em Numero
                total_vendas+=i



    print(f'O total é de: {total_vendas}')
    
    historico.close()

def sair(produtos_preco,arquivo_produtos,produtos_estoque,valores_das_compras,arquivo_historico):

    #Novos dados para produtos

    lista_produtos=open(arquivo_produtos,'w')#Abrir o arquivo para sobreescrever dados

    for produto in produtos_preco: # Acesar os produtos dos dicionarios

        linha = produto+','+f'{produtos_preco[produto]}'+','+f'{produtos_estoque[produto]}'+'\n'#Formatar o texto da maneira correta

        lista_produtos.write(linha)#Adicionar no arquivo
    
    #Modificar o arquivo historico

    adicionar_historico = open(arquivo_historico,'a')#Abrir o arquivo de historico para adicionar

    #Achar a data atual

    data_atual=dt.date.today()#Tipo objeto
    data_atual = str(data_atual)#Transformar em string

    if int(data_atual[5:7])<10:
        data_atual= data_atual[0:5]+data_atual[6:]

    #Ver as compras do sistema e adicionar no arquivo 

    
    compras_string=''
    for compras in valores_das_compras:#Acessar as compras do sistema
        
        compras = str(compras)#Transformar em string
        compras_string=compras_string+compras+','#Formar uma string
    
    linha=data_atual+','+compras_string+'\n'


    adicionar_historico.write(linha)#Escrever no arquivo


    
    lista_produtos.close()#Fechar arquivo
    adicionar_historico.close()#Fechar arquivo

    print(produtos_preco)
    print(produtos_estoque)

    return produtos_preco,produtos_estoque #Return da funcao
    
        

def menu1(arquivo_produtos,arquivo_historico):

    lista_produtos=open(arquivo_produtos,'r')#Abrir o arquivo para visualizacao
    historico=open(arquivo_historico,'r') #Abrir o arquivo 
    info_produtos = lista_produtos.readlines()#Separar o arquivo em linhas
    
    valores_das_compras=() #Armazenas os valores das compras realizadas 
    produtos_preco={}#Dicionario com chave produto e valor preco
    produtos_estoque={}#Dicionario com chave produto e valor quantidade em estoque

    for linha in info_produtos: #Percorre as linhas do arquivo

        linha=linha.split(',')#Separar os itens da linha

        produtos_preco[linha[0]]=float(linha[1])#Adicionar no dict de produtos/valor

        produtos_estoque[linha[0]]=int(linha[2])#Adicionar no dict de produtos
    
    lista_produtos.close()#Fechar os arquivos txt
    historico.close()#Fechar os arquivos txt
        
    while True:

        print('1-Realizar uma Venda')
        print('2-Alterar preço de um produto')
        print('3-Alterar quantidade de itens de um produto')
        print('4-Adicionar um novo produto')
        print('5-Imprimir relatório de venda de um dia')
        print('6-sair')
        print('')
        escolha=int(input("Digite o que deseja fazer: "))

        if escolha == 1: # Realizar Venda
            valores_das_compras+=realizar_venda(produtos_preco,produtos_estoque,valores_das_compras)



        elif escolha==2: #Mudar Preco do Produto
            alterar_preco_produto(produtos_preco)

        elif escolha == 3:#Alterar Quantidade de produto
            alterar_quantidade_produto(produtos_estoque)
            

        elif escolha ==4: #Adicionar Produto
            adicionar_produto(produtos_estoque,produtos_preco)

        elif escolha==5: # Imprimir relatório de vendas de um dia
            imprimir_relatorio_de_vendas(arquivo_historico)

        elif escolha == 6:#Overwrite arquivos produtos e imprimir histórico
            sair(produtos_preco,arquivo_produtos,produtos_estoque,valores_das_compras,arquivo_historico)
            break

        else:
            print('Valor invalido!')
            continue


menu1('produtos2.txt','historico2.txt')

                











                            
                
                
                    






