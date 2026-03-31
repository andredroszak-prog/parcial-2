def segundos_para_hms(segundos):
    horas = segundos // 3600  # 1 hora = 3600 segundos
    minutos = (segundos % 3600) // 60  # 1 minuto = 60 segundos
    segundos_restantes = segundos % 60  # O restante é o número de segundos

    return horas, minutos, segundos_restantes

# Testando
segundos = int(input("Digite o número de segundos: "))
horas, minutos, segundos_restantes = segundos_para_hms(segundos)
print(f"{segundos} segundos equivalem a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
Código 2: Converter horas, minutos e segundos para segundos
def hms_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

# Testando
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))

total_segundos = hms_para_segundos(horas, minutos, segundos)
print(f"{horas} horas, {minutos} minutos e {segundos} segundos equivalem a {total_segundos} segundos.")
Como funciona:
Primeiro código: Recebe um número de segundos e calcula quantas horas, minutos e segundos correspondem a esse número. Ele usa divisão inteira (//) para calcular as horas e minutos, e o operador módulo (%) para obter o restante.
Segundo código: Recebe horas, minutos e segundos e converte para o total de segundos. Multiplica as horas por 3600 (segundos por hora), os minutos por 60 (segundos por minuto) e soma tudo.

Você pode testar ambos para ver a conversão funcionando!
