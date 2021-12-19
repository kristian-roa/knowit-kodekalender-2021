import requests
from collections import defaultdict


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBc3dDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--bb0aa747ae7259b673eb90e9e7c024958ebfbfd6/factory.txt?disposition=inline'
    raw = requests.get(url).content.decode('utf-8').splitlines()

    machines = []
    for line in raw:
        clock, *gifts = line.split(', ')
        clock = (int(x) for x in clock.split(':'))
        clock = 60*next(clock) + next(clock)
        machines.append([clock] + [(int(prod), int(pack)) for item, prod, pack in zip(*[iter(gifts)]*3)])

    packable = defaultdict(list)
    for clock, *gifts in machines:
        for prod, pack in gifts:
            clock += prod
            packable[clock].append(clock + pack)

    early, end = min(packable), max(packable)
    benches = []

    for time in range(early, end+1):
        finishes = packable[time]
        for i in range(len(benches)):
            if benches[i][0] == time: benches[i] = (0, True)

        for finish in finishes:
            for i in range(len(benches)):
                if benches[i][1]:
                    benches[i] = (finish, False)
                    break
            else:
                benches.append((finish, False))

    print(len(benches))


if __name__ == '__main__':
    main()
