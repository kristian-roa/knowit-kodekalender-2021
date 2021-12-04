import numpy as np

def main():
    n = 100_000_000_000_000_000_079
    x = n // 3 * 2
    y = n // 3

    diff = n - (x + y)
    pos = np.array([x, y])
    north = np.array([0, 1])
    east = np.array([1, 0])

    N = True; i = 0
    while i < diff:
        if N:
            idx = 1
            steps = 3
            mod = 5
        else:
            idx = 0
            steps = 5
            mod = 3

        move = next_div_by_n(pos[idx], steps)
        while not move % mod: move += steps
        amount = move - pos[idx]
        pos += (north if N else east) * amount

        N = not N
        i += amount

    for j in range(i-diff):
        pos -= north if N else east

    print(f'{pos[0]},{pos[1]}')

def next_div_by_n(num, n):
    return ((num // n) + 1) * n


if __name__ == '__main__':
    main()
