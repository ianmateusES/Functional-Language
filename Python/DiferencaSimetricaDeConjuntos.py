# Faça um programa que recebe duas listas A e B e 
# imprime a diferença simétrica de A e B. A
# diferença simétrica de A e B é dada por 
# (A - B) U (B - A).

pertence = lambda x, l: (len(l) > 0) and (l[0] == x or pertence(x,l[1:]))
dif_simetrica = lambda l1, l2: list(filter((lambda x: not(pertence(x,l2))), l1)) + list(filter((lambda x: not(pertence(x,l1))), l2))

print(dif_simetrica(list(map(int, input("Lista1:\n").split(" "))),  list(map(int, input("Lista1:\n").split(" ")) )))