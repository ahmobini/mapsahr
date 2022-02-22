
ls = ['square', 'circle', 'rectangle', 'triangle']

def get_func(ls):
    ch = input('enter a shape:')
    if ch == 'square':
        a = int(input('enter a: '))
        return square(a)
    elif ch == 'circle':
        r = int(input('enter r: '))
        return circle(r)
    elif ch == 'rectangle':
        a,b = map(int, input('enter a and b: ').split())
        return rectangle(a,b)
    elif ch == 'triangle':
        ghaede,height = map(int, input('enter ghaede and height: ').split())
        return triangle(ghaede, height)



def square(a):
    return a*a

def circle(r):
    pi = 3.14
    return pi*r**2

def rectangle(a,b):
        return 2*(a+b)

def triangle(ghaede, height):
    return ghaede*height/2


ls = get_func(ls)
print(ls)