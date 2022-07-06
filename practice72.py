def f(y):
    x = 2
    return g(x)

def g(x):
    global x
    x = 4
    return x*y

x = 0
res = f(x)
print('x= {}, f(0) = {}'.format(x, res))