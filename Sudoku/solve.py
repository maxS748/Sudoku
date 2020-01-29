def solve(box):
    find = find_empty(box)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(box, i, (row, col)):
            box[row][col] = i

            if solve(box):
                return True

            box[row][col]
    return False

def valid(box, num, pos):
    #check row
    for i in range(len(box[0])):
        if box[pos[0]][i] == num and pos[1] != i:
            return False

    #check colomn
    for i in range(len(box)):
        if box[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 +3):
            if box[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(box):
    for i in range(len(box)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(box[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(box[i][j])
            else:
                print(str(box[i][j]) + " ", end="")

def find_empty(box):
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] == 0:
                return (i, j) #row, col

    return None 