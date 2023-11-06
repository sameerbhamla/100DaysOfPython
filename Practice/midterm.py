def f(x):
    n = len(x)
    for i in range(n,-1):
        x[n-i],x[i] = x[i],x[n-i]
    return x


def lists(*x):
    return sum(*x),max(*x),min(*x)


def test(x):
    return x.sorted(key=lambda x: (sum(x))//2)

a = [1,2,3,4,5]
print(f(a))
#print(test([[16,99],[1,2,3,6,5],[1,2,0]]))

