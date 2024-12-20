# Random.py

import random
random.seed(34)

# print 5 random numbers between 100 and 200
for i in range(0, 5):
    n = random.randint(100, 200)
    print(n)
