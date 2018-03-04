#OOb python in pycharm
a = 'ADFDSGADF'
for c in a:
    print(c)

l1 =[1,3,4]
l2=[7,8,8,4,4,6]

for a,b in zip(l1,l2):
    print(a,b)
#only the first several parts will be printout

for a,b in zip(l1,l2):
    if a<b:
        print(a)
    else:
        print(b)

def add(a,b):
    '''
    add two numbers together
    :param1 a
    :param2 b
    :return the sumup values
    '''
    return(a+b)

print(add(5,6))
b=add(9,4)
print(b)

def isMetro(city):
    l=['sfo','nyc','la']
    if city in l:
        return True
    else:
        return False
print(isMetro('DC'))

#having a local scope

a=10

def test_method(a):
    print('value of local a is:'+a)

print(test_method("0"))


    # golbal variables
a = 10

def test_method():
    global a
    print('value of a inside the method is :' + str(a))
    a = 2
    print('New value of "a" inside the method is changed to ' + str(a))

print(a)
test_method()
print(a)




















