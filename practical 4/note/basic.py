# #number
# a = 12
# b = 2 
# print(a + b)#加法  14
# print(a - b)#减法  10
# print(a * b)#乘法  24
# print(a / b)#除法  6.0
# print(a % b)#余数  0
# print(a ** b)#幂   144 
# print(a // b)#整除 6

# #word
# a = 'hello'
# b = 'world'
# print(a + b)#拼接  helloworld
# print(a * 2)#重复  hellohello
# print(a[1])#索引  e
# print(a[1:5])#切片  el
# print('h' in a)#成员  True
# print('M' not in a)#非成员  True
# print(a == b)#比较  False
# print(a != b)#不等于  True

# c = "four"
# d = "two"
# print(c+2*d)    #fourtwotwo

# a = "2"
# b = "4"
# print(a+b)    #24

# #list
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# print(a + b)#拼接  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a * 2)#重复  [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(a[1])#索引  2

# a = [1, 2, 3, 4, 5]
# print(a[1:3])#切片  [2, 3]
# print(3 in a)#成员  True
# print(6 not in a)#非成员  True
# print(a == b)#比较  False
# print(a !=
# b)#不等于  True

# #tuple
# a = (1, 2, 3, 4, 5)
# b = (6, 7, 8, 9, 10)
# print(a + b)#拼接  (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(a * 2)#重复  (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
# print(a[1])#索引  2
# print(a[1:3])#切片  (2, 3)
# print(3 in a)#成员  True
# print(6 not in a)#非成员  True
# print(a == b)#比较  False
# print(a != b)#不等于  True

# #dict
# a = {'name': 'Tom', 'age': 20}

# print(a['name'])#索引  Tom
# print(a['age'])#索引  20
# print(a.keys())#键  dict_keys(['name', 'age'])
# print(a.values())#值  dict_values(['Tom', 20])
# print(a.items())#键值对  dict_items([('name', 'Tom'), ('age', 20)])
# print('name' in a)#成员  True
# print('Tom' not in a)#非成员  True
# print(a == b)#比较  False
# print(a !=
# b)#不等于  True

# #set
# a = {1, 2, 3, 4, 5}
# b = {6, 7, 8, 9, 10}
# print(a | b)#并集  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(a & b)#交集  set()
# print(a - b)#差集  {1, 2, 3, 4, 5}
# print(a ^ b)#对称差集  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(3 in a)#成员  True
# print(6 not in a)#非成员  True
# print(a == b)#比较  False
# print(a != b)#不等于  True

# #bool（Boolean variables）
# a = True
# b = False
# print(a and b)#与  False
# print(a or b)#或  True
# print(not a)#非  False
# print(a == b)#比较  False
# print(a != b)#不等于  True

# #None
# a = None
# print(a)#None  None
# print(a == 1)#比较  False
# print(a != 1)#不等于  True

# #if
# a = 1
# b = 2
# if a > b:
#     print('a > b')
# elif a < b:
#     print('a < b')
# else:
#     print('a = b')

# if x%2 == 0:
#     print("Even")
# elif x%2 == 1:
#     print("Odd")
# else:
#     print("x is not an integer")
# x = 3.14 #Not an integer
# x = 4 #Even
# x = 5 #Odd
# #while
# a = 1
# while a < 5:
#     print(a)
#     a += 1
# import random
# j = 0
# while j != 23: 
#     j = random.randint(0, 100)
# print(j)

# #for   
# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i)

# #break
# a = 1
# while a < 5:
#     print(a)
#     if a == 3:
#         break
#     a += 1
# import random
# j = 0
# while 1==1:
#     j = random.randint(0, 100)
#     print(j)
#     if j == 23:
#         break

# #continue
# a = 1
# while a < 5:
#     a += 1
#     if a == 3:
#         continue
#     print(a)

# #range
# for i in range(5):#(end) 0-4 5个
#     print(i)

# for i in range(1, 5):
#     print(i)

# for i in range(1, 5, 2):#(start, end, step)
#     print(i)

# #enumerate
# a = ['a', 'b', 'c', 'd', 'e']
# for i, j in enumerate(a):
#     print(i, j)

# #zip
# a = ['a', 'b', 'c', 'd', 'e']
# b = [1, 2, 3, 4, 5]
# for i, j in zip(a, b):
#     print(i, j)

# #booleans are often used for comparation   
# a = 1
# b = 2
# print(a > b)#False
# print(a < b)#True
# print(a == b)#False #equal
# print(a != b)#True #not equal
# print(a >= b)#False #greater than or equal to
# print(a <= b)#True #less than or equal to

# #Truth tables
# #And(both are true)
# a = True
# b = True
# print(a and b)#True
# a = True
# b = False
# print(a and b)#False
# a = False
# b = False
# print(a and b)#False
# a = False
# b = True
# print(a and b)#False

# #Or(at least one is true)
# a = True
# b = False
# print(a or b)#True
# a = True
# b = True
# print(a or b)#True
# a = False
# b = True
# print(a or b)#True
# a = False
# b = False
# print(a or b)#False

# #Not
# a = True
# print(not a)#False
# a = False
# print(not a)#True

# #either or(only one is true)
# a = True
# b = False
# print(a ^ b)#True
# a = True
# b = True
# print(a ^ b)#False
# a = False
# b = True
# print(a ^ b)#True
# a = False
# b = False
# print(a ^ b)#False

# x = true or y = ture  and x != y
# #True or False and True != False

# #for loop
# count = 25
# print(count)
# for i in range(1, 25): #range(start, end) 
#     count = count - 1 
#     print("count:", count) #print 