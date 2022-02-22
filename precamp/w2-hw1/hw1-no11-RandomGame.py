from random import randint

for iter in range(1, 6):
    guessed = int(input('guess the number: '))
    Random_Selected = randint(1, 20)
    if Random_Selected == guessed:
        print('You Win')
else:
    print('Game Over')
    print(Random_Selected)
