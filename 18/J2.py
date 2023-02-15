N = int(input())
yesterday = list(input())
today = list(input())

counter = 0
for i in range(N):
    if yesterday[i] == 'C' and today[i] == 'C':
        counter += 1

print(counter)