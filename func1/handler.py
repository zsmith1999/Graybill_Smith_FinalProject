import numpy as np
def handle(req):
    arr = []
    for i in range(5000):
      arr.append(np.random.randint(5000))
    return arr