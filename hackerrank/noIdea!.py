
x,y = map(int, input().split())
n = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

def happiness_production(n,A,B):
    for i in n:
        if i in A:
            yield 1
        elif i in B:
            yield -1
        else:
            yield 0
happiness = 0
for i in happiness_production(n,A,B):
    happiness += i
    
print(happiness)