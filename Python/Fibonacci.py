# Faça um programa que recebe um inteiro n e 
# imprima os n primeiros termos da sequência
# de Fibonacci
# F(n+2) = F(n+1) + F(n), n>= 1 e F(1) = F(2) = 1

Fibonacci = lambda x: (x == 1 and 1) or (x == 2 and 1) or (Fibonacci(x-2) + Fibonacci(x-1))

print(list(map(Fibonacci, range(1, int(input("NumeroIntero\n"))+1) ) ) )