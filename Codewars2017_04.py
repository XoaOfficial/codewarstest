n = int(input())
m = int(input())
suma1 = 0
suma2 = 0

for i in range(m):
    suma1 += n+i+1
    suma2 += n-i-1

print(suma1,suma2)