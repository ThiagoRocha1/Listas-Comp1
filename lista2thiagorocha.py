#Questao 1

def verificar1 (x):
#Essa funcao verifica se um numero é 0, diferente de 0 e impar ou  diferente de 0 e par.
   if x == 0: 
     return 0
   elif (x%2) != 0 : 
     return 1
   else: 
    return 2

print(verificar1(0))
print(verificar1(17))
print(verificar1(18))
print('----------------------------------')

#Questao 2 

def expressao2 (x):
#Essa funcao fornece a resolucao de uma equacao que possui x como entrada limitada
# por intervalos numericos
 
   if x < 0:
     return 0

   elif 0 <=x and x<1: 
     return 3

   elif 1<= x < 3:
     return 3-(2*(x-1))

   elif 3 <= x < 4.5: 
     return ((x-3)**2) + 4*(x-3)

   else:
     return -1* ((x- 4.5)**3) + 5*(x**2) - 6*(x-5) + 2

print(expressao2(-3))
print(expressao2(0))
print(expressao2(2.9))
print(expressao2(4))
print(expressao2(6))
print('----------------------------------')

#Questao 3

def questao3 (x,y,z):
#Saber se uma condica e verdadeira apos analisa o valor de uma diferenca em modulo com um terceiro numero  

#Returns das diferencas

   diferenca = x-y 
   if diferenca >= 0:
     diferenca  = diferenca 
   else:
     diferenca = -diferenca 
     
   if diferenca < z:
     return 1
   else:
     return 0 


print(questao3(5,5.5,1))
print(questao3(6,5,2))
print(questao3(4.8,4.9,0.1))
print(questao3(5,2,3))
print('----------------------------------')


#Questao4 


def questao4 (bolas_encontradas,bolas_total,tempo_limite,tempo_completado):
  
   pontuacao_base = 0 

#Calculo da pontuacao base
   if bolas_encontradas == bolas_total:
     pontuacao_base = 100

   elif bolas_encontradas > (0.7 * bolas_total):
     pontuacao_base = 50

   elif (0.3* bolas_total) <= bolas_encontradas <= (0.7* bolas_total):
     pontuacao_base = 25

   else:
     pontuacao_base = 0

# Calculo dos descontos pelo tempo finalizado a prova
   if tempo_completado <=  tempo_limite:
     pontuacao_final = pontuacao_base

   elif tempo_limite <  tempo_completado < (tempo_limite + 10 ):
     pontuacao_final = (0.8 * pontuacao_base)
   
   elif (tempo_limite + 10) <= tempo_completado <= (tempo_limite +30):
     pontuacao_final= (0.4 * pontuacao_base)
   else:
     pontuacao_final = 0

   return pontuacao_final


print(questao4(8,8,20,15))     
print(questao4(8,10,20,15)) 
print(questao4(7,10,20,15)) 
print(questao4(2,10,20,15)) 
print(questao4(5,10,20,20)) 
print(questao4(5,10,20,25)) 
print(questao4(5,10,20,30)) 
print(questao4(5,10,20,50)) 
print(questao4(5,10,20,60)) 
print('----------------------------------')

   

   
   
   
#Questao 5 
#Essa funcao ira indicar a situacao de um aluno no seu numero de faltas 


def questao5 (qnt_total_aulas,qnt_faltas_aluno):

#Essa primeira parte analisa se as entradas sao validas. Valores inteiros maiores ou iguais a 0 e numero de faltas< numero de aulas 
   if type(qnt_total_aulas) == int and type(qnt_faltas_aluno) == int and qnt_total_aulas >= 0 and qnt_faltas_aluno >= 0 and qnt_faltas_aluno <= qnt_total_aulas:
     qnt_total_aulas = qnt_total_aulas 
     qnt_faltas_aluno = qnt_faltas_aluno
   else:
     return -1 
      
#Essa parte analisa a situacao do aluno
   qnt_max_faltas = 0.3 * qnt_total_aulas
   porct_faltas = (qnt_faltas_aluno/qnt_total_aulas) *100
   qnt_faltas_excedidas = qnt_faltas_aluno - qnt_max_faltas
   
   if qnt_faltas_aluno > qnt_max_faltas:
     return 0, qnt_faltas_excedidas , porct_faltas  
   else:
     return 1,qnt_max_faltas - qnt_faltas_aluno, porct_faltas  
     
print(questao5(True,110))
print(questao5(100,15))
print(questao5(100,25))
print(questao5(100,35))
print('----------------------------------')


