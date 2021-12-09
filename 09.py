from z3 import Ints, Solver


def main():
    vals = Ints('x y z')
    remaining = [1854803357, 2787141611, 1159251923]
    children = [2424154637, 2807727397, 2537380333]

    eq = [vals[i] * children[i] + remaining[i] for i in range(3)]

    ans = Solver()
    ans.add(eq[0] == eq[1] == eq[2])
    ans.check()

    print(ans.model().eval(eq[0]))


if __name__ == '__main__':
    main()
