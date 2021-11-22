water = int(input('Write how many water the coffee machine has: '))
beans = int(input('Write how many beans the coffee machine has: '))
milk = int(input('Write how many milk the coffee machine has: '))
cups = int(input("Write how many cups of coffee you will need: "))
m = milk // 50
b = beans // 15
w = water // 250
a = [m, b, w]
n = min(a)
if cups == n:
    print("Yes,I can make this amount of coffee")
else:
    if cups > n:
        print(f"No,I can make only {n} cups of coffee")
    else:
        print(f"Yes,I can make that amount of coffee (and even {n - cups} more than that")

