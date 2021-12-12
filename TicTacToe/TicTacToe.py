a = input("Enter cells:")
print("---------")
print("|", a[0], a[1], a[2], "|")
print("|", a[3], a[4], a[5], "|")
print("|", a[6], a[7], a[8], "|")
print("---------")
n = a.count('X')
b = a.count('O')
c = a.count('_')
if a[0] == a[1] == a[2] and (a[3] == a[4] == a[5] or a[6] == a[7] == a[8]) or \
        a[0] == a[3] == a[6] and (a[1] == a[4] == a[7] or a[2] == a[5] == a[8]) or \
        a[3] == a[4] == a[5] and a[6] == a[7] == a[8] or \
        a[1] == a[4] == a[7] and a[2] == a[5] == a[8]:
    print("Impossible")
elif abs(n-b)>1:
    print("Impossible")
elif a[0] == a[1] == a[2] or a[0] == a[4] == a[8] or a[0] == a[3] == a[6]:
    print(a[0], "wins")
elif a[1] == a[4] == a[7] or a[3] == a[4] == a[5]:
    print(a[4], "wins")
elif a[6] == a[7] == a[8] or a[6] == a[4] == a[2]:
    print(a[6], "wins")
elif a[2] == a[5] == a[8]:
    print(a[2], "wins")
else:
    if abs(n-b)>1:
        print("Impossible2")
    if "_" in a:
        print("Game not finished")
    else:
        print("Draw")