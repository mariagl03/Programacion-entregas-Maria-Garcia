W = False
X = True
Y = False
Z = True

print("C", not (W or not Y) and X or Z)
print("F", not X and Y and ( not Z or not X))