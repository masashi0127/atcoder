# coding: utf-8;

def main():
    n, q = map(int, input().split())
    p = [0 for _ in range(n + 1)]

    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        p[l] += 1
        p[r] -= 1

    res = ''

    for i in range(n):
        p[i + 1] += p[i]
        res += str(p[i] % 2)

    print(res)

if __name__ == '__main__':
    main()
