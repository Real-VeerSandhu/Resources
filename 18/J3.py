cities = input().split(' ')

distances = [int(i) for i in cities]

first = distances[0]
second = distances[1]
third = distances[2]
forth = distances[3]

row1 = [0, first, first+second, first+second+third, first+second+third+forth]
row2 = [first, 0, second, second+third, second+third+forth]
row3 = [first+second, second, 0, third, third+forth]
row4 = [first+second+third, second+third, third, 0, forth]
row5 = [first+second+third+forth, second+third+forth, third+forth, forth, 0]

answer = [row1, row2, row3, row4, row5]

for row in answer:
    for i in row:
        print(i, end=' ')
    print()

# or do this:

# in1 = input()

# arr = in1.split()
# arr =[int(i) for i in arr]

# first = arr[0]
# sec = arr[1]
# third = arr[2]
# fourth = arr[3]

# city_loc = [0, arr[0], arr[0] + arr[1], arr[0] + arr[1] + arr[2],  arr[0] + arr[1] + arr[2] + arr[3]]

# sec = []

# def find_distance(idx):
#     distances = []
#     for city in city_loc:
#         distances.append(abs(city - city_loc[idx]))
#     return distances

# for i in range(5):
#     output = (find_distance(i))
#     for number in output:
#         print(number, end=' ')
#     print('')