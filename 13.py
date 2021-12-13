import requests
import numpy as np


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBcmtDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--084d36cb3409a1e265d498b4345d745b1356842c/moves.txt?disposition=inline'
    moves = requests.get(url).content.decode('utf-8').splitlines()

    chimney = np.zeros((9, 9))
    dirs = {'N': np.array([1, 0]), 'S': np.array([-1, 0]), 'E': np.array([0, 1]),
            'W': np.array([0, -1]), 'I': np.array([0, 0])}

    for gift in moves:
        pos, height = np.array([chimney.shape[0] // 2, chimney.shape[1] // 2]), 250
        for M in gift:
            new_pos = pos + dirs[M]
            if all(0 <= new_pos[j] < chimney.shape[j] for j in (0, 1)) and chimney[tuple(new_pos)] < height:
                pos = new_pos

            if height == 0 or chimney[tuple(pos)] == height - 1: break
            height -= 1

        chimney[tuple(pos)] += 1

    print(np.max(chimney) * 10)


if __name__ == '__main__':
    main()
