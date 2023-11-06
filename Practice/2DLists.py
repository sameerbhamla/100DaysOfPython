#M x N 2d array

col=5
row=5

zeros = [ [0] * col for _ in range(row) ]

zeros[2][2] = 5
print(zeros)