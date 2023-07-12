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
c = random.choice(alphabet)
d = random.choice(alphabet)
e = random.choice(alphabet)
f = random.choice(alphabet)
g = random.choice(alphabet)
h = random.choice(alphabet)
i = random.choice(alphabet)
j = 0

while True:
    if a == "k" and b == "o" and c == "h" and d == "m" and e == "a" and f == "y" and g == "u" and h == "t" and i == "o":
        print("KOHAMA, YUTO")
        print(str(j) + "回しました。")
        break
    else:
        print(a, b, c, d, e, f, g, h, i, end=' ')
        a = random.choice(alphabet)
        b = random.choice(alphabet)
        c = random.choice(alphabet)
        d = random.choice(alphabet)
        e = random.choice(alphabet)
        f = random.choice(alphabet)
        g = random.choice(alphabet)
        h = random.choice(alphabet)
        i = random.choice(alphabet)
        j += 1

