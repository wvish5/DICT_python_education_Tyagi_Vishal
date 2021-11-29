money = 550
water = 400
milk = 540
beans = 120
cups = 9


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
    Status = False
    if water < need_water:
        print('Sorry, not enough water!\n')
        Status = True
    if milk < need_milk:
        print('Sorry, not enough milk!\n')
        Status = True
    if beans < need_beans:
        print('Sorry, not enough beans!\n')
        Status = True
    if cups < 1:
        print('Sorry, not enough cups\n')
        Status = True
    return Status



def buy():
    global money, water, milk, beans, cups

    flavor = select_flavor()

    try:
        if flavor == 0:
            pass
        elif flavor == 1:  # espresso
            Status = is_enough(need_water=250, need_beans=16)
            if Status == False:
                money += 4
                water -= 250
                beans -= 16
                cups -= 1
                print('I have enough resources, making you a coffee!\n')
        elif flavor == 2:  # latte
            Status = is_enough(need_water=350, need_milk=75, need_beans=20)
            if Status == False:
                money += 7
                water -= 350
                milk -= 75
                beans -= 20
                cups -= 1
                print('I have enough resources, making you a coffee!\n')
        elif flavor == 3:  # cappuccino
            Status = is_enough(need_water=200, need_milk=100, need_beans=12)
            if Status == False:
                money += 6
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
                print('I have enough resources, making you a coffee!\n')
        else:
            print(f'Unknown flavor{flavor}')
    except:
        print("Error")


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
            print(f'Unknown command {action}')


if __name__=="__main__":
    main()
