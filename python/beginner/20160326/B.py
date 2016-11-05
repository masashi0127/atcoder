# coding: utf-8;

def main():
    s = input()
    t = int(input())

    l = s.count('L')
    r = s.count('R')
    u = s.count('U')
    d = s.count('D')
    q = s.count('?')

    if t == 1:
        print(abs(l - r) + abs(u - d) + q)
    else:
        res = abs(l - r) + abs(u - d) - q
        print(max(abs(res) % 2, res))

if __name__ == '__main__':
    main()
