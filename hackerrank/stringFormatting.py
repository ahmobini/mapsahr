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