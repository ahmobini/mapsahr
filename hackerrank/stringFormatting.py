from unittest import result


def dec_to_bin(n):
    if n == 0:
        return [0]
    else:
        lst = []
        while n:
            lst.append(n%2)
            n=n//2
        return lst[::-1]

def dec_to_oct(n):
    if n == 0:
        return [0]
    else:
        res= []
        result = []

        lst = [int(i) for i in str(n)]
        for ele in lst:
            res.append(dec_to_bin(ele))
            result = ",".join(map(str, res))

        return result

#  zfill(3) must be added

def dec_to_hex(n):
    if n == 0:
        return [0]
    else:
        res= []
        result = []

        lst = [int(i) for i in str(n)]
        for ele in lst:
            res.append(dec_to_bin(ele))
            result = ",".join(map(str, res))

        return result

# zfill(4) must be added



if __name__ == '__main__':
    n = int(input())
    print(dec_to_bin(n))
    print(dec_to_oct(n))
    print(dec_to_hex(n))