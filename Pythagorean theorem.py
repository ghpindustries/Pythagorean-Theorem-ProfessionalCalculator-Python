def find_base(perpendicular,hypotenuse):
    base = ((hypotenuse**2)-(perpendicular**2))**(1/2)
    return base

def find_perpendicular(base,hypotenuse):
    perpendicular = ((hypotenuse**2)-(base**2))**(1/2)
    return perpendicular

def find_hypotenuse(base,perpendicular):
    hypotenuse= ((perpendicular**2)+(base**2))**(1/2)
    return hypotenuse

print("Enter any two values, Enter Unknown Value as '0'!!")
b = int(input('Base: '))
p = int(input('Perpendicular: '))
h = int(input('Hypotenuse: '))


if (h != 0) and (h<b or h<p):
    print('Hypotenuse cannot be lesser the the other two sides')
elif (h == 0 and b == 0)or(b == 0 and p == 0)or(p == 0 and h == 0):
    print('Error Finding the value \n You Must Enter 2 Values \n Please Check And Try Again!')
elif (h == 0 or (h>b and h>p)) and (h == 0 or b == 0  or p == 0):
    if b == 0:
        print(find_base(p,h))
    elif p == 0:
        print(find_perpendicular(b,h))
    elif h == 0:
        print(find_hypotenuse(b,p))
else:
    print("Error!")
