def sum(n):
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = a, a + b
