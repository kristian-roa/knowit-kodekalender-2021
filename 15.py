def main():
    lines = ['wawwgjlmwkafeosjoæiralop',
             'jagwfjsuokosjpzæynzxtxfnbæjkæalektfamxæø',
             'wawwgjlmwkoåeosaæeoltååøbupscpfzqehkgdhkjdoqqkuuakvwogjkpøjsbmpq',
             'vttyøyønøbjåiåzpejsimøldajjecnbplåkyrsliænhbgkvbecvdscxømrvåmagdioftvivwøkvbnyøå']

    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['æ', 'ø', 'å']
    print(len(letters))

    def idx(c): return letters.index(c) + 1

    key = ''  # 'alvalv'
    key_len = 6  # len(key)
    key += 'x' * (8 - len(key))

    # decrypt
    for line in lines:
        blocks = [line[i:i+8] for i in range(0, len(line), 8)]
        decrypted = ''
        for n, block in enumerate(blocks, start=1):
            word = ''.join(letters[(idx(block[i]) - key_len*n - 1 - (i + 1) - idx(key[i])) % len(letters)] for i in range(len(block)))
            decrypted += word

        print(decrypted)


if __name__ == '__main__':
    main()
