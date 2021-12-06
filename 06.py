import requests
import numpy as np


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBallDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--20b29549a475416a15aa81ff11b00da4c4103e67/pakker.txt?disposition=inline'
    gifts = [(int((x := s.split(','))[0]), int(x[1])) for s in requests.get(url).text.splitlines()]

    stack = np.full((1, 21), True)
    fall = 0

    for x, length in gifts:
        # insert new row on top
        if stack[0, :].any(): stack = np.concatenate((np.full((1, 21), False), stack))

        # find row to insert gift
        for i, row in enumerate(stack[:-1, :]):
            if row[x:x+length].any(): break
            idx = i

        # support under middle ?
        mid = length // 2
        mid_support = stack[idx+1, x+mid] if length % 2 else False

        # support on left and right side?
        left = stack[idx+1, x:x+mid].any()
        right = stack[idx+1, x+length-mid:x+length].any()

        if (left and right) or mid_support:
            stack[idx, x:x+length] = True
        else:
            fall += 1

    print(fall)


if __name__ == '__main__':
    main()
