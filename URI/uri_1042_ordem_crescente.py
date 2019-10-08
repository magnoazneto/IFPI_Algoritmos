def main():
	lista = input().split()
	original = []
	for c in range(0, 3):
		original.append(int(lista[c]))
	crescente = original[:]
	crescente.sort()
	for c in range(0, 3):
		print(crescente[c])
	print()
	for c in range(0, 3):
		print(original[c])


main()