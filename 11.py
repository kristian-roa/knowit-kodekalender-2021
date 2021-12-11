import requests
from collections import Counter
from math import inf


def main():
    url_names = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBcDhDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--4e38dd2802132b5f356a3018edad90e70c24e93e/names.txt?disposition=inline'
    url_gifts = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBcUFDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--8e26125e06ecb2664bba74b49be7bd0727ca8373/locked.txt?disposition=inline'

    names = {name: variants(name) for name in requests.get(url_names).content.decode('utf-8').splitlines()}
    gift_list = requests.get(url_gifts).content.decode('utf-8').splitlines()

    gifts = Counter()

    for crypto in gift_list:
        c = Counter(crypto)
        elf = None, inf
        collision = False

        for name, variations in names.items():
            n = Counter(name)
            if any(c[l] < count for l, count in n.items()): continue

            for variant in [name] + variations:
                start = crypto.index(variant[0])
                i, j, end = 0, start, None

                while i < len(variant) and j < len(crypto):
                    if variant[i] == crypto[j]:
                        i += 1
                        if i == len(variant): end = j + 1
                    j += 1

                if end:
                    remaining = sum((Counter(crypto[start:end]) - n).values())
                    if remaining < elf[1]:
                        elf = name, remaining
                        collision = False
                        break
                    elif remaining == elf[1]:
                        collision = True

        if not collision and elf[0]:
            gifts[elf[0]] += 1

    print(*gifts.most_common(1)[0])


def variants(name):
    return [name[:i] + name[i+1] + name[i] + name[i+2:] for i in range(len(name) - 1)]


if __name__ == '__main__':
    main()
