import random

a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
b = (random.sample(a,4, k=4))
c = (''.join(b))
while True:
    val = input()
    if val == c:
        print('great!')
        break
    else:
        print("Try!")
