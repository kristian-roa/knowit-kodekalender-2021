import requests
import re


def main():
    url = 'https://julekalender-backend.knowit.no/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBak1DIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--d6d3984e0f603df1771ef6b699e6e86d6ee577a7/tree.txt?disposition=inline'
    tree_str = requests.get(url).content.decode('utf-8')
    elves = re.sub(r'\)', r' )', re.sub(r'\(', r' ( ', tree_str)).split()

    prev = elves[0]
    parents = []
    height = depth = 0

    for elf in elves[1:]:
        if elf == '(':
            parents.append(prev)
            if prev != 'Grinch': depth += 1
        elif elf == ')':
            if parents.pop() != 'Grinch': depth -= 1
        else:
            prev = elf
        height = max(depth, height)

    print(height)


if __name__ == '__main__':
    main()
