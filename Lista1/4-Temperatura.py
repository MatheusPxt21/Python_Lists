resposta = 's'

while(resposta != 'n'):
  de = int(input("Qual unidade deseja converter?\n(1 - Celsius)\n(2 - Fahrenheit)\n(3 - Kelvin)\n"))

  para = int(input("Para qual unidade deseja converter?\n(1 - Celsius)\n(2 - Fahrenheit)\n(3 - Kelvin)\n"))

  if(de == para):
    print("você selecionou unidades iguais")
    print("A temperatura será a mesma")
    
  else:
    temperatura = float(input("Insira a temperatura: \n(apenas números e ponto, caso necessário)\n "))

    if(de == 1 and para == 2):
      print("Você selecionou a conversão de Celsius para Fahrenheit\n")
      Fahrenheit = (temperatura * 1.8) + 32
      print(f"{temperatura}°C = {Fahrenheit}°F")
    
    if(de == 1 and para == 3):
      print("Você selecionou a conversão de Celsius para Kelvin\n")
      Kelvin = 273.15 + temperatura
      print(f"{temperatura}°C = {Kelvin}K")
    
    if (de == 2 and para == 1):
      print("Você selecionou a conversão de Fahrenheit para Celsius\n")
      Celsius = (temperatura - 32) * (5/9)
      print(f"{temperatura}°F = {Celsius}°C")
    
    if (de == 2 and para == 3):
      print("Você selecionou a conversão de Fahreinheit para Kelvin\n")
      Kelvin = ((temperatura - 32) * (5/9)) + 273.15
      print(f"{temperatura}°F = {Kelvin}K")

    if(de == 3 and para == 1):
      print("Você selecionou a conversão de Kelvin para Celsius\n")
      Celsius = temperatura - 273.15
      print(f"{temperatura}K = {Celsius}°C")

    if(de == 3 and para == 2):
      print("Você selecionou a conversão de Kelvin para Fahrenheit\n")
      Fahrenheit = ((temperatura - 273.15) * 1.8) + 32
      print(f"{temperatura}K = {Fahrenheit}°F")
    
  
  resposta = input("Deseja fazer novamente? (s = sim)(n = não): ")

print("====================================================")
print("Fim do programa!")
print("====================================================")