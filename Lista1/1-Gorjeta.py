#Garçom receberá 10% do total consumido no restaurante

n = int(input("Insira quantos itens foram consumidos: "))
print(f"\nForam consumidos {n} produtos")

soma = 0

for i in range(n):
  a = float(input(f"Insira o valor do {i+1}º item: "))
  soma = soma + a

print("A soma total dos produtos foi: R$", soma)

garçom = soma * 0.10
print("\nO garçom receberá: R$ ", garçom)