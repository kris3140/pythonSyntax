import pandas as pd



data = pd.read_csv('bevolking.csv', sep=";", index_col=0)

print(data["Population"])    # geeft de kolom ‘Population’ als een data serie
print(data[["Population"]])  # geeft de kolom ‘Population’ als een DataFrame
print();print()

# dubbele punt notatie = los
print(data.iloc[0:5, 1:]  ,"\n")
print(data.loc["Vlaanderen" : "Brussel", "Population" ]  ,"\n")

# komma notatie = met vierkante haakjes
print(data.iloc[[0,1,2,3,4,5] , 2 ]  ,"\n")
print(data.loc[["Vlaanderen" , "Brussel"], "Population" ]  ,"\n")



# data
#            Age Group Gender  Population
# Region
# Vlaanderen       18-  Women      630037
# Vlaanderen       18-    Men      659950
# Vlaanderen     18-64  Women     1976581
# Vlaanderen     18-64    Men     2009936
# Vlaanderen       65+  Women      752827
# Vlaanderen       65+    Men      623731
# Brussel          18-  Women      134558
# Brussel          18-    Men      140995
# Brussel        18-64  Women      392440
# Brussel        18-64    Men      392951
# Brussel          65+  Women       93898
# Brussel          65+    Men       65128
# Wallonie         18-  Women      365068
# Wallonie         18-    Men      381514
# Wallonie       18-64  Women     1103755
# Wallonie       18-64    Men     1104332
# Wallonie         65+  Women      394863
# Wallonie         65+    Men      298674