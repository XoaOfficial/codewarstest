info = []
sumaimpar = 0
sumapar = 0
while True:
	y = int(input())
	if y != 0:
		info.append(y)
	else:
		break

for i in range(len(info)):
	for j in range(len(str(info[i]))):
		if j % 2 == 0:
			sumapar += info[i][j]
		if j % 2 == 1:
			sumaimpar += info[i][j]
	if sumapar == sumaimpar:
		print(i, "is a balanced number")
	else:
		print(i, "is not a balanced number")