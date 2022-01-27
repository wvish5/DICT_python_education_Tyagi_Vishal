count = int(input("Enter the number of friends joining (including you):"))
n = {}
if count >= 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(count):
        name = input()
        n[name] = 0
else:
    print("No one is joining for the party")
print(n)
