def matrixA():
    global matrix_A, n1, m1
    q = input().split(" ")
    n1, m1, = int(q[0]), int(q[1])
    matrix_A = []
    for t in range(n1):
        matrix_A.append([])
    for i in range(n1):
        q = input().split(" ")
        matrix_A[i] = [int(j) for j in q]

def matrixB():
    global matrix_B, n2, m2
    q = input().split(" ")
    n2, m2, = int(q[0]), int(q[1])
    matrix_B = []
    for t in range(n2):
        matrix_B.append([])
    for i in range(n2):
        q = input().split(" ")
        matrix_B[i] = [int(j) for j in q]

def check():
    if n1==n2 and m1==m2:
        matrixSum()
    else:
        print("ERROR")
        quit()

def matrixSum():
    for i in range(n2):
        for j in range(m2):
            matrix_A[i][j] += matrix_B[i][j]

def output():
    for i in range(n1):
        print(*matrix_A[i], sep=" ")

matrixA()
matrixB()
check()
output()