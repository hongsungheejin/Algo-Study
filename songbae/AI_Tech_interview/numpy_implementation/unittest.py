from utils.functions import *
import numpy as np
x = [0, 0, 1, 2, 3, 4, 5, 1, 2, 3]
y = [1, 1, 1, 2, 3, 4, 5, 1, 1, 1]
x = np.array(x)
y = np.array(y)
print(cross_entropy_error(x, y))
