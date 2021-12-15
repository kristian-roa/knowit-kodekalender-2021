def main():
    lines = ['wawwgjlmwkafeosjoæiralop',
             'jagwfjsuokosjpzæynzxtxfnbæjkæalektfamxæø',
             'wawwgjlmwkoåeosaæeoltååøbupscpfzqehkgdhkjdoqqkuuakvwogjkpøjsbmpq',
             'vttyøyønøbjåiåzpejsimøldajjecnbplåkyrsliænhbgkvbecvdscxømrvåmagdioftvivwøkvbnyøå']

    lines = lines[:1]

    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['æ', 'ø', 'å']

    def idx(c): return letters.index(c) + 1

    key = ''

    # key_len = len(key)
    key_len = 8
    key += 'x' * (8 - len(key))
    print(f'{key = }')

    for line in lines:
        blocks = [line[i:i+8] for i in range(0, len(line), 8)]
        decrypted = ''
        for n, block in enumerate(blocks, start=1):
            word = ''.join(letters[(idx(block[i]) - key_len*n - 1 - (i + 1) - idx(key[i])) % len(letters)] for i in range(len(block)))
            decrypted += word + ' '

            # print('KEY:', ''.join(letters[(idx(block[i]) - range(key_len * n + 2, key_len * n + 10)[i] - idx(word[i]) + 1) % len(letters) - 1] for i in range(len(word))))

        print(decrypted)


if __name__ == '__main__':
    main()
