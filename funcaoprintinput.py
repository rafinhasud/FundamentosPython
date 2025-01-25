import math

#pedir ao utilizador um número inteiro e devolver a sua raiz quadrada

numero = int(input("Introduza um número inteiro"))
#numero=int(numero)
raizquadrada = math.sqrt(numero)

print(f"A raíz quadrada do número: {numero} é igual a, {round(raizquadrada,2)}")