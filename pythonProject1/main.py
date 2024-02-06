x = [1,2,[3,[4,5,[6],7,[8,9,[[[11,12]]]]]]]

def freeThem(x):
    z = []
    for i in x:
        if type(i) == type(1):
            z.append(i)
        else:
            z.extend(freeThem(i))

    return z


def oddEven(m,n):
    for i in range(m,n+1):
        if i % 2 == 0:
            yield i
    for j in range(m,n+1):
        if j % 2 == 0:
            yield j


def even_fibonacci_generator(n):
    if n <= 0:
        return 0
    third,first = 0,0
    second = 2
    count = 0
    while True:
        third = first + second
        second,first = first + second, second
        if(third % 2  == 0):
            yield third
            count += 1
        if count == n:
            break


def create_dictionary(n):
    coutnDict = dict()
    for i in range(10):
        coutnDict[str(i)] = 0
    for i in range(n+1):
        for char in str(i):
            coutnDict[char] +=1
    return coutnDict



#gen = oddEven(2,7)
#for i in range(10):
#    print(next(gen))

#result = create_dictionary(200)
#for digit,count in result.items():
#    print(f'Digit {digit}: {count} times')
print(freeThem(x))