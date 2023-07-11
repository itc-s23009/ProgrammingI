x = True
y = False
z = None
# andやorよりもisやnotが先に判定される。
print(x and z is None)
print(not x or not y)
print(x and not y and z is None)
