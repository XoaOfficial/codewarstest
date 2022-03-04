info = []
separado = []
votos = []
while True:
	y = input()
	if y != "0":
		info.append(y)
	else:
		break

for i in range(len(info)):
	separado.append(info[i].split())

for i in range(len(separado)):
	for j in range(3):
		separado[i][j] = int(separado[i][j])

for i in range(15):
	votos.append(0)

for i in separado:
	votos[i[0]] += 3
	votos[i[1]] += 2
	votos[i[2]] += 1

print(votos.index(sorted(votos)[-1]), sorted(votos)[-1])
print(votos.index(sorted(votos)[-2]), sorted(votos)[-2])
print(votos.index(sorted(votos)[-3]), sorted(votos)[-3])