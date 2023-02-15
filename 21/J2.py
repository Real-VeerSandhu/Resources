N = int(input())

auction = []
for i in range(2 * N):
    auction.append(input())

names = []
for i in range(0, len(auction), 2):
    names.append(auction[i])

money = []
for i in range(1, len(auction), 2):
    money.append(auction[i])

money = [int(i) for i in money]

print(names[money.index(max(money))])