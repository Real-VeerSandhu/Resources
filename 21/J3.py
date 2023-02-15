flag = True

raws = []
while flag:
    raws.append(input())
    if '99999' in raws:
        flag = False

int_raws = [int(i) for i in raws]
raws = raws[:-1]

steps = []
for i in range(len(raws)):
    steps.append([ (raws[i][0:2]), (raws[i][2:]) ]) 

directions = []
for i in steps:
    sum = int(i[0][0]) + int (i[0][1])
    if sum == 0:
        directions.append('void')
    elif (sum % 2 == 1):
        directions.append('left')
    elif (sum % 2 == 0):
        directions.append('right')

for i in range(len(directions)):
    if directions[i] == 'void':
        directions[i] = directions[i-1] 

distances = []
for i in steps:
    distances.append(i[1])

for i in range(len(directions)):
    print(directions[i], distances[i])
