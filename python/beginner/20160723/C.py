# coding: utf-8;

def main():
    num = [0,1,2,3,4,5,6,7,8,9]
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    usable_num = list(set(num) - set(d))

    while True:
        f = True
        for a in str(n):
            if int(a) not in usable_num:
                f = False
                break
        if f: break
        n += 1
    print(n)

if __name__ == '__main__':
    main()
