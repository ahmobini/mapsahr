count1 = 0
count2 = 0
occurences = int(input())

for iter in range(occurences):
    s = input()

def Minotrity(occurences):
    for iter in range(occurences):
        for c in range(len(s)):
            if s[c] == '0':
                count1 += 1
            elif s[c] == '1':
                count2 += 1
        if count1 > count2:
            return count2
        elif count1 < count2:
            return count1
        else:
            pass

print(Minotrity(3))

