from math import pi

straal = 4
oppervlakte = straal**2 * pi
opp = format((straal**2 * pi), ".2f")

print("1/ opp van de cirkel met straal %d is %f" % (straal, oppervlakte))
print("2/ opp van de cirkel met straal %d is %.2f" % (straal, oppervlakte))

print("3/ opp van de cirkel met straal", straal, "is", oppervlakte)
print("4/ opp van de cirkel met straal", straal, "is", opp)
print("4b/ opp vn de cirkel met straal", straal, "is", format(oppervlakte, ".2f"))

# 5
print(f"5/ opp van de cirkel met straal {straal} is {oppervlakte:.2f}")

print("6/ opp van de cirkel met straal {} is {}".format(straal, opp))
print("7/ opp van de cirkel met straal {} is {}".format(straal, oppervlakte))

# 8 f-string

print(f"8/ opp van de cirkel met straal {straal:.0f} is {oppervlakte:.2f}")





# %f = float
# %d = decimal integer
# %s = string