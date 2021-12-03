import requests


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBOdz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--31fa0c541c69eeb9063ccfc56e686f4768662004/input.txt?disposition=inline'
    neighbours = requests.get(url).text

    assert search('JJJJJNNJJNNJJJJJ') == (8, 3)
    print(search(neighbours))


def search(neighbours):
    l = len(neighbours)
    biggest = min(j := neighbours.count('J'), l - j) * 2
    for size in range(biggest if biggest % 2 == 0 else biggest - 1, 1, -2):
        for i in range(l - size + 1):
            if neighbours[i:size + i].count('J') == size / 2:
                return size, i


if __name__ == '__main__':
    main()
