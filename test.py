def f(x):
    y = []
    for i in range(x):
        y.append(i)
        print(y)
        y.append([i])
        print(y)
        y.append(i)
        print(y)
    
    f(2)