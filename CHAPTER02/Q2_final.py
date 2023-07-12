import random

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
a = random.choice(alphabet)
b = random.choice(alphabet)
c = 0

while True:
    if a == "k" and b == "y":
        print("K,Y")
        print(str(c) + '回しました。')
        break
    else:
        for i in (a, b):
            print(a, b)
        a = random.choice(alphabet)
        b = random.choice(alphabet)
        c += 1
