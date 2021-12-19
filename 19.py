import requests
import numpy as np


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBc3dDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--bb0aa747ae7259b673eb90e9e7c024958ebfbfd6/factory.txt?disposition=inline'
    raw = requests.get(url).content.decode('utf-8').splitlines()

    packing = np.zeros(24 * 60)

    for line in raw:
        clock, *gifts = line.split(', ')
        time = 60 * next(c := map(int, clock.split(':'))) + next(c)

        for _, prod, pack in zip(*[iter(gifts)] * 3):
            time += int(prod)
            packing[time:time+int(pack)] += 1

    print(np.max(packing))


if __name__ == '__main__':
    main()
