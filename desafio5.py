# Função para calcular a área de um triângulo
def area_do_triangulo(base, altura):
    return (base * altura) / 2

# Exemplo de uso
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

area = area_do_triangulo(base, altura)

print(f"A área do triângulo é: {area}")
