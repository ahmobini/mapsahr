
li = list(map(int, input('enter a list: ').split()))
m = int(input('enter number of groups: '))
n = len(li)

def calculator(li,m,n):
    m_list = [sum(li[i*m:(i+1)*m]) for i in range(n//m+1)]
    temp = 0
    for i in range(len(m_list)):
        temp += ((-1) ** (i)) * m_list[i]

    return temp
print(calculator(li,m,n))