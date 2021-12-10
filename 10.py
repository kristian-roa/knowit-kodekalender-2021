import numpy as np


def main():
    grid = np.array([
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
    ])

    buttons = set(grid.flatten())
    DIRS = [np.array([y, x]) for x in (-1, 0, 1) for y in (-1, 0, 1) if not x == y == 0]

    def valid_moves(history, grid):
        idx = np.argwhere(grid == history[-1])[0]

        invalid = {grid[i] for d in DIRS
                   if (0 <= (i := tuple(idx + d*2))[0] <= 2 and 0 <= i[1] <= 2)
                   and grid[tuple(idx + d)] not in history}

        return buttons - invalid - set(history)

    def count_perms(code, length):
        if len(code) == length: return 1
        return sum(count_perms(code + [b], length) for b in valid_moves(code, grid))

    print(count_perms(['D'], length=8))


if __name__ == '__main__':
    main()
