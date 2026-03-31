desafio1. Função para verificar se o número é par
def verificar_par(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")

# Entrada do usuário
numero = int(input("Digite um número: "))
verificar_par(numero)
