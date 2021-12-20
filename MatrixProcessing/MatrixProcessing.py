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

def multiplication():
    c = int(input())
    for i in range(n1):
        for j in range(m1):
            matrix_A[i][j] *= c


def output():
    for i in range(n1):
        print(*matrix_A[i], sep=" ")

matrixA()
multiplication()
output()