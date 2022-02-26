# Which data type?
# 6 random numbers
# Don't need to be in sequence
# Not a dictionary
# Should not be duplicates
# Cannot append a tuple, so using a list

import random

random.seed(a=None, version=2)

randomNumbers = []

a = 1
while a <= 6:
    x = random.randint(1, 51)
    randomNumbers.append(x)
    a = a + 1
else:
    pass

print(randomNumbers)

