import random
def first():
    first = input('Кто ходит первым (1 - компьютер, 2 - пользователь): ')
    return first
first = first()
# забахать проверку ввода
#while first != 1 or first != 2:
#    print('Надо ввести или цифру 1, или цифру 2')
#    first = first()
    
matrix = [[' ', '1', '2', '3'],
          ['a', ' ', ' ', ' '],
          ['b', ' ', ' ', ' '],
          ['c', ' ', ' ', ' ']
          ]
x = 0
y = 1
position = [0, 0]
def random_move():
    x = 0
    y = 1
    while matrix[x][y] != ' ':
        x = random.randint(1, 3)
        y = random.randint(1, 3)
    return x, y

def your_move():
    position = input('Введите координаты (вначале буква, потом цифра, слитно: ')
    position1 = str(position)
    x = str(position1[0])
    y = int(position1[1])
    if x == 'a':
        x = 1
    elif x == 'b':
        x = 2
    elif x == 'c':
        x = 3
    else:
        print('Вы ввели неверные координаты, давайте попробуем снова')
        return 0
    if y != 1 and y != 2 and y != 3:
        print('Вы ввели неверные координаты, давайте попробуем снова')
        return 0
    if matrix[x][y] == ' ':
        matrix[x][y] = 'X'
        return 1
    else:
        print('Здесь занято, введите другие координаты')
        return 0

def print_matrix():
    for row in matrix:
        print(row)

victory = 0

def check_two():
    position = random_move()
    x = position[0]
    y = position[1]
    for i in range(1,4):
        if matrix[i][1] == matrix[i][2] != ' ':
            if matrix[i][3] == ' ':
                y = 3
                x = i
        elif matrix[i][1] == matrix[i][3] != ' ':
            if matrix[i][2] == ' ': 
                y = 2
                x = i
        elif matrix[i][2] == matrix[i][3] != ' ':
            if matrix[i][1] == ' ':
                y = 1
                x = i
    for j in range(1,4):
        if matrix[1][j] == matrix[2][j] != ' ':
            if matrix[3][j] == ' ': 
                x = 3
                y = j
        elif matrix[1][j] == matrix[3][j] != ' ':
            if matrix[2][j] == ' ': 
                x = 2
                y = j
        elif matrix[2][j] == matrix[3][j] != ' ':
            if matrix[1][j] == ' ': 
                x = 1
                y = j
    if matrix[1][1] == matrix[2][2] != ' ':
        if matrix[3][3] == ' ':
            x = 3
            y = 3
    if matrix[1][1] == matrix[3][3] != ' ':
        if matrix[2][2] == ' ':
            x = 2
            y = 2
    if matrix[3][3] == matrix[2][2] != ' ':
        if matrix[1][1] == ' ':
            x = 1
            y = 1
    if matrix[1][3] == matrix[2][2] != ' ':
        if matrix[3][1] == ' ':
            x = 3
            y = 1
    if matrix[3][1] == matrix[2][2] != ' ':
        if matrix[1][3] == ' ':
            x = 1
            y = 3
    if matrix[1][3] == matrix[3][1] != ' ':
        if matrix[2][2] == ' ':
            x = 2
            y = 2
    matrix[x][y] = 'O'
    
def check_victory():
    for i in range(1,4):
        if matrix[i][1] == matrix[i][2] == matrix[i][3] != ' ':
            if matrix[i][2] != ' ':
                print('Победа! строка ', i)
                exit()
    for j in range(1,4):
        if matrix[j][1] == matrix[j][2] == matrix[j][3] != ' ':
            if matrix[2][j] != ' ':
                print('Победа! столбец ', j)
                exit()
    if matrix[1][1] == matrix[2][2] == matrix[3][3] != ' ':
        if matrix[2][2] != ' ':
            print('Победа! диагональ ')
            exit()
    if matrix[1][3] == matrix[2][2] == matrix[3][1] != ' ':
        if matrix[2][2] != ' ':
            print('Победа! диагональ')
            exit()
    cont = 0
    for row in matrix:
        for element in row:
            if element == ' ':
                cont = 1
    if cont == 0:
        print('Ходы кончились, победителя нет')
        exit()

print_matrix()

if first == '1':
    position = random_move()
    x = position[0]
    y = position[1]
    matrix[x][y] = 'O'
    print('Ход компьютера:')
    print_matrix()

    
while victory != 1:
    check = your_move()
    while check != 1:
        check = your_move()
    print_matrix()
    victory = check_victory()
    
    check_two()
    print('Ход компьютера:')
    print_matrix()
    victory = check_victory()

exit()
