#Этап 1
print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready")
#Этап 2
def main():
    cups = int(input('Write how many cups of coffee you will need: '))

    # One cup: 200 ml of water, 50 ml of milk, and 15 g of coffee beans
    water = 200 * cups
    milk = 50 * cups
    beans = 15 * cups

    print(f'For {cups} cups of coffee you will need:')
    print(f'{water} ml of water')
    print(f'{milk} ml of milk')
    print(f'{beans} g of coffee beans')


if __name__ == '__main__':
    main()
#Этап 3
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


def main():
    water = int(input('Write how many ml of water the coffee machine has: '))
    milk = int(input('Write how many ml of milk the coffee machine has: '))
    beans = int(input('Write how many grams of coffee beans'
                      ' the coffee machine has: '))
    cups = int(input('Write how many cups of coffee you will need: '))

    print(count(water, milk, beans, cups))


if __name__ == '__main__':
    main()
#Этап 4
money = 550
water = 1200
milk = 540
beans = 120
cups = 9


def print_state():
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()


def select_action() -> str:
    return input('Write action (buy, fill, take): ')


def select_flavor() -> int:
    return int(input('What do you want to buy?'
                     ' 1 - espresso, 2 - latte, 3 - cappuccino: '))


def buy():
    global money, water, milk, beans, cups

    flavor = select_flavor()
    if flavor == 1:  # espresso
        assert water >= 250
        assert beans >= 16

        money += 4
        water -= 250
        beans -= 16
    elif flavor == 2:  # latte
        assert water >= 350
        assert milk >= 75
        assert beans >= 20

        money += 7
        water -= 350
        milk -= 75
        beans -= 20
    elif flavor == 3:  # cappuccino
        assert water >= 200
        assert milk >= 100
        assert beans >= 12

        money += 6
        water -= 200
        milk -= 100
        beans -= 12
    else:
        raise ValueError(f'Unknown flavor {flavor}')

    cups -= 1


def fill():
    global water, milk, beans, cups

    water += int(input('Write how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    beans += int(input('Write how many grams of coffee beans'
                       ' do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee'
                      ' do you want to add: '))


def take():
    global money

    print(f'I gave you ${money}')
    money = 0


def main():
    print_state()

    action = select_action()

    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    else:
        raise ValueError(f'Unknown command {action}')

    print()
    print_state()


if __name__ == '__main__':
    main()
















