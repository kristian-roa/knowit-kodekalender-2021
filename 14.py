import requests
import re

def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBcnNDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--6831d5c3e2a2dd4afaf03b75859fc803cafcef20/ordliste.txt?disposition=inline'
    words = requests.get(url).content.decode('utf-8').splitlines()

    count = 0

    troll = r'^.*t.{1,5}r.{1,5}o.{1,5}l.{1,5}l.*$'
    nisse = r'^[^n].*n.{0,2}i.{0,2}s.{0,2}s.{0,2}e.*[^e]$'

    for word in words:
        if re.match(troll, word) or re.match(nisse, word): count += 1

    print(count)


if __name__ == '__main__':
    main()
