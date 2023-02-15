n = int(input())

# Transform Input into 2D Array
inputs = []
for i in range(n):
    inputs.append(input())

data = []
for i in inputs:
    data.append([int(j) for j in i.split()])

x = len(data[0])
y = len(data) 

# Define Rotation and Checking Functions
def rotate90(orginal_data):
    new_data = []
    for i in range(x):
        temp = []
        for j in orginal_data:
            temp.append(j[i])
        new_data.append(temp[::-1])
    return new_data

def checkdata(given_data):
    passes_case = True
    
    for i in given_data:
        if i != sorted(i):
            passes_case = False
            break

    temp_firsts = []
    for j in given_data:
        temp_firsts.append(j[0])

    if temp_firsts != sorted(temp_firsts):
        passes_case = False
    return passes_case

def find_correct():
    data_0 = data
    data_90 = rotate90(data)
    data_180 = rotate90(rotate90(data))
    data_270 = rotate90(rotate90(rotate90(data)))

    for dataset in [data_0, data_90, data_180, data_270]:
        if checkdata(dataset):
            return dataset

# Print Correct Oriented Array
for i in find_correct():
    for j in i:
        print(j, end=' ')
    print()

# Sunflowers: Full Score