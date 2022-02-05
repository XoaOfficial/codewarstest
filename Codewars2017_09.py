needed = input()
found = input()

neededlist = needed.split( )
foundlist = found.split( )

neededlist = [int(x) for x in neededlist]
foundlist = [int(x) for x in foundlist]

if neededlist[0] <= foundlist[0] and neededlist[1] <= foundlist[1]:
    print("yes")
elif neededlist[0] <= foundlist[1] and neededlist[1] <= foundlist[0]:
    print("yes")
else:
    print("no")