import requests
from collections import defaultdict


def main():
    url_wrong = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdVFDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--0231bdab4db307bd7c2cc773887ac45934075ea5/feilregistreringer.txt?disposition=inline'
    url_work = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBdVVDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--7c54e83e4bf7d625841928ae1b26b9adb4cfd0fa/skritt.txt?disposition=inline'

    wrongs = {(x := position.split(' /'))[0]: [int(wrong) for wrong in x[1:]]
              for position in requests.get(url_wrong).content.decode('utf-8').splitlines()}

    workers = [[int(z) if z.strip().isdigit() else 0 if z.strip() == '' else z.strip() for z in elf.split('/')]
               for elf in requests.get(url_work).content.decode('utf-8').splitlines()]

    total_steps, days = defaultdict(lambda: [0]*7), 1
    for w in workers:
        if len(w) == 1: days += 1; continue  # new week
        elf, title, *steps = w

        for i in range(7): total_steps[elf][i] += val if (val := steps[i] - wrongs[title][i]) >= 0 else 0

    santa, elves = [0] * 7, [0] * 7
    for elf, steps in total_steps.items():
        for i in range(7):
            if elf == 'Nissen 🎅': santa[i] = steps[i] / days
            else: elves[i] += (steps[i] / days) / (len(total_steps) - 1)

    print(''.join(str(int(santa[i] - elves[i])) for i in range(7)))


if __name__ == '__main__':
    main()
