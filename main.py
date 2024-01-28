import os
import random
import time


try:
    import msvcrt
    def key_pressed():
        return msvcrt.kbhit()
    def get_key():
        return msvcrt.getch().decode('utf-8')
except ImportError:
    def key_pressed():
        return False
    def get_key():
        return None


def create_grid(rows, cols):
    grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return grid


def print_grid(grid):
    horizontal_border = '+' + '-' * (len(grid[0]) + 1) + '+'
    print(horizontal_border)
    for row in grid:
        print('|', end=' ')
        print(*['█' if cell else ' ' for cell in row], sep='', end='')
        print('|')
    print(horizontal_border)


def get_neighbours(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbour_row = (row + i) % rows
            neighbour_col = (col + j) % cols
            neighbours.append(grid[neighbour_row][neighbour_col])
    return neighbours


def update_grid(grid):
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = grid[row][col]
            neighbours = get_neighbours(grid, row, col)
            live_neighbours = sum(neighbours)
            if cell == 1 and (live_neighbours < 2 or live_neighbours > 3):
                new_grid[row][col] = 0
            elif cell == 0 and live_neighbours == 3:
                new_grid[row][col] = 1
            else:
                new_grid[row][col] = cell
    return new_grid


def main():
    rows = 5
    cols = 10
    grid = create_grid(rows, cols)
    stop_key = 'b'


    while not key_pressed() or get_key() != stop_key:
        print_grid(grid)
        print ("Press 'b' to stop the game.")
        grid = update_grid(grid)
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')


    print("Game stopped by user.")


if __name__ == '__main__':
    main()
