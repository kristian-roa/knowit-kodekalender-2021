import requests
import csv
import re
from math import radians, sin, cos, acos


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBOUT09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--7bb23c39ab7eb5b367e3b0841b86e0667756397f/cities.csv?disposition=inline'
    data = requests.get(url).content.decode('utf-8')
    data = csv.reader(data.splitlines(), delimiter=',')
    cities = {city[0]: point_to_coord(city[1]) for city in data}
    del cities['city']

    # BEGIN
    POLE = (0, 90)
    location = POLE
    distance = 0

    while cities:
        closest = min(cities.items(), key=lambda x: dist(location, x[1]))
        del cities[closest[0]]
        distance += dist(location, closest[1])
        location = closest[1]

    distance += dist(location, POLE)
    print(round(distance))


def point_to_coord(point):
    return tuple(float(x) for x in re.findall(r'[-+]?\d*\.\d+|\d+', point))


def dist(a, b):
    lon1, lat1, lon2, lat2 = map(radians, [a[0], a[1], b[0], b[1]])
    return 6371 * (acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)))


if __name__ == '__main__':
    main()
