def inverso(texto):
    inv = ""
    for caracter in texto:
        inv = caracter + inv
    return inv

original = []
while 1<2:
    a = input()
    if a != "#":
        original.append(a)
    else:
        break

for i in original:
    print(inverso(i))