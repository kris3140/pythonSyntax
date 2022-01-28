import ezsheets

# documentation:
# https://ezsheets.readthedocs.io/en/latest/



# step by step setup of authorisation:
# https://developers.google.com/sheets/api/quickstart/python/
# steps to complete:
# create a project (=quickstart) : done
# enable API (google sheets API) : done
# create credentials :
# section : Configure the OAuth consent screen : done

# section : Create a OAuth client ID credential
# click link : Create Desktop application credentials. Use this section for non-JavaScript quickstarts.
# here you create a json file
# then run quickstart.py
#


ss = ezsheets.Spreadsheet('1I2ERJptS8cvDaNnBjAchCgjFEHOEXfD8ag8X1UlHWVM')  # Aandelen Dbase S&P500
print(ss)
print(ss.title)
print(ss.sheetTitles)
print(ss.sheets)

sheet = ss[0]
sheet2 = ss['Selection']



# write content to Google Sheets
sheet['A1'] = 'test'        # cell A1

sheet[2, 1] = 'test2'       # cell B1 = col2 row1

my_list = ['test a', 'test b', 'test c']
for i, tekst in enumerate(my_list):
    sheet[i+1, 2] = tekst

sheet.updateRow(3, ['test', 'test2', 'test3']    #  or : sheet.updateColumn(1, [])


# get content from Google Sheets
print(sheet['A1'])          # prints content of cell A1
content = sheet[2, 1]       # col2 row1
print(content)              # prints content of cell B1

myList = sheet.getColumn('A')   # or : getRow(2)
print(myList)

