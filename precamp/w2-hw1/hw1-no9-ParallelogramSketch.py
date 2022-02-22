length, height = map(int, input('enter length and height of Parallelogram: ').split())
print(" " * length + "*" * length)
for j in range(1, height-1):
    print(" "*(height-j) + "*" + " "*(height) + "*")
print("*" * length )
