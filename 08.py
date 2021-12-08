import requests
import re
import numpy as np

def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBcEVDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--c58f01ade88c36b61eda8ecd198328de54f47160/input.txt?disposition=inline'
    coords, route = (s := requests.get(url).text.splitlines())[:200], s[200:]
    coords = [(int((x := re.findall(r'\d+', y))[0]), int(x[1])) for y in coords]
    route = map(int, route)

    city = np.zeros((1000, 1000))
    x1, y1 = coords[next(route)]

    for move in route:
        x2, y2 = coords[move]

        y = slice(y1, y2) if y2 > y1 else slice(y2+1, y1+1)
        x = slice(x1, x2) if x2 > x1 else slice(x2+1, x1+1)
        city[y, x] += 1

        x1, y1 = x2, y2

    ys, xs = np.where(city == np.max(city))
    print(f'{min(xs)},{min(ys)} {max(xs)},{max(ys)}')


if __name__ == '__main__':
    main()