#Questao6

def questao6 (a1,a2,a3,b1,b2,b3):
#jogo par oum impar. As tres primeiras entradas sao as jogadas do 1 jogador e as 3 ultimas as jogadas do 2 jogador
#Jogador 1  escolhe sempre par e o Jogador 2 escolhe sempre impar
   vitoria1 = 0 
   vitoria2 = 0 
#Jogada 1
   if (a1+b1)%2 == 0:
     vitoria1 = vitoria1 + 1
   else:
     vitoria2 = vitoria2 + 1  
#Jogada 2
   if (a2+b2)%2 == 0:
     vitoria1 = vitoria1 + 1
   else:
     vitoria2 = vitoria2 + 1   
#Jogada 3
   if (a3+b3)%2 == 0:
     vitoria1= vitoria1 +1 
   else:
     vitoria2= vitoria2 + 1   
     
#Vitorias de cada jogador 
   return vitoria1,vitoria2

    
print(questao6(1,1,1,1,1,1))
print(questao6(2,1,1,1,1,1))
print(questao6(2,1,1,1,2,1))
print(questao6(2,1,2,1,2,1))
print('----------------------------------')



#Questao 7 

def questao7(ovosDisponiveis,ovosNecessarios,farinhaDisponivel,farinhaNecessaria ) :
    #Analise da validacao dos argumentos. O que nao pode acontecer
   if type(ovosDisponiveis) != int and type(farinhaDisponivel)!= int or ovosDisponiveis < 0 or farinhaDisponivel < 0:
      return -1,-1,-1 
   if type(ovosNecessarios) != int and type(farinhaNecessaria) != int or ovosNecessarios<= 0 or farinhaNecessaria <= 0: 
     return -1,-1,-1
       
       
   # Codigo da receita de bolo 
   
   # Quantos Bolos consigo fazer 
   razaoOvos = (ovosDisponiveis// ovosNecessarios)
   razaoFarinha = (farinhaDisponivel//farinhaNecessaria)
   bolosPossiveis = 0 
   
   if ovosDisponiveis >= ovosNecessarios and farinhaDisponivel >= farinhaNecessaria:
     if razaoOvos == razaoFarinha: 
       bolosPossiveis = razaoOvos
     elif razaoOvos < razaoFarinha:
       bolosPossiveis = razaoOvos
     else:
       bolosPossiveis = razaoFarinha
   else:
     bolosPossiveis = 0 
     
   # Separar em dois codigos. O primeiro bolo possivel >= 1 e o outro Bolo possivel == 0. 
   farinhaFaltante = 0 
   caixasOvos = 0 
   #Bolo >= 1 
   if bolosPossiveis>=1:
    ovosAposBolo = ovosDisponiveis - ovosNecessarios * bolosPossiveis
    farinhaAposBolo = farinhaDisponivel - farinhaNecessaria * bolosPossiveis 
   #Sobra ou Falta Ovo   
    if ovosAposBolo >= ovosNecessarios : 
      caixasOvos = 0 
    else:
      ovosPreciso = ovosNecessarios - ovosAposBolo
      if ovosPreciso// 12 == 0:
        caixasOvos = 1
      else:
        caixasOvos = ovosPreciso//12 + 1 
    
    # Sobra ou falta farinnha
    if farinhaAposBolo >= farinhaNecessaria:
      farinhaFaltante = farinhaNecessaria 
    else: 
      farinhaFaltante = farinhaNecessaria - farinhaAposBolo
    # Bolos Possiveis <= 0 
   else:
       #Ovos Faltando ou Sobrando 
      if ovosDisponiveis <= ovosNecessarios:
        ovosPreciso = ovosNecessarios - ovosDisponiveis 
        if ovosPreciso//12 == 0:
          caixasOvos = 1
        else:
          caixasOvos = (ovosPreciso//12) + 1
      else:
           caixasOvos = 0
      if farinhaDisponivel < farinhaNecessaria:
          farinhaFaltante = farinhaNecessaria - farinhaDisponivel
      else:
          farinhaFaltante = 0 

          

        
   return bolosPossiveis, caixasOvos, farinhaFaltante 
   
   
   
print(questao7(6,6,200,200))
print(questao7(18,6,600,200))
print(questao7(18,6,500,200))
print(questao7(4,5,150,100))
print(questao7(8,3,100,300))
print(questao7(2,18,100,250))
print(questao7(5,0,300,150))
print('----------------------------------')   
   
