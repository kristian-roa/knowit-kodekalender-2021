import requests


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBNdz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--0af4f790dec929a13e3615fdac11667323ea1597/tall.txt?disposition=inline'
    s = requests.get(url).content.decode('utf-8')

    words = {'en': 1, 'to': 2, 'tre': 3, 'fire': 4, 'fem': 5, 'seks': 6, 'sju': 7, 'åtte': 8, 'ni': 9, 'ti': 10,
             'elleve': 11, 'tolv': 12, 'tretten': 13, 'fjorten': 14, 'femten': 15, 'seksten': 16, 'sytten': 17,
             'atten': 18, 'nitten': 19, 'tjue': 20, 'tretti': 30, 'førti': 40, 'femti': 50}

    for word, value in sorted(words.items(), reverse=True, key=lambda x: len(x[0])):
        s = s.replace(word, f'{value} ')

    print(sum(int(x) for x in s.split()))


main()
