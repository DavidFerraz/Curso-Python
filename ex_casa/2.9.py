# Faça um programa que receba um número. Verifique se este número é primo ou não, e retorne o resultado:

# 	O número x é primo
# ou
# 	O número x não é primo

numero = int(input("Entre com um numero: "))

if numero > 1:
    for i in range(2,numero):
        if numero % i == 0:
            print("O número", numero, "não é primo")
            break
    else:
        print("O número", numero, "é primo")