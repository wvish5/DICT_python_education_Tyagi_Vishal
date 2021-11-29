print('X O X')
print('O X O')
print('X X O')
x = (list(input()))
board = '---------\n| ' + x[0] + ' ' + x[1] + ' ' + x[2] + ' | \n| ' + x[3] + ' ' + x[4] + ' ' + x[5] + ' | \n| ' + x[6] + ' ' + x[7] + ' ' + x[8] + ' | \n---------'
print(board)
def seq(inp):
    print("---------")
    print("|", " ".join(inp[0:3]), "|")
    print("|", " ".join(inp[3:6]), "|")
    print("|", " ".join(inp[6:9]), "|")
    print("---------")

def whowon(inp, var):
    win = []
    for x in wins:
        win.append(len([y for y in x if inp[y] == var]))
    return win.count(3)

ini = list(input().replace(" ", "_"))
seq(ini)

wins = [[0, 4, 8], [2, 4, 6], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]

x_win = whowon(ini,"X")
y_win = whowon(ini,"O")

if abs(ini.count("X") - ini.count("O")) >= 2 or (x_win == 1 and y_win == 1):
    print("Impossible")
elif x_win == 1:
    print("X wins")
elif y_win == 1:
    print("O wins")
elif x_win == 0 and y_win == 0 and ini.count("_") != 0:
    print("Game not finished")
else:
    print("Draw")
user_input = list(input("Enter cells: "))
matrix = []
k = 0
def show():
    global matrix
    print("---------")
    for i in range(0, 3):
        print("|", end="")
        for j in range(0, 3):
            print(" " + matrix[i][j], end="")
        print(" |")
    print("---------")

for i in range (0,3):
    matrix.append([])
    for j in range (0,3):
        matrix[i].append(user_input[k])
        k += 1

show()

while True:
    x, y = input("Enter the coordinates: ").split()
    try:
        x = int(x)
        y = int(y)
        if x < 1 or y > 3 or x < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            if matrix[abs(y-3)][abs(x-1)] == "_":
                matrix[abs(y-3)][abs(x-1)] = "X"
                show()
                break
            else:
                print("This cell is occupied! Choose another one!")
    except:
        print("You should enter numbers!")
a = list(" " * 9)
step = 0
def printgame():
    print('-' * 9)
    for i in range(3):
        print("| {} {} {} |".format(a[0 + 3 * i], a[1 + 3 * i], a[2 + 3 * i]))
    print('-' * 9)
while " " in a:
    playx, playy = input("Enter the coordinates:").split()
    if (int(playx) or int(playy)) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("You should enter numbers!")
    elif (int(playx) or int(playy)) not in [1, 2, 3]:
        print("Coordinates should be from 1 to 3!")
    elif a[(int(playx) - 1) + abs(int(playy) - 3) * 3] != " ":
        print("This cell is occupied! Choose another one!")
    else:
        if step == 0:
            a[(int(playx) - 1) + abs(int(playy) - 3) * 3] = "X"
            step = 1
        elif step == 1:
            a[(int(playx) - 1) + abs(int(playy) - 3) * 3] = "O"
            step = 0
        printgame()
        rule = [a[:3], a[3:6], a[6:], a[0:9:3], a[1:9:3], a[2:9:3], a[0:9:4], a[2:7:2]]
        if ['X', 'X', 'X'] in rule:
            print("X wins")
        elif ['O', 'O', 'O'] in rule:
            print("O wins")
        elif a.count(" ") == 0:
            print("Draw")