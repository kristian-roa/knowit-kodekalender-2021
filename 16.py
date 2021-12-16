import requests
import numpy as np


def main():
    url_last = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBc01DIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--da41666bbf046e85ca348e28eecdbac89b6e4a67/str%C3%B8mpriser.txt?disposition=inline'
    url_next = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBc1FDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--36c5a9fb6cefb1e71af8290bea926503f67f955f/str%C3%B8mpriser_next.txt?disposition=inline'

    last_year = read(requests.get(url_last).content.decode('utf-8'))
    next_year = read(requests.get(url_next).content.decode('utf-8'))

    # STRAT 1
    hour = np.argmin([sum(last_year[i::24]) for i in range(24)])
    price_1 = sum(next_year[hour::24])

    # STRAT 2
    price_2 = 0; skip = False
    for day in range(365):
        if skip: skip = False; continue

        price_2 += next_year[day*24 + hour]

        if last_year[day*24 + hour] < last_year[(day+1)*24 + hour]:
            price_2 += next_year[day*24 + hour + 1]
            skip = True

    print(f'{np.argmin((price_1, price_2))+1},{abs(price_1 - price_2)}')


def read(year, days=365):
    def get(price, hour): return year[(max_price - price) * (24 * days + 1) + hour]

    max_price = year.count('\n') - 1
    for price in range(max_price):
        if get(price, 0) != ' ':
            break

    prices = [price]
    for hour in range(1, days*24):
        for price in range(min(0, price), max(price, max_price) + 1):
            if get(price, hour) != ' ':
                prices.append(price)
                break

    return prices


if __name__ == '__main__':
    main()
