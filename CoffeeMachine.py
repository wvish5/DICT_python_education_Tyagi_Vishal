print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")
cups = int(input('Write how many cups of coffee you will need: '))
water = 200 * cups
milk = 50 * cups
beans = 15 * cups
print(f'For {cups} cups of coffee you will need:')
print(f'{water} ml of water')
print(f'{milk} ml of milk')
print(f'{beans} g of coffee beans')
def count(water: int, milk: int, beans: int, cups: int) -> str:
    possible = min([
        water // 200,
        milk // 50,
        beans // 15
    ])

    if possible == cups:
        message = 'Yes, I can make that amount of coffee'
    elif possible > cups:
        message = f'Yes, I can make that amount of coffee' \
                  f' (and even {possible - cups} more than that)'
    else:
        message = f'No, I can make only {possible} cups of coffee'

    return message

water = int(input('Write how many ml of water the coffee machine has: '))
milk = int(input('Write how many ml of milk the coffee machine has: '))
beans = int(input('Write how many grams of coffee beans'' the coffee machine has: '))
cups = int(input('Write how many cups of coffee you will need: '))

print(count(water, milk, beans, cups))





