import copy
import os
import random
import time

def run_game(state):
    render(state)
    # time.sleep(1)

    while(is_alive(state)):
        state = next_board_state(state)
        render(state)
        time.sleep(1)

    print('The Game of Life is over')

def random_state(width, height):
    state = dead_state(height, width)
    for x in range(len(state)):
        for y in range(len(state[x])):
            random_number = random.random()
            if random_number > 0.15:
                state[x][y] = 0
            else:
                state[x][y] = 1

    return state

def is_alive(board):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] == 1:
                return True

    return False

def dead_state(width, height):
    board = [[0 for _ in range(height)] for _ in range(width)]
    return board

def next_board_state(board):
    # * copy.deepcopy(arr) to make array copies without reference
    temp_board = copy.deepcopy(board)
    for x in range(len(board[0])):
        for y in range(len(board)):
            count = neighbor_count(x, y, board)
            if board[y][x] == 1:
                if count == 0:
                    temp_board[y][x] = 0
                elif count in [2, 3]:
                    pass
                else:
                    temp_board[y][x] = 0
            elif board[y][x] == 0 and count == 3:
                temp_board[y][x] = 1

    return temp_board

def neighbor_count(x, y, board):
    if x == 0:
        if y == 0:
            count = board[y][x + 1] + board[y + 1][x + 1] + board[y + 1][x]
        elif y == len(board) - 1:
            count = board[y][x + 1] + board[y - 1][x + 1] + board[y - 1][x]
        else:
            count = board[y - 1][x + 1] + board[y - 1][x] + board[y][x + 1] + board[y + 1][x + 1] + board[y + 1][x]
    elif x == len(board[y]) - 1:
        if y == 0:
            count = board[y][x - 1] + board[y + 1][x - 1] + board[y + 1][x]
        elif y == len(board) - 1:
            count = board[y][x - 1] + board[y - 1][x - 1] + board[y - 1][x]
        else:
            count = board[y][x - 1] + board[y + 1][x - 1] + board[y + 1][x] + board[y - 1][x - 1] + board[y - 1][x]
    else:
        if y == 0:
            count = board[y][x - 1] + board[y + 1][x - 1] + board[y + 1][x] + board[y + 1][x + 1] + board[y][x + 1]
        elif y == len(board) - 1:
            count = board[y][x - 1] + board[y - 1][x - 1] + board[y - 1][x] + board[y - 1][x + 1] + board[y][x + 1]
        else:
            count = board[y - 1][x - 1] + board[y - 1][x] + board[y - 1][x + 1] + board[y][x - 1] + board[y][x + 1] + board[y + 1][x - 1] + board[y + 1][x] + board[y + 1][x + 1]

    return count

def render(board):
    os.system('clear')
    print('\tThe Game of Life')
    for x in range(len(board)):
        print('|', end = '')
        for y in range(len(board[x])):
            print(' ' if board[x][y] == 0 else '#', end = '')
        print('|')

def load_state(state_file):
    f = open(f'./{state_file}', 'r')
    state = f.read().split('\n')
    new_board = []
    for x in state:
        temp = list(x)
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        new_board.append(temp)

    return new_board

def main():
    op = input('Do you want to load a file?\n' +
              'y = YES | n = N\n')

    state = []

    if op.lower() == 'n':
        width = input("Board's width: ")
        height = input("Board's height: ")
        state = random_state(width, height)
    elif op.lower() == 'y':
        file_name = input('Introduce the file name: ')
        state = load_state(file_name)

    run_game(state)

if __name__ == "__main__":
    main()