# Faça um programa que recebe um inteiro n e uma string s como entrada e imprime uma
# nova string com cada vogal (letras ‘a’, ‘e’, ‘i’, ‘o’, ‘u’ minúsculas ou maiúsculas) repetida n
# vezes, os outros caracteres devem permanecer inalterados. Por exemplo, se s = “quixada” e
# n = 3, seu programa deve imprimir “quuuiiixaaadaaa”.

rep_vogal = lambda vogal, qtd: (qtd > 0) and (vogal + rep_vogal(vogal, qtd-1)) or ""
proc_vogal = lambda plv, qtd: (len(plv) > 0 or "") and (((plv[0]=="A" or plv[0]=="a" or plv[0]=="E" or plv[0]=="e" or plv[0]=="I" or plv[0]=="i" or plv[0]=="O" or plv[0]=="o" or plv[0]=="U" or plv[0]=="u") and rep_vogal(plv[0],qtd) + proc_vogal(plv[1:], qtd)) or (plv[0] + proc_vogal(plv[1:],qtd)))

print(proc_vogal(input("Palavra:\n"), int(input("Quantidade:\n"))))