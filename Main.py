
#Exercício B1 - Número Positivo ou Negativo
num = float(input("Escreve um numero: "))

if num <= 0 :
    print("Numero negativo")
else:
    print("Numero positivo")

#Exercício B2 - Maior de Idade
idade = int(input("Escreva  tua idade: "))

if idade >= 18:
    print("És maior de idade")
else:
    print("És menor de idade")

#Exercício B3 - Número Par ou Ímpar
num1 = int(input("Escreva um numero: "))

par = num1 % 2 == 0 

print(par)

#Exercício B4 - Comparação de Dois Números
num2 = float(input("Escreve um numero: "))
num3= float(input("Escreve outro numero: "))

if num2 > num3:
    print(f"O valor maior é {num2}")
else:
    print(f"O valor maior é {num3}")

#Exercício B5 - Password Simples
password_correta =("python")
password = str(input("Escreve a password: "))

if password == password_correta:
    print("Acesso permitido")
else:
    print("Acesso negado")

#Exercício I1 - Classificação de Nota

nota = int(input("Insere a tua nota: "))

if nota <10:
    print("Reprovado")
elif nota >= 10 and nota <= 13:
    print("suficiente")
elif nota >= 14 and nota <= 17:
    print("Bom")
elif nota >= 18 and nota <= 20: 
    print("Excelente")

#Exercício I2 - Classificação de Idade
idade2 = int(input("Insere a tua idade: "))

if idade2 <13:
    print("És uma criança")
elif idade2 >= 13 and idade2 <= 17:
    print("És um jovem")
elif idade2 >= 18 and idade2 <= 64:
    print("És um adulto")
else:
    print("És um senior")

#Exercício I3 - Múltiplo de 3 e 5
multiplos = int(input("Insere um numero: "))

if multiplos % 3 == 0 and multiplos % 5 == 0:
    print("Multiplos de 3 e 5")
elif multiplos % 3 == 0:
    print("Multiplos de 3")
elif multiplos % 5 == 0:
    print("Multiplos de 5")
else: print("Não e multilo de 3 nem de 5 ")

#Exercício I4 - Login com Utilizador e Password
user_correto =("admin")
password2_correta = ("1234")

user = str(input("Insere o user: "))
password2 = str(input("Insere a password:"))

if user == user_correto and password2 == password2_correta:
    print("Acesso concedido")
else:
    print("Acesso negado")

#Exercício I5 - Número dentro de intervalo
num4 = float(input("Insere um numero: "))

if num4 >= 10 and num4 <= 20:
    print("Esta entre o intervalo de 10 a 20")
else:
    print("Não esta no intervalo")

#Exercício A1 - Sistema Multibanco Simples
saldo = 1000
valor_a_levantar = float(input("Quanto queres levantar: "))

if valor_a_levantar <= saldo:
    print("Levantamento autorizado")
else: 
    print("Levantamento não autorizado")

#Exercício A2 - Maior de Quatro Números
maior = float(input("Insere o primeiro numero: "))
maior1 = float(input("Insere o segundo numero: "))
maior2 = float(input("Insere o terceiro numero: "))
maior3 = float(input("Insere o quarto numero: "))

if maior > maior1 and maior > maior2 and maior > maior3:
    print(f"O numero maior é {maior}")
elif maior1 > maior and maior1 > maior2 and maior1 > maior3:
    print(f"O numero maior é {maior1}")
elif maior2 > maior and maior2 > maior1 and maior2 > maior3:
    print(f"O numero maior é {maior2}")
elif maior3 > maior and maior3 > maior1 and maior3 > maior2:
    print(f"O numero maior é {maior3}")

#Exercício A3 - Classificação de IMC (Simplificado)
peso = float(input("Insere o teu peso: "))
altura = float(input("Insere a tua altura: "))

imc = peso / (altura * altura)

if imc <18.5:
    print("Baixo Peso")
elif imc >=18.5 and imc <=24.9:
    print("Peso normal")
elif imc >=25 and imc <=29.9:
    print("Excesso de peso")
else:
    print("Obesidade")

#Exercício A4 - Sistema de Desconto
valor_compra = float(input("Insere o valor da compra: "))
desconto = 0
valor_final = 0

if valor_compra >= 100:
    desconto = valor_compra * 0.1
    valor_final = valor_compra - desconto
    print(f"O valor final é de {valor_final} euros")
elif valor_compra >= 50:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print(f"O valor final é de {valor_final} euros")
else:
    print(f"Não tem desconto, o valor final fica {valor_compra}")


#Exercício A5 - Verificação de Ano Bissexto (Simplificado)
ano = int(input("Coloca o ano: "))

if ano % 4 == 0:
    print("Ano bissexto")
else:
    print("Ano normal")








