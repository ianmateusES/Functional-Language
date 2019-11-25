# Faça um programa que recebe uma lista de inteiros e 
# imprime somente os números que não
# são primos.

not_primo = lambda x: list(filter(lambda num: x % num == 0 , range(2, x)))

print(list(filter(not_primo, list(map(int, input("Numeros:\n").split(" "))))))