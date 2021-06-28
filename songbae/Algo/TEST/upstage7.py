from collections import defaultdict
def find_unique_numbers(numbers):
    temp=set(numbers)
    arr=defaultdict(int)
    temp1=set()
    for i in numbers:
      arr[i]+=1
      if arr[i]>1:
        temp1.add(i)
    
    return temp-temp1


if __name__ == "__main__":
    print(find_unique_numbers([1, 2, 1, 3]))
