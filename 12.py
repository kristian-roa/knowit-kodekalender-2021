import requests
import re
from collections import deque


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBcklDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--6b8096adf032d85569a684cbda764a8cb8eba185/task.txt?disposition=inline'
    categories = [re.match(r'(-*)(K|G) .*', x).groups() for x in requests.get(url).content.decode('utf-8').splitlines()]

    count = 0
    stack = deque()

    for depth, kind in categories + [('', 'K')]:
        while stack and len(depth) <= stack[-1][0]:
            if stack.pop()[1]: count += 1

        if kind == 'K':
            stack.append([len(depth), False])
        else:
            for s in reversed(stack):
                if s[1]: break
                s[1] = True

    print(count)


if __name__ == '__main__':
    main()
