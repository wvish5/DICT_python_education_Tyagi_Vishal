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
#Этап 5
money = 550
water = 400
milk = 540
beans = 120
cups = 9


class ResourceError(Exception):
    pass


def print_state():
    print()
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()


def select_action() -> str:
    return input('Write action (buy, fill, take, remaining, exit): ')


def select_flavor() -> int:
    print()
    response = input('What do you want to buy?'
                     ' 1 - espresso,'
                     ' 2 - latte,'
                     ' 3 - cappuccino,'
                     ' back - to main menu: ')
    if response == 'back':
        return 0
    return int(response)


def is_enough(need_water=0, need_milk=0, need_beans=0):
    if water < need_water:
        print('Sorry, not enough water!\n')
        raise ResourceError
    if milk < need_milk:
        print('Sorry, not enough milk!\n')
        raise ResourceError
    if beans < need_beans:
        print('Sorry, not enough beans!\n')
        raise ResourceError
    if cups < 1:
        print('Sorry, not enough cups\n')
        raise ResourceError
    print('I have enough resources, making you a coffee!\n')


def buy():
    global money, water, milk, beans, cups

    flavor = select_flavor()

    try:
        if flavor == 0:
            pass
        elif flavor == 1:  # espresso
            is_enough(need_water=250, need_beans=16)

            money += 4
            water -= 250
            beans -= 16
            cups -= 1
        elif flavor == 2:  # latte
            is_enough(need_water=350, need_milk=75, need_beans=20)

            money += 7
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
        elif flavor == 3:  # cappuccino
            is_enough(need_water=200, need_milk=100, need_beans=12)

            money += 6
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
        else:
            raise ValueError(f'Unknown flavor {flavor}')
    except ResourceError:
        pass


def fill():
    global water, milk, beans, cups

    print()
    water += int(input('Write how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    beans += int(input('Write how many grams of coffee beans'
                       ' do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee'
                      ' do you want to add: '))
    print()


def take():
    global money

    print()
    print(f'I gave you ${money}')
    print()

    money = 0


def main():
    while True:
        action = select_action()

        if action == 'buy':
            buy()
        elif action == 'fill':
            fill()
        elif action == 'take':
            take()
        elif action == 'exit':
            break
        elif action == 'remaining':
            print_state()
        else:
            raise ValueError(f'Unknown command {action}')


if __name__ == '__main__':
    main()
#Этап 6
water = 400
milk = 540
beans = 120
cups = 9
money = 550
task = ('buy', 'fill', 'take', 'remaining', 'exit', 'back')
print('Write action (buy, fill, take, remaining, exit): ')
x = input()
while x in task:
    espresso_water = 250
    espresso_milk = 0
    espresso_beans = 16
    espresso_cups = 1
    espresso_price = 4
    latte_water = 350
    latte_milk = 75
    latte_beans = 20
    latte_cups = 1
    latte_price = 7
    cappuccino_water = 200
    cappuccino_milk = 100
    cappuccino_beans = 12
    cappuccino_cups = 1
    cappuccino_price = 6
# Do we have enough to make one cup?
    make_espresso1 = water - espresso_water
    make_espresso2 = milk - espresso_milk
    make_espresso3 = beans - espresso_beans
    make_espresso4 = cups - espresso_cups
    espresso_min = min(make_espresso1, make_espresso2, make_espresso3, make_espresso4)
    make_latte1 = water - latte_water
    make_latte2 = milk - latte_milk
    make_latte3 = beans - latte_beans
    make_latte4 = cups - latte_cups
    latte_min = min(make_latte1, make_latte2, make_latte3, make_latte4)
    make_cappuccino1 = water - cappuccino_water
    make_cappuccino2 = milk - cappuccino_milk
    make_cappuccino3 = beans - cappuccino_beans
    make_cappuccino4 = cups - cappuccino_cups
    cappuccino_min = min(make_cappuccino1, make_cappuccino2, make_cappuccino3, make_cappuccino4)
# Run Machine
    if x == 'buy':
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
        b = input()
        if b == '1':
            if make_espresso1 >= 0 and make_espresso2 >= 0 and make_espresso3 >= 0 and make_espresso4 >= 0:
                print('I have enough resources, making you a coffee!')
                water = water - espresso_water
                milk = milk - espresso_milk
                beans = beans - espresso_beans
                cups = cups - espresso_cups
                money = money + espresso_price
            else:
                if espresso_min == make_espresso1:
                    print('Sorry, not enough water!')
                if espresso_min == make_espresso2:
                    print('Sorry, not enough milk!')
                if espresso_min == make_espresso3:
                    print('Sorry, not enough coffee beans')
                if espresso_min == make_espresso4:
                    print('Sorry, not enough disposable cups')
        elif b == '2':
            if make_latte1 >= 0 and make_latte2 >= 0 and make_latte3 >= 0 and make_latte4 >= 0:
                print('I have enough resources, making you a coffee!')
                water = water - latte_water
                milk = milk - latte_milk
                beans = beans - latte_beans
                cups = cups - latte_cups
                money = money + latte_price
            else:
                if latte_min == make_latte1:
                    print('Sorry, not enough water!')
                if latte_min == make_latte2:
                    print('Sorry, not enough milk!')
                if latte_min == make_latte3:
                    print('Sorry, not enough coffee beans')
                if latte_min == make_latte4:
                    print('Sorry, not enough disposable cups')
        elif b == '3':
            if make_cappuccino1 >= 0 and make_cappuccino2 >= 0 and make_cappuccino3 >= 0 and make_cappuccino4 >= 0:
                print('I have enough resources, making you a coffee!')
                water = water - cappuccino_water
                milk = milk - cappuccino_milk
                beans = beans - cappuccino_beans
                cups = cups - cappuccino_cups
                money = money + cappuccino_price
            else:
                if cappuccino_min == make_cappuccino1:
                    print('Sorry, not enough water!')
                if cappuccino_min == make_cappuccino2:
                    print('Sorry, not enough milk!')
                if cappuccino_min == make_cappuccino3:
                    print('Sorry, not enough coffee beans')
                if cappuccino_min == make_cappuccino4:
                    print('Sorry, not enough disposable cups')
        else:
            ()
    elif x == 'fill':
        print('Write how many ml of water do you want to add: ')
        water_fill = int(input())
        print('Write how many ml of milk do you want to add: ')
        milk_fill = int(input())
        print('Write how many grams of coffee beans do you want to add: ')
        beans_fill = int(input())
        print('Write how many disposable cups of coffee do you want to add: ')
        cups_fill = int(input())
        water = water + water_fill
        milk = milk + milk_fill
        beans = beans + beans_fill
        cups = cups + cups_fill
        money = money + 0
    elif x == 'take':
        print('I gave you $' + str(money))
        water = water + 0
        milk = milk + 0
        beans = beans + 0
        cups = cups + 0
        money = 0
    elif x == 'remaining':
        print('The coffee machine has:')
        print(str(water) + ' of water')
        print(str(milk) + ' of milk')
        print(str(beans) + ' of coffee beans')
        print(str(cups) + ' of disposable cups')
        print('$' + str(money) + ' of money')
    elif x == 'exit':
        exit()
    print('Write action (buy, fill, take, remaining, exit): ')
    x = input()
















