from collections import Counter

rooms = list(map(int, input().split(' ')))
set_ = set(rooms)
count = Counter(rooms)

for i in set_:  
    rooms.remove(i)  
    if i not in rooms:
        print(i)
        break
        