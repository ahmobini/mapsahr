def Diff_Game(number):
    number = str(number)
    if number[0] > number[1]:
        difference = int(number[0]) - int(number[1])
        return difference
    elif number[0] < number[1]:
        difference = int(number[1]) - int(number[0])
        return difference
    else:
        return 0


print(Diff_Game(18))