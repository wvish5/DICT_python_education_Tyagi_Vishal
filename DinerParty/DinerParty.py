from random import choice
count = int(input("Enter the number of friends joining (including you):"))
n = {}

sh = []
if count >= 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(count):
        name = input()
        n[name] = 0
        sh.append(name)

else:
    print("No one is joining for the party")
summa = int(input("Enter the total amount:"))
certain = round(summa / count, 2)
    print("No one is joining for the party")
summa = int(input("Enter the total amount: "))
fact = round(summa / count, 2)
for name in n:
    n[name] = certain
sh_name = choice(sh)
question = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
if question == "Yes":
    n[name] = fact
sh_name = choice(sh)
question = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No ")
if question == "Yes" or "yes":
    print(sh_name, "Is Lucky one!")
    n[sh_name] = 0
    print(n)
else:
    print("No one is going to be lucky")
    print("No one is going to be lucky\n", n)
