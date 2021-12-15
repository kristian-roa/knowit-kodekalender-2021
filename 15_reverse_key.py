def main():
    lines = ['wawwgjlmwkafeosjoæiralop',
             'jagwfjsuokosjpzæynzxtxfnbæjkæalektfamxæø',
             'wawwgjlmwkoåeosaæeoltååøbupscpfzqehkgdhkjdoqqkuuakvwogjkpøjsbmpq',
             'vttyøyønøbjåiåzpejsimøldajjecnbplåkyrsliænhbgkvbecvdscxømrvåmagdioftvivwøkvbnyøå']

    lines = lines[:1]

    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['æ', 'ø', 'å']
    def idx(c): return letters.index(c) + 1

    for line in lines:
        blocks = [line[i:i+8] for i in range(0, len(line), 8)]
        print('LINE:', line)
        for key_len in range(1, 9):
            for n, block in enumerate(blocks, start=1):
                print('KEY:', ''.join(letters[(idx(block[i]) - range(key_len*n + 2, key_len*n + 10)[i]) % len(letters) - 1] for i in range(len(block))))
            print()



if __name__ == '__main__':
    main()
