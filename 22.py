import requests
from collections import deque


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdHNDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--714ad1051b4004fa4b99b3d06fda2801cc8abb2c/boards.txt?disposition=inline'
    boards = requests.get(url).content.decode('utf-8').splitlines()
    solved = '🎅🎅🎅🎅⛄⛄⛄⛄✨✨✨✨🎄🎄🎄🎄'

    moves = (column_up, column_down, row_left, row_right)

    # Generate all possible states 1-6 steps from solution
    steps_from_solution = {}
    Q, steps = deque([(solved, 0)]), 0

    while steps <= 6:
        state, steps = Q.popleft()
        if state in steps_from_solution: continue
        steps_from_solution[state] = steps

        for move in moves:
            for i in range(4):
                b = move(state, i)
                if b not in steps_from_solution:
                    Q.append((b, steps + 1))

    # Solve the boards
    total_steps = 0
    for num, board in enumerate(boards):
        print(f'Board {num}: ', end='')

        Q = deque([(board, 0)])
        visited = set()

        while Q:
            state, steps = Q.popleft()
            if state in steps_from_solution:
                steps += steps_from_solution[state]
                print(steps)
                break

            visited.add(state)

            for move in moves:
                for i in range(4):
                    b = move(state, i)
                    if b not in visited:
                        Q.append((b, steps+1))

        total_steps += steps

    print('Total steps:', total_steps)


def column_up(board, column):
    col = board[column::4]
    return board[:column] + ''.join(col[(i+1) % 4] + board[column+(i*4)+1:column+(i+1)*4] for i in range(4))


def column_down(board, column):
    col = board[column::4]
    return board[:column] + ''.join(col[(i-1) % 4] + board[column+(i*4)+1:column+(i+1)*4] for i in range(4))


def row_left(board, row):
    return board[:(row-1)*4+4] + board[row *4+1:row*4+4] + board[row * 4] + board[(row+1)*4:]


def row_right(board, row):
    return board[:(row-1)*4+4] + board[row*4+3] + board[row*4:row*4+3] + board[(row+1)*4:]


if __name__ == '__main__':
    main()
