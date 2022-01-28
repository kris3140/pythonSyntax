
myList = [10, 20, 30, 40]
result = list(map(lambda x: x * 2, myList))
print(result, '\n')

myOtherList = [10, 20, 30, 40]
result = list(map(lambda x, y: x + y, myList, myOtherList))
print(result, '\n')

result = list(filter(lambda x: x % 20 == 0, myList))
print(result)
print()

# Using list comprehension to iterate through loop
text = 'Geeks 4 Geeks!'
myList = [char for char in text.upper()]
print(myList)
