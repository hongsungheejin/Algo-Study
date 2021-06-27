def check(aim, tri_list):
    for i in range(len(tri_list)):
        for j in range(len(tri_list)):
            for k in range(len(tri_list)):
                temp = tri_list[i] + tri_list[j] + tri_list[k]
                if temp == aim:
                    return True
                    
if __name__ == '__main__':
    T = int(input())

    tri_list = [int(i * (i + 1) /2) for i in range(1,51)]

    for _ in range(T):
        aim = int(input())
        
        if check(aim, tri_list):
            print("1")
        else:
            print("0")


