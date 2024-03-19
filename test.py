def func(x,y):
    return x*x+y*y

def der(x,y):
    return 2*x,2*y

x,y=3,4
n=0.1
for i in range(100):
    z=func(x,y)
    print(f'{i}:{z:.2f}')
    dx,dy=der(x,y)
    x,y=x-dx*n,y-dy*n
