a = 's'

while(a != 'n'):
  km_por_litro = float(input("Insira quantos quilômetros o carro percorre com 1L de combustível: "))

  velocidade_media = float(input("Insira a velocidade média da viagem (em km/h): "))
  tempo = float(input("Insira o tempo gasto na viagem (em horas): "))
  distancia = velocidade_media * tempo

  consumo = distancia / km_por_litro

  print(f"O carro consumiu {consumo}L de combustível nessa viagem")

  a = input("Deseja continuar? (s = sim)(n = não)\n")

print("====================================================")
print("Fim do programa!")
print("====================================================")