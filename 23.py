import requests
import numpy as np
import re
from collections import deque


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdUVDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--36798097015ac3421173fefd2d750dbdfe9f0a85/maze.txt?disposition=inline'

    maze = np.asarray([[tuple(int(z) for z in re.findall(r'\d', y)) for y in re.findall(r'\(\d,\d,\d,\d\)', x)]
                       for x in requests.get(url).content.decode('utf-8').splitlines()])

    maze[0, 0, 0] = 0  # close entry

    moves = [np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1])]

    Q = deque([(np.array([0, 0]), 0)])
    visited = set()

    while Q:
        pos, steps = Q.popleft()
        if tuple(pos) in visited: continue
        if tuple(pos + 1) == maze.shape[:-1]: break

        visited.add(tuple(pos))

        for rot, move in enumerate(moves):
            if maze[(*pos), rot]:
                Q.append((pos + move, steps + 1))

    print(steps)


if __name__ == '__main__':
    main()
