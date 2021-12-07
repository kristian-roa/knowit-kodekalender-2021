def main():
    x = ant = 1
    while ant < 20*x:
        ant = ant * (x+1) / x + 1
        x += 1

    print(0.2 * x)


if __name__ == '__main__':
    main()
