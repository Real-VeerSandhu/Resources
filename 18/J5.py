n = int(input())

pages_truth = []
for i in range(n):
    pages_truth.append(i)

inputs = []
for i in range(n):
    inputs.append(input())

book = []
for i in inputs:
    book.append([int(j) for j in i.split()])

def reach_pages():
    pages_reached = []
    if book[0] == [0]:
        return 'N'
    else:
        pages_reached.append(0)
        for i in book:
            for j in i[1:]:
                pages_reached.append(j-1)
        if list(dict.fromkeys(pages_reached)) == pages_truth:
            return 'Y', list(dict.fromkeys(pages_reached))
        else:
            return 'N', list(dict.fromkeys(pages_reached))
        
def shortest_path():
    path_len = 1
    if book[0] == [0]:
        path_len = 1
    else:
        paths = []
        for i in book:
            if i != [0]:
                print(i)
                for j in i[:1]:
                    if book[j - 1] == [0]:
                        path_len += 1
                        break
                    else:
                        path_len += 1
                        # new_page = book[j - 1]
    print(path_len)

print('*'*50)
print(f'Ground Truth: {pages_truth}', 'Actual:', reach_pages())

print('\n')
print('/'*50)
shortest_path()

# Most likely finished Y/N part, need to find path length for story that continues on multiple pages
