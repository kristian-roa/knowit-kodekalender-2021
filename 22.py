import requests
from collections import deque


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdHNDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--714ad1051b4004fa4b99b3d06fda2801cc8abb2c/boards.txt?disposition=inline'
    boards = requests.get(url).content.decode('utf-8').splitlines()
    # boards = ['🎅🎅⛄🎄✨⛄⛄🎅🎄✨✨⛄🎅🎄🎄✨']

    moves = (column_up, column_down, row_left, row_right)

    total_steps = 0
    for board_num, board in enumerate(boards):
        print(f'BOARD: {board_num + 1}')

        for idx, emoji in enumerate(('🎅', '⛄', '🎄', '✨')): board = board.replace(emoji, str(idx))

        stack = deque([(board, 0)])
        visited = set()

        while stack:
            state, steps = stack.popleft()
            if solved(state): break
            visited.add(state)

            for move in moves:
                for i in range(4):
                    b = move(state, i)
                    if b not in visited:
                        stack.append((b, steps+1))

        total_steps += steps

    print(steps)


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

def solved(board):
    return all((b := board[i*4:i*4+4]) == 4 * b[0] for i in range(4))

def print_board(board):
    for i in range(4):
        print(board[i*4:i*4+4])


if __name__ == '__main__':
    main()
