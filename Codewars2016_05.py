info = []
separado = []
cuentaW = 0
cuentaZ = 0
while True:
	y = input()
	if y != "#":
		info.append(y)
	else:
		break

for i in range(len(info)):
	separado.append(info[i].split())

for i in separado:
	if int(i[1]) > int(i[2]):
		if i[0] == "W":
			cuentaW += 1
		if i[0] == "Z":
			cuentaZ += 1
		else:
			continue

print(cuentaW, "fines to Whynot")
print(cuentaZ, "fines to Zzyzx")
if cuentaW < cuentaZ:
	print("Whynot inhabitants are safer at driving than Zzyzx ones")
elif cuentaW > cuentaZ:
	print("Zzyzx inhabitants are safer at driving than Whynot ones")
else:
	print("Whynot and Zzyzx inhabitants are equally safe at driving")