import requests
from itertools import chain, zip_longest


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBc2NDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--668171c35d5406b640886290fcd386d895ebea51/alverekke.txt?disposition=inline'
    elves = requests.get(url).content.decode('utf-8').splitlines()

    letters = [chr(i) for i in range(ord('A'), ord('Z')+1)] + ['Æ', 'Ø', 'Å']
    alfabet = {c: i for i, c in enumerate(chain([' '], letters, map(lambda x: x.lower(), letters)))}

    def in_line(prev, elf):
        for p, e in zip_longest(prev, elf, fillvalue=' '):
            if p == e: continue
            return alfabet[p] < alfabet[e]
        return True

    prev = ''
    print(sum(len((prev := elf)) for elf in elves if in_line(prev, elf)))


if __name__ == '__main__':
    main()
