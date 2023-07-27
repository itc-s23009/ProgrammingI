a = [sum, min, max]
number_list = list(range(1, 11))

for func in a:
    print("Function: {}, result: {}".format(func.__name__, func(number_list)))

