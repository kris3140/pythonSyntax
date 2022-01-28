
print('\n LOOP through STRINGS')
myString = 'dit is een tekst'

for i, letter in enumerate(myString):
    print('item nr:', i, ' / letter:', letter, end='')
    print(' ', myString[i])
# see also list

for letter in myString:
    print(letter, end='')


print('\n\n LOOP through LIST')
myList = ('apple', 'banana', 'cherry')

for i, item in enumerate(myList):
    print('item nr:', i, 'item:', item)

for i in range(len(myList)):
    print('item nr:', i)

for item in myList:
    print('item:', item, end=' ')
print()

i = 0
while i < len(myList):
    print('met while:', myList[i])
    i += 1
print()

if 'apple' in myList:
    print('there is an', myList[0], 'in my list')



print('\n\n LOOP through DICT')
myPet= {'name': 'Zini', 'species': 'kat', 'age': '7', 'color': 'black & white'}
print()

for k, v in myPet.items():
    print('key:', k, '/ value:', v)

print()
if 'Zini' in myPet.values():
    print(myPet['name'], 'is de naam van uw', myPet['species'])


# check if a key exists
print()
print(myPet.get('name', 0))
print()




print('\n update a DICT' )
dict = {}
key = 'cats'
value = '1'
dict[key] = value

dict2 = {}
dict2.update({"color": "red"})

print(dict)
print(dict2)



