list = []
while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    list.append(value)
average = sum(list)/len(list)
print('Average: ', average)