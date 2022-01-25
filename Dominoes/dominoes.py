import random

def definite():
    global stock, computer, player, snake
    all_domino = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                  [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6],
                  [5, 5], [5, 6], [6, 6]]
    al = random.sample(all_domino, 28)
    stock, computer, player, snake = al[:14], al[14:21], al[21:], []

def domino_snake():
    global status
    max_computer, max_player, exseption = (0,0), (0,0), 0
    for i in range(7):
        if computer[i][0] == computer[i][1]:
            if computer[i][0]>max_computer[0]:
                max_computer = computer[i]
                exseption += 1
    for j in range(7):
        if player[j][0] == player[j][1]:
            if player[j][0]>max_player[0]:
                max_player = player[j]
                exseption += 1
    if exseption == 0:
        main()
    else:
        if max_computer[0]>max_player[0]:
            snake.append(max_computer)
            computer.remove(max_computer)
            status = "player"
        else:
            snake.append(max_player)
            player.remove(max_player)
            status = "computer"

def main():
    print("="*70)
    print(f"Stock pieces: {len(stock)}\n"
          f"Computer pieces: {len(computer)}\n")
    output_snake()
    print()
    print("Your pieces:")
    for i in range(len(player)):
        print(f"{str(i+1)}:{player[i]}")
    finish()
    if status=="computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        computer_move()
    else:
        print("\nStatus: It's your turn to make a move. Enter your command.")
        player_move()

def player_move():
    global status
    move = input()
    try:
        move = int(move)
    except ValueError:
        print("Invalid input. Please try again.")
        player_move()

    if 0<abs(move)<=len(player):
        if "-" in str(move-1):
            snake.insert(0, player[abs(move)-1])
            a = player[abs(move)-1]
            player.remove(a)
        elif "-" not in str(move-1):
            snake.append(player[move-1])
            a = player[move-1]
            player.remove(a)
    elif move==0:
        a = random.choice(stock)
        player.append(a)
        stock.remove(a)
    else:
        print("Invalid input. Please try again.")
        player_move()
    status = "computer"
    main()

def computer_move():
    global status
    a = input()
    move = random.randint(-len(computer), len(computer))
    if "-" in str(move) and move!=0:
        snake.insert(0, computer[abs(move)-1])
        a = computer[abs(move)-1]
        computer.remove(a)
    elif "-" not in str(move) and move!=0:
        snake.append(computer[move-1])
        a = computer[move-1]
        computer.remove(a)
    elif move==0:
        a = random.choice(stock)
        computer.append(a)
        stock.remove(a)
    status = "player"
    main()

def finish():
    if len(snake)>4:
        if snake[0][0]==snake[-1][-1]:
            total = snake[0][0]
            for i in range(len(snake)):
                for j in range(2):
                    if total==snake[i][j]:
                        total +=1
            if total==8:
                print("Status: The game is over. It's a draw!")
                quit()
    if len(computer)==0:
        print("Status: The game is over. The computer won!")
        quit()
    elif len(player)==0:
        print("Status: The game is over. You won!")
        quit()

def output_snake():
    if len(snake)<=6:
        print(*snake, sep=" ")
    else:
        print(f"{snake[0]}{snake[1]}{snake[2]}...{snake[-3]}{snake[-2]}{snake[-1]}")

definite()
domino_snake()
main()