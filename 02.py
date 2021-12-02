import requests
from math import radians, sin, cos, acos
import parse


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBOUT09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--7bb23c39ab7eb5b367e3b0841b86e0667756397f/cities.csv?disposition=inline'
    data = requests.get(url).content.decode('utf-8')

    pattern = parse.compile('{city},Point({x:f} {y:f})')
    cities = set((match['x'], match['y']) for line in data.splitlines() if (match := pattern.parse(line)))

    location = POLE = (0, 90)
    distance = 0

    while cities:
        closest = min(cities, key=lambda x: dist(location, x))
        cities.remove(closest)
        distance += dist(location, closest)
        location = closest

    distance += dist(location, POLE)
    print(round(distance))


def dist(a, b):
    lon1, lat1, lon2, lat2 = map(radians, [*a, *b])
    return 6371 * (acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)))


if __name__ == '__main__':
    main()
