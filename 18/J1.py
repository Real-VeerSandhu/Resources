digits = []
for i in range(4):
    digits.append(int(input()))

if digits[0] == 8 or digits[0] == 9:
    if digits[3] == 8 or digits[3] == 9:
        if digits[1] == digits[2]:
            print('ignore')
        else:
            print('answer')
    else:
        print('answer')
else:
    print('answer')