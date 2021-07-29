a = 0
b = 0
c = 0

def func(a,b):
    if b == 1:
        return a % c

    if b % 2 == 1:
        return ((func(a,b//2)**2)*a)%c
    else:
        return (func(a,b//2)**2)%c

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    
    print(func(a,b))