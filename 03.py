import requests
import numpy as np


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBOdz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--31fa0c541c69eeb9063ccfc56e686f4768662004/input.txt?disposition=inline'
    neighbours = requests.get(url).text

    vals = [{'J': 1, 'N': -1}[c] for c in neighbours]
    last_idx, size, idx = {}, 0, 0
    for i, cs in enumerate(np.cumsum(vals)):
        if cs in last_idx:
            if (j := i - last_idx[cs]) > size:
                size, idx = j, last_idx[cs] + 1
        else:
            last_idx[cs] = i

    print(size, idx)


if __name__ == '__main__':
    main()
