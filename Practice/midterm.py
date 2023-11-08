def f(x):
    for i in range(len(x)):
        x[i],x[len(x)-1] = x[len(x)-1],x[i]
    return x


def lists(*x):
    return sum(*x),max(*x),min(*x)


def test(x):
    pass
 #   return x.sort(lambda key: average(key))

a = [1,2,3,4,5]
print(f(a))
#print(test([[16,99],[1,2,3,6,5],[1,2,0]]))

