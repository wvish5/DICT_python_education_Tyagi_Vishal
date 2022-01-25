import random
def definite():
    global stock, computer, player
    all_domino = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                  [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6],
                  [5, 5], [5, 6], [6, 6]]
    al = random.sample(all_domino, 28)
    stock, computer, player = al[:14], al[14:21], al[21:]
    domino_snake()

def domino_snake():
    global snake
    max_computer, max_player, exseption = (0,0), (0,0), 0
    snake = []
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
        else:
            snake.append(max_player)
            player.remove(max_player)

def main():
    definite()
    print("="*70)
    status = "player" if len(computer)==6 else "computer"
    print(f"Stock pieces: {len(stock)}\n"
          f"Computer pieces: {len(computer)}\n\n"
          f"{snake[0]}\n")
    for i in range(len(player)):
        print(f"{str(i+1)}:{player[i]}")
    if status=="computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")
main()