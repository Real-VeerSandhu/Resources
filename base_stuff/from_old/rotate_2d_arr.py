n = int(input())

inputs = []
for i in range(n):
    inputs.append(input())

data = []
for i in inputs:
    data.append([int(j) for j in i.split()])

def rotate_90_clockwise(input_arr):
    A = input_arr.copy()
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return A

print(data)
print(rotate_90_clockwise(data.copy()))
print(data)