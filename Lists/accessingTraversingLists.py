shoppingList = ['butter', 'eggs', 'bread']
print(shoppingList[0])

print('milk' in shoppingList)
print(shoppingList[-1])

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + '!'
    print(shoppingList[i])