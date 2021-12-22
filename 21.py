import re


def main():
    code = '45205145192051057281419115181357209121021125181201516161911252091475141221011351923522729182181222718192919149121210211251491919514'
    alfabet = [' '] + [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['æ', 'ø', 'å']

    for n in (10, 20): code = code.replace(f'{n}', alfabet[int(n)])

    swaps = None
    while swaps != 0:
        code, swaps = re.subn(r'(^|[a-z]|[1-2][1-9])([3-9])',
                              lambda m: rf'{m.group(1) + alfabet[int(m.group(2))]}', code)

    print(code)

    # Endte opp med å dekode manuelt


if __name__ == '__main__':
    main()
