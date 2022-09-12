def hello():
    print('hellow word')
hello()


def media (val1, val2 , val3):
    return (val1 + val2 + val3)/3
print(media(20,25,30))

def media (val1 = 0, val2 = 0 , val3 = 0):
    return (val1 + val2 + val3)/3

print(media())

def media2(*args):
    return sum(args)/len(args)
print(media2(50,25,10))

def print_inf(**keywargs):
    print(keywargs, type(keywargs))
print_inf(name='adeir',idade= 27)