s = ''
for i in range(1, 10):
    for j in range(1, 10):
        b = i * j
        s += "{:2d},".format(b)
    s += '\n'

print(s)


s = '\n'.join([' '.join(f"{i*j:2d}" for j in range(1, 10)) for i in range(1, 10)])
print(s)

