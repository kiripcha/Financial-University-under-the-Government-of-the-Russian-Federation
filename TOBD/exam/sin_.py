import math
from collections import Counter
res = []
mask = []
def find_sin(a):
    mask.append(Counter(list(str(math.sin(a)))).most_common()[0][1]>=9)
    res.append({a:math.sin(a)})
    return mask, res
    #if Counter(list(str(math.sin(a)))).most_common()[0][1]>=9:
    #    return({a:math.sin(a)})
    #else:
    #    return None
