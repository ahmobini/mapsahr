from random import choices


def CoinToss(weight, step):
    location = 0
    coin = choices([0,1], weights= [weight, 1-weight], k=step)

    for ele in coin:
        # print(coin)
        if ele == 1:
            # print('Heads')
            location += 1
        else:
            # print ('Tails')
            location -=1

    return location


def bernouli(k,p):
    f = p**k*(1-p)**(1-k)
    return f   

def BernouliEx(): #expected value
    return p

def BinomialEx(step, p=0.8):
    return step*p

print(BinomialEx(0.8))
print(CoinToss(0.2, 10))