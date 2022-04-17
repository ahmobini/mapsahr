from unittest import result


def change_dec_base(n, b=2):
    if n == 0:
        return [0]
    else:
        lst = []
        while n:
            lst.append(str(n%b))
            n=n//b
        return "".join(lst[::-1])


def dec_to_bin(n):
    return change_dec_base(n, 2)

def dec_to_oct(n):
    return change_dec_base(n, 8)


def dec_to_hex(n):
    return change_dec_base(n, 16)



if __name__ == '__main__':
    n = int(input())
    print(dec_to_bin(n))
    print(dec_to_oct(n))
    print(dec_to_hex(n))
    
    # call for 17 must be:
    '''
    0     0     0     0
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   '''
