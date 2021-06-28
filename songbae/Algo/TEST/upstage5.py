from collections import Counter
from collections import defaultdict

def nth_lowest_selling(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """
    T = Counter(sales)
    temp=defaultdict(int)
    for i in sales:
      temp[i]+=1
    for idx,(k,v) in enumerate(temp.items()):
      if idx==len(temp)-n:
        return k



if __name__ == "__main__":
    print(nth_lowest_selling([6,6,6,6,6,6,6,6,6,5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))


def nth_lowest_selling(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """
    T = Counter(sales)
    for idx, (key, value) in enumerate(T.items()):
        if idx == len(T)-n:
           return key


if __name__ == "__main__":
    print(nth_lowest_selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))
