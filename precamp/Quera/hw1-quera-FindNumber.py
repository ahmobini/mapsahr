import random

def random_num_generator(num1,num2,num3):
    rand_list = [num1, num2, num3]
    for x in range(1,5):
        if x not in rand_list:
            return x

num1, num2, num3 = map(int, input('enter number: ').split())
print(random_num_generator(num1,num2,num3))
