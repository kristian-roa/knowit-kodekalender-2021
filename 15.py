def main():
    lines = ['aaaaaaaabbbbbbbbcccccccc',
             'wawwgjlmwkafeosjoæiralop',
             'jagwfjsuokosjpzæynzxtxfnbæjkæalektfamxæø',
             'wawwgjlmwkoåeosaæeoltååøbupscpfzqehkgdhkjdoqqkuuakvwogjkpøjsbmpq',
             'vttyøyønøbjåiåzpejsimøldajjecnbplåkyrsliænhbgkvbecvdscxømrvåmagdioftvivwøkvbnyøå']

    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['æ', 'ø', 'å']

    def idx(c): return letters.index(c) + 1

    key = 'godjul'
    key = key[:8]
    key_len = len(key)
    key += 'x' * (8 - len(key))

    for line in lines:
        blocks = [line[i:i+8] for i in range(0, len(line), 8)]
        encrypted = ''
        for n, block in enumerate(blocks, start=1):
            word = ''.join(letters[(idx(block[i]) + idx(key[i]) + i + n*key_len) % len(letters)] for i in range(len(block)))
            encrypted += word

            print('KEY:', ''.join(letters[(idx(word[i]) - range(key_len*n + 2, key_len*n + 10)[i] - idx(block[i]) + 1) % len(letters) - 1] for i in range(len(word))))
        print(encrypted)


if __name__ == '__main__':
    main()
