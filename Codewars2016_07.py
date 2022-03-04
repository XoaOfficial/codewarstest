def dec_to_base(num, base):
    if num == 0:
        return 0
    base_num = ""
    while num > 0:
        dig = int(num % base)
        if dig < 10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)
        num //= base
    base_num = base_num[::-1]  # Inverts order?
    return int(base_num)

info = input()
separado = [letter for letter in info if letter != ":"]
base2 = []
v2 = []
output = ["","","",""]

for i in separado:
	base2.append(dec_to_base(int(i), 2))
for i in base2:
	j = str(i)
	while len(j) < 4:
		j = "0" + j
	v2.append(j)

for i in range(6):
	for j in range(4):
		if v2[i][j] == "1":
			output[j] = output[j] + "o"
		if v2[i][j] == "0":
			output[j] = output[j] + "-"
		output[j] = output[j] + " "

for i in range(4):
	print(output[i])