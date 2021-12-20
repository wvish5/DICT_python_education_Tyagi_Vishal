def menu():
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit")
    choice = int(input("Your choice: "))
    if choice == 1:
        cho_add()
    if choice == 2:
        cho_multiply_constant()
    if choice == 3:
        cho_multiply()
    if choice == 0:
        quit()


def cho_add():
    q = input("Enter size of first matrix: ").split(" ")
    if len(q) > 1:
        nA = int(q[0])
        mA = int(q[1])
    else:
        print("The operation cannot be performed.")
        print()
        menu()
    print("Enter first matrix:")
    matrix_A = [list(map(float, input().split(" "))) for _ in range(nA)]
    nB, mB = [int(y) for y in input("Enter size of second matrix: ").split(" ")]
    print("Enter second matrix:")
    matrix_B = [list(map(float, input().split(" "))) for _ in range(nB)]

    if nA != nB and nB != mB:
        print("The operation cannot be performed.")
        print()
        menu()
    print("The result is:")
    for i in range(nA):
        for j in range(mA):
            matrix_A[i][j] += matrix_B[i][j]
    for ii in range(nA):
        print(*matrix_A[ii], sep=" ")
    print()
    menu()


def cho_multiply_constant():
    n, m = [int(x) for x in input("Enter size of matrix: ").split(" ")]
    print("Enter matrix:")
    matrix = [list(map(float, input().split(" "))) for _ in range(n)]
    c = float(input("Enter constant: "))
    print("The result is:")
    for i in range(n):
        for j in range(n):
            matrix[i][j] *= c
    for ii in range(n):
        print(*matrix[ii], sep=" ")
    print()
    menu()


def cho_multiply():
    nA, mA = [int(x) for x in input("Enter size of first matrix: ").split(" ")]
    print("Enter first matrix:")
    m_A = [list(map(float, input().split(" "))) for _ in range(nA)]

    nB, mB = [int(x) for x in input("Enter size of second matrix: ").split(" ")]
    print("Enter second matrix:")
    m_B = [list(map(float, input().split(" "))) for _ in range(nB)]

    if mA != nB:
        print("The operation cannot be performed.")
        print()
        menu()
    matrix = []
    for w in range(nB):
        matrix.append([])
        for ww in range(mB):
            matrix[w].append(0)

    for i in range(nA):  # i=0  j=1  k=0
        for j in range(mB):
            for k in range(nB):
                matrix[i][j] += m_A[i][k] * m_B[k][j]

    print("The result is:")
    for ii in range(nA):
        print(*matrix[ii], sep=" ")
    print()
    menu()


menu()