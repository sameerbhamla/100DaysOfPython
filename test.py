def f(x):
    for i in range(len(x)//2):
        x[i],x[:-1] = x[:-1],x[i]
    return x


def list_em(x):
    return removeDuplicate(sorted(x))



y='ADDEAADEE'
x= [1,2,3,4,5]
print(f(x))