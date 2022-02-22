
def test_case():
    global A, B, C, D
    global Matrix
    A,B,C,D = map(int, input('enter matrix elements: ').split())
    Matrix =  [
    [A,B],
    [C,D]
    ]
    return Matrix


def abs_value(x):
    if x>=0:
        return x
    if x<0:
        return -x

def quadratic_equ():

    a = 1
    b = -(A + D)
    c = A * D - B * C
    dis = b**2 - 4*a*c
    dis_sqrt = abs_value(dis)**0.5

    if dis == 0:
        sol = -b / (2*a)
        return str(sol)

    elif dis > 0:
        sol = [ (-b + dis_sqrt) / (2*a) , (-b - dis_sqrt) / (2*a) ]
        return str(sol)
    else:
        sol = [ -b / (2*a), " + i ", dis_sqrt , -b / (2*a), " - i ", dis_sqrt ]
        return sol

   
for i in range (10):
    test_case()
    print(quadratic_equ())
