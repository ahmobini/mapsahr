def print_rangoli(size):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    
    for c1 in range(size-1,-1,-1):
        result1 = []
        s1 = "-".join(alph[c1:size])
        result1.append((s1[::-1]+s1[1::]).center(2*(size*2-1)-1, "-"))
        print("\n".join(result1[:0:-1]+result1))
        
    for c2 in range(1, size):
        result2 = []
        s2 = "-".join(alph[c2:size])
        result2.append((s2[::-1]+s2[1::]).center(2*(size*2-1)-1, "-"))
        print("\n".join(result2[:0:-1]+result2))
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)