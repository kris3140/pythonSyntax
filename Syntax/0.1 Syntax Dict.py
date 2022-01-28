cats = {
    "Name": "Zini",
    "Tail": "Long"
}

key = 'number'
value = 1
cats[key] = value

cats["food"] = 'mice'
cats.update({"color": "red"})

print(cats)

# Filter
myDict = { 'jan': 31, 'feb': 28, 'mar': 31, 'april': 30, 'may': 31, 'june': 30 }

# With Lambda
output = dict(filter(lambda item: item[1] == 31, myDict.items() ))    # item[0] = key ; item[1] = value
print(output)

# With Comprehension
output = { key:value for (key,value) in myDict.items() if value == 31}
print(output)





