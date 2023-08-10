a = {x for x in range(21)}
b = {x for x in range(21) if x % 2 == 0}
c = a - b
print(c)
