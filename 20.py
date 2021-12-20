import requests
import numpy as np
import re


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBczRDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--8c02ba82414b0b5862f18fc5899e5c855f788178/maze.txt?disposition=inline'

    maze = np.asarray([[tuple(int(z) for z in re.findall(r'\d', y)) for y in re.findall(r'\(\d,\d,\d,\d\)', x)]
                       for x in requests.get(url).content.decode('utf-8').splitlines()])

    def left(rot): return (rot - 1) % 4
    def right(rot): return (rot + 1) % 4
    def double(rot): return (rot + 2) % 4

    move = [np.array([-1, 0]), np.array([0, 1]), np.array([1, 0]), np.array([0, -1])]

    pos = np.array([0, 0]); rot = 2; steps = 0
    while tuple(pos + 1) != maze.shape[:-1]:
        if maze[(*pos), left(rot)]: rot = left(rot)
        elif maze[(*pos), rot]: pass
        elif maze[(*pos), right(rot)]: rot = right(rot)
        else: rot = double(rot)

        pos += move[rot]
        steps += 1

    print(steps)


if __name__ == '__main__':
    main()
