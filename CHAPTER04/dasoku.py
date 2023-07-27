a = list(range(100))
s = ''
for i in a:
    s += "{:2d},".format(i)
    if i % 10 == 9:
        s += "\n"
print(s)
