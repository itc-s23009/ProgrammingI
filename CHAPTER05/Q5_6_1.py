a = {x for x in 'abcabcabc' if x not in 'ab'}
b = {y for y in 'abcabcabc' if y not in 'bc'}
a | b

 # print(a) >> {c}
 # print(b) >> {a}
 # {'a','c'}
