import re

'''
link for testing the result of a regex on a string: https://pythex.org/
link for advanced regex tutuorials : 

\d = numeric digit = [0-9]
\d\d\d = \d{3}
\D = any character that is not a numeric digit

\w = letter, numeric digit or underscore = [a-zA-Z0-9_]
\w\w = \w{2}
\W = any character that is not a letter, numeric digit or underscore = [^a-zA-Z_]
caret within a set inverses the set content

\s = any space, tab or newline character 
\S = any character that is not a space, tab or newline character

. = matches any charachter except newline

(ha){3,5} => hahaha or hahahaha or hahahahaha (greedy)
(ha){3,5}? => hahaha or hahahaha or hahahahaha (not greedy)

* == {0, }
? == {0,1}
+ == {1, }

() = group
\(?\d\)? = escaping a group, so searching for a digit between parentheses or not

[] = set eg: [aouio] or [a-zA-Z]
'''

#1
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = regex.search('My number is 415-555-4242. My mobile number is 421-153-7896')
print('1: ', mo)           # mo =  match object
print('1: ', mo.group())   # without parameters if there are no groups in the regex
print(' ')
# 1:  <re.Match object; span=(13, 25), match='415-555-4242'>
# 1:  415-555-4242


# 1b without compile
regex = r'\d\d\d-\d\d\d-\d\d\d\d'
text = 'My number is 415-555-4242. My mobile number is 421-153-7896'
mo = re.search(regex ,text )
print('1: ', mo)           # match =  match object
print('1: ', mo.group())   # without parameters if there are no groups in the regex
print(' ')
# 1:  <re.Match object; span=(13, 25), match='415-555-4242'>
# 1:  415-555-4242

#2
regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = regex.search('My number is 415-555-4242.')
print('2: ', mo.group(1))
print('2: ', mo.group(2))  # parameters indicating the groups () in the regex
print('2: ', mo.group(0))
print('')
# 2:  415
# 2:  555-4242
# 2:  415-555-4242



#3
regex = re.compile(r'(\({0,1}\d\d\d\)?)-(\d\d\d-\d\d\d\d)')
mo = regex.search('My number is 415-555-4242.')
print('3: ', mo.group(1))
print('3: ', mo.group(2))
print(' ')
# 3:  415
# 3:  555-4242


#3 bis idem without compile
regex = r'(\({0,1}\d\d\d\)?)-(\d\d\d-\d\d\d\d)'
text = 'My number is 415-555-4242.'
mo = re.search(regex, text)
print('3b: ', mo.group(1))
print('3b: ', mo.group(2))
print(' ')
# 3:  415
# 3:  555-4242


#4 findall
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # no groups
match = regex.findall('My number is 415-555-4242. My mobile number is 421-153-7896')
print('4: ', match)
print(' ')
# 4:  ['415-555-4242', '421-153-7896']

#5 findall with groups and without compile
regex = r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)'   # groups
text = 'My number is 415-555-4242. My mobile number is 421-153-7896'
match = re.findall(regex, text)
print('5: ', match)
print(' ')
# 5:  [('415', '555', '4242'), ('421', '153', '7896')]

#6
regex = r'\d+,?\d+'
text = '1,235.25'
mo = re.search(regex, text)
match = mo.group()
match = match.replace(',', '.')
print('6', mo)
print('6', match)
print()
# 6 <re.Match object; span=(0, 5), match='1,235'>
# 6 1.235


#7
regex = r'([a-zA-Z]+\s\d+)'    # zoek een woord + spatie + getal (+ = minstens 1)
text = r'I was born on June 11 and you on August 25th.'
match = re.findall(regex, text)
print('7', match)
print()
# 7 ['June 11', 'August 25']


# re.search geeft een match object waar je met group de match uithaalt
# re.start geeft uit het match object de index waar de match begint
# re.findall geeft een list van matches

#8
regex = re.compile(r"\s")
mo = regex.search('No rain in Spain')
position = mo.start()
print('8:', position)
# 8: 2

#8b without compile
regex = r"\s"
text = 'No rain in Spain'
mo = re.search(regex, text)
startPosition = mo.start()
endPosition = mo.end()
match = mo.group()
print('8b:', startPosition)
print('8b:', endPosition)
print('8b:', match)
print()
# 8b: 2
# 8b: 3
# 8b:

#9
regex = re.compile('\d')
regex2 = re.compile('\d+')
print('9',  regex.findall("I went to him at 11 A.M. on 4th July 1886"))
print('9', regex2.findall("I went to him at 11 A.M. on 4th July 1886"))
# 9 ['1', '1', '4', '1', '8', '8', '6']
# 9 ['11', '4', '1886']


regex = re.compile('\w')
regex2 = re.compile('\w+')
regex3 = re.compile('\W')
print('10: ',  regex.findall("He said * in some_lang."))
print('10: ', regex2.findall("He said * in some_lang."))
print('10: ', regex3.findall("He said * in some_lang."))
# 10:  ['H', 'e', 's', 'a', 'i', 'd', 'i', 'n', 's', 'o', 'm', 'e', '_', 'l', 'a', 'n', 'g']
# 10:  ['He', 'said', 'in', 'some_lang']
# 10:  [' ', ' ', '*', ' ', ' ', '.']



