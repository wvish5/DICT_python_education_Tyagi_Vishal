from numpy import matrix, rot90, fliplr, flipud


class Matrix:
    def __init__(self, name):
        self.name = name
        self.n, self.m = None, None
        self.matrix = None

    def matrix_reader(self):
        self.n, self.m = map(int, input(f'Enter size of {self.name}matrix: ').split())
        print(f'Enter {self.name}matrix:')
        self.matrix = matrix([list(map(float, input().split())) for _ in range(self.n)])

    def __eq__(self, other):
        return self.n == other.n and self.m == other.m

    def __add__(self, other):
        return self.matrix + other.matrix

    def mul(self, number):
        return self.matrix * number

    def __mul__(self, other):
        return self.matrix * other.matrix

    def print_matrix(self):
        for col in self.matrix.tolist():
            print(*col)


while True:
    print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n0. Exit')
    choice = int(input('Your choice: '))
    if choice == 0:
        exit()
    if choice == 1:
        first = Matrix('first ')
        first.matrix_reader()
        second = Matrix('second ')
        second.matrix_reader()
        print('The result is:')
        if first == second:
            result = Matrix('')
            result.matrix = first + second
            result.print_matrix()
        else:
            print('The operation cannot be performed.')
    if choice == 2:
        first = Matrix('')
        first.matrix_reader()
        const = float(input('Enter constant: '))
        result = Matrix('')
        result.matrix = first.mul(const)
        print('The result is:')
        result.print_matrix()
    if choice == 3:
        first = Matrix('first ')
        first.matrix_reader()
        second = Matrix('second ')
        second.matrix_reader()
        print('The result is:')
        if first.m == second.n:
            result = Matrix('')
            result.matrix = first * second
            result.print_matrix()
        else:
            print('The operation cannot be performed.')
    if choice == 4:
        print('1. Main diagonal', '2. Side diagonal',
              '3. Vertical line', '4. Horizontal line')
        choice_ = int(input('Your choice: '))
        first = Matrix('')
        first.matrix_reader()
        print('The result is:')
        result = Matrix('')
        if choice_ == 1:
            result.matrix = first.matrix.T
        if choice_ == 2:
            result.matrix = rot90(rot90(first.matrix).T, 3)
        if choice_ == 3:
            result.matrix = fliplr(first.matrix)
        if choice_ == 4:
            result.matrix = flipud(first.matrix)
        result.print_matrix()