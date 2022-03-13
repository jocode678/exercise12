# Which data type?
# 6 random numbers
# Don't need to be in sequence
# Not a dictionary
# Should not be duplicates
# Cannot append a tuple, so using a list

import random

# random.seed(a=None, version=2)
# What is this?

randomNumbers = []

# a = 1
# while a <= 6:
#     x = random.randint(1, 50)
#     randomNumbers.append(x)
#     a = a + 1
# else:
#     pass

# for int in range(6):
#     x = random.randint(1, 50)
#     randomNumbers.append(x)
# print(randomNumbers)

# for int in range(6):
#     myList = list(range(1, 51))
# print(random.sample(myList, 6))

myList = list(range(1, 51))
print(random.sample(myList, 6))

set = []
set.appen

# Should it be 50 or 51? Above using randint, putting 51, I got a result of 51 (thought it would be non-inclusive)
# Ask about refactoring
# Ask about jobs