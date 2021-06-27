from itertools import combinations

if __name__ == '__main__':

    while True:
        check = input()

        if check == '0':
            break
            
        check = list(map(int,check.split()[1:]))

        for c in combinations(check,6):
            print(*c)
        print()