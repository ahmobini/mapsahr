#itertools ro bekhoonid ketabkho
# try:
#     [][3]
# # except NameError as err:
# #     derf=0
# except IndexError as err:
#     print('midonam', err)
# except Exception as err:
#     print(err)


# a = input()

''' recursive program for khoshtarif problem

def khoshtarif(txt):
    # if txt isinstance(txt, str):
    # if not isinstance(txt, str):
        # raise TypeError
    ans = None
    assert isinstance(txt, str), 'alarm'
    if any(i not in '01?' for i in txt):
        raise InputError
    print(txt)
    if condition(txt):
        return num_checker(txt)
    else:
        temp = [khoshtarif(txt.replace('?', i, 1)) for i in '01']
        ans = any(temp)
    print(txt, ans)
    return ans

def condition(txt):
    return True if '?' not in txt else False

def num_checker(txt):
    # if '00' or '11' in txt:
    #     return False
    # else:
    #     return True

    return not any(a in txt for a in ['00','11'])

            
print(khoshtarif('?01'))


'''

#direct solution to khoshtarif problem
from itertools import product

def khosh_tarif(txt):
    inx_lst = [i for i,j in enumerate(txt) if j=='?']
    print(inx_lst)
    for ch_lst in product('01', repeat = len(inx_lst)):
        lst = list(txt)
        for i , ch in zip():
            lst[] = ch
        nex_txt = ''.join(lst)
        if not any

khosh_tarif('?0101010???1')