temp = int(input())

pressure = int(5*temp - 400)

sea_level = 0
if pressure == 100:
    sea_level = 0
elif pressure > 100:
    sea_level = -1
else:
    sea_level = 1

print(pressure)
print(sea_level) 