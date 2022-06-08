#Questao 1 

def total1 (gramaspresunto,precopresunto,gramasqueijo,precoqueijo,gramasmortadela,precomortadela):
   #Essa função retorna o valor total do mercado, inserindo o peso do produto e o preço por peso
   totalPresunto= gramaspresunto*precopresunto
   totalQueijo= gramasqueijo * precoqueijo 
   totalMortadela= gramasmortadela * precomortadela
   valorTotal= totalPresunto +  totalQueijo + totalMortadela
   return valorTotal   

print(total1(1,1,2,2,3,3))
print(total1(100,0.02,200,0.011,150,0.09))
print(total1(150,0.012,300,0.1,250,0.08))

#Questao 2

def corrente2 (r1,r2,ifn):
# Essa função retorna o valor da corrente que passa por r2
   i2= r1/(r1+r2) * ifn
   return i2

print(corrente2(1,1,10))
print(corrente2(3,2,15))
print(corrente2(1,100,5))

#Questao 3

def funcao3 (x):
#Essa função fornece o valor de y, a partir de x, através de uma expressão algébrica
   y=3*x**3+ (x**2+5)/4 - 2*(x+4* (x**2 + x**(1/3)))
   return y

print(funcao3(0))
print(funcao3(1))
print(funcao3(5))

#Questao4

def conversor4 (x):
# Essa função converte radianos em graus
   pi=3.1416
   graus=( x*180)/pi
   return graus 

print(conversor4(1))
print(conversor4(3.1416/2))
print(conversor4(3.1416/4))

#Questao5

def perimetro5 (base,altura):
#Essa função retorna o perimetro de um triângulo isósceles, dado o valor de sua altura e base.
   l=( altura**2 + (base**2)/4 )**(1/2)
   return 2*l + base

print(perimetro5(6,4))
print(perimetro5(10,6))
print(perimetro5(30,17))

#Questao 6

def aceleracao6 (ti1,tf1,deltaS1,S1,S2,vf):
#Essa funcao retorna o valor da aceleracao de um veículo dado os valores do tempo, caminho percorrido
#posição e velocidade final
   v0=(deltaS1)/(tf1-ti1)
   deltaS2 = S2-S1
   a=(vf**2 - v0**2)/(2*deltaS2)
   return a

print(aceleracao6(0,1,0,2,12,30))
print(aceleracao6(1,2,10,5,15,80))
print(aceleracao6(0.5,5.5,20,2.3,42.3,100))


#Questao7
def seno7 (x):
#Essa função retorna o seno de um ângulo em radianos
   seno= x - (x**3)/(3*2*1) + (x**5)/(5*4*3*2*1) - (x**7)/(7*6*5*4*3*2*1) + (x**9)/(9*8*7*6*5*4*3*2*1)
   return seno


print(seno7(0.523583))
print(seno7(3.1416/2))
print(seno7(3.1416/4))
