print("Digite 10 números:")
n1 = int(input("1º número: "))
n2 = int(input("2º número: "))
n3 = int(input("3º número: "))
n4 = int(input("4º número: "))
n5 = int(input("5º número: "))
n6 = int(input("6º número: "))
n7 = int(input("7º número: "))
n8 = int(input("8º número: "))
n9 = int(input("9º número: "))
n10 = int(input("10º número: "))

lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
print("Lista original:", lista)

trocou = True
while trocou:
    trocou = False
    for i in range(9):
        if lista[i] > lista[i+1]:
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
            trocou = True

print("Lista ordenada:", lista)

lista_sem_repetir = []
for num in lista:
    if num not in lista_sem_repetir:
        lista_sem_repetir.append(num)

print("Lista sem repetir:", lista_sem_repetir)

