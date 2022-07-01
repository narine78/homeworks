# functions
# def 
# lambda 
# def fun():
#     print('Hello')
# fun()

# def fun():
#     return 'Hello'
# print(fun())

# def func(x):
#     return x ** 2
# print(func(int(input('Enter number -->>'))))


# def func(x, y, z):
#     return x + y / z
# print(func(y = 1, z = 2, x = 3))

# def fun(*x):
#     return x
# print(fun(2, 3, 4, 6, 'Hello'))

# def fun(**x):
#     return x
# print(fun(a = 7, b = 4, c = 9))

# x = lambda a, b: a + b
# print(x(2, 4))

# x = lambda a, b: print(a+ b); x(8, 9)

# def func(x:int, y:str, z:bool) -> list:
#     return [x, y, z]
# print(func(4, 'a', True))

# def func():
#     global x
#     x = 5
#     return x
# print(func())
# print(x +7)

# def fun(*x):
#     return sum(x)
# print(fun(7, 5, 6, 12, 3))

# def func(x, res):
#     for i in x:
#         res += 1
#     return res
# print(func('Hello', 0))

# def func(*x, res=0):
#     for i in x:
#         res += i
#     return res
# print(func(7, 5, 3, 7, 0))



text_1 =input('Enter any text -->>')
text_2 =str(input('Enter any number -->>'))
def func(text_1, text_2, res = 0):
    for i in text_1:
        res += 1
    return res 
    for j in text_2:
        res_1 +=1
    return res_1 
print(func(res, res_1))