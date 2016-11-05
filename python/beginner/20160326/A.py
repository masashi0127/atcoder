# coding: utf-8;

def main():
    w, h = map(int, input().split())
    a = w
    b = h
    while a % b != 0:
        t = a % b
        a = b
        b = t
    print('{}:{}'.format(w // b, h // b))

if __name__ == '__main__':
    main()
