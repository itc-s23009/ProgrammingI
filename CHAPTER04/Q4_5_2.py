a = ["1..0,2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2","2.1,3.1,4.5"]
def str(a):
    p = a.split(",")
    return list(map(float, p)
