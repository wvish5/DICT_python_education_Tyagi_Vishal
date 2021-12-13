a = input("Enter cells: ").replace("_", " ")
a = list(a)


def game_grid():
    print("---------")
    print("|", a[0], a[1], a[2], "|")
    print("|", a[3], a[4], a[5], "|")
    print("|", a[6], a[7], a[8], "|")
    print("---------")


def change():
    global a, q, q1, q2
    q = input("Enter the coordinates: ").split(" ")
    q1 = q[0]
    q2 = q[1]
    def check(q1, q2):
        global pos
        if q1 == "1" and q2 == "1":
            pos = a[0]
            return pos
        elif q1 == "1" and q2 == "2":
            pos = a[1]
            return pos
        elif q1 == "1" and q2 == "3":
            pos = a[2]
            return pos
        elif q1 == "2" and q2 == "1":
            pos = a[3]
            return pos
        elif q1 == "2" and q2 == "2":
            pos = a[4]
            return pos
        elif q1 == "2" and q2 == "3":
            pos = a[5]
            return pos
        elif q1 == "3" and q2 == "1":
            pos = a[6]
            return pos
        elif q1 == "3" and q2 == "2":
            pos = a[7]
            return pos
        elif q1 == "3" and q2 == "3":
            pos = a[8]
            return pos
    if check(q1, q2) != " ":
        print("This cell is occupied! Choose another one!")
        change()
    elif q1 not in "0123456789" or q2 not in "0123456789":
        print("You should enter numbers!")
        change()
    elif q1 not in "123" or q2 not in "123":
        print("Coordinates should be from 1 to 3!")
        change()
    else:
        if q1 == "1" and q2 == "1":
            a[0] = "X"
        elif q1 == "1" and q2 == "2":
            a[1] = "X"
        elif q1 == "1" and q2 == "3":
            a[2] = "X"
        elif q1 == "2" and q2 == "1":
            a[3] = "X"
        elif q1 == "2" and q2 == "2":
            a[4] = "X"
        elif q1 == "2" and q2 == "3":
            a[5] = "X"
        elif q1 == "3" and q2 == "1":
            a[6] = "X"
        elif q1 == "3" and q2 == "2":
            a[7] = "X"
        elif q1 == "3" and q2 == "3":
            a[8] = "X"
        game_grid()


game_grid()
change()