def myRound(n, decimals=0):
	if decimals < 0:
		a = 1 / 0
		# If you ended up here its because you tried a negative number of decimals
	elif round(decimals) - decimals != 0:
		a = 1 / 0
		# if you ended up here its because you tried a not whole number of decimals
	elif decimals == 0:
		return str(round(n))
	elif type(n) == type(123):
		return str(n) + "." + "0"*decimals
	elif type(n) == type(12.34):
		ret = str(round(n, decimals))
		n_decimals = len(ret) - ret.index(".") - 1
		ret += "0"*(decimals - n_decimals)
		return ret

a = input()
b = int(input())

if a == "M":
    if b < 44:
        print(myRound(b-34.5, 1))
    else:
            print(myRound(b-35, 1))
else:
    if b < 40:
        print(myRound(b-31.5, 1))
    else:
        print(myRound(b-32, 1))