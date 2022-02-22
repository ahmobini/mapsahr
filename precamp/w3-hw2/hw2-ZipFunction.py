
import random

def random_num_generator():
    while True:
        rand = random.randint(-10, 10)
        yield rand

n = int(input('enter number of values: '))
g = random_num_generator()
for i in range(n):
    print(next(g))

