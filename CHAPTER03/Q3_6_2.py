import random

a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
b = random.sample(a, k=4)
c = ''.join(b)

while True:
    val = input("4桁の数字を入力してください: ")
    if len(val) != 4 or not val.isdigit():
        print("無効な入力です。4桁の数字を入力してください。")
        continue

    if val == c:
        print('great!')
        break
    else:
        print("Try!")
        answer = ''
        for i in range(4):
            if c[i] == val[i]:
                answer += c[i]
            else:
                answer += 'x'
        print('-> ' + answer)

