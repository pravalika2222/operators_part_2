'''relational/comparision operators'''
'relatonal means- the o/p may get in the boolen form '
# a=int(input("enter the value of a:"))   #  2
# b=int(input("enter the value of b:"))   #  3
# print(f"the value of {a} > {b} is {a>b}")     #  2>3 is False
# print(f"the value of {a} < {b} is {a<b}")     #  2<3 is True
# print(f"the value of {a} >= {b} is {a>=b}")   #  2>=3 is False
# print(f"the value of {a} <= {b} is {a<=b}")   #  2<=3 is True
# print(f"the value of {a} == {b} is {a==b}")   #  2==3 is False
# print(f"the value of {a} != {b} is {a!=b}")   #  2!=3 is True

'here the o/p may get in the form of true & false value means true-1 & false-0'
# a=int(input("enter the value of a:"))     # 4
# b=int(input("enter the value of b:"))     # 6
# print("the value of %d<%d=%d"%(a,b,a<b))  # 4<6=1
# print("the value of a=%d , b=%d and a<b=%d"%(a,b,a<b))        # 4<6=1 - true
# print("the value of a=%d , b=%d and a>b=%d"%(a,b,a>b))        # 4>6=0 - false
# print("the value of a=%d , b=%d and a>=b=%d"%(a,b,a>=b))      # 4>=6=0 - false
# print("the value of a=%d , b=%d and a<=b=%d"%(a,b,a<=b))      # 4<=6=1 - true
# print("the value of a=%d , b=%d and a==b=%d"%(a,b,a==b))      # 4==6=0 - false
# print("the value of a=%d , b=%d and a!=b=%d"%(a,b,a!=b))      # 4!=6=1 - true

'''logical operators'''
'in python logical operators are represented by "words"'
# a=int(input("enter the value of a:"))       # 5
# b=int(input("enter the value of b:"))       # 6
# print("the value of a<b and b>a is {}".format(a<b and b>a))     # True
# print("the value of a>b and a<b is {}".format(a>b and b<a))     # False
# print("the value of a!=b and a==b is {}".format(a!=b and a==b)) # False
# print("the value of a==b or a>b is {}".format(a==b or a>b))     # False
# print("the value of a!=b or a<b is {}".format(a!=b or a<b))     # True
# print("the opposite of {}=={} is {}".format(a,b,not a==b))      # True 
# print("the opposite of {}!={} is {}".format(a,b,not a!=b))      # False

'''bitwise operators'''
'in python bitwise operators are represented by "symbols"'
# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# c=int(input("enter the value of c:"))
# print("the value of {} & {} is {}".format(a,b,a&b))   # 0
# print("the value of {} | {} is {}".format(a,b,a|b))   # 6
# """note:  the  formula for negative (~) is -(value+1)"""
# print("the value of ~{} is {}".format(a,~a))          # -3
# print("the value of ~{} is {}".format(c,~c))         # -6

'''identity operators'''
# a=20
# b=2

# if (a is b):
#     print("a and b have same identity")
# else:
#     print("a and b do not have same identity")

# if (id(a) == id(b)):
#     print("a and b have same identity")
# else:
#     print("a and b do not have same idnetity")

# x=5
# print(type(x) is int)         # True
# print(type(x) is not float)   # True
# print(type(x) is float)       # False 
# x=2.33
# print(type(x) is float)         # True
# print(type(x) is int)           # False
# print(type(x) is not float)     # False  

'''membership operator'''
# name=['akhil','vijay','vinay','vicky','vasu','rajesh','prava','tej','dakshu']
# print('akhil' in name)       # True 
# print('tej' in name)         # True
# print('vicky' in name)       # True
# print('prava' in name)       # true
# print('rama' not in name)    # true
# print('nishu' not in name)    # true
# print('cherry' in name)       # false
# print('rinky' in name)        # false
# name.sort()
# print(name)    # ['akhi','dakshu','prava','rajesh','tej','vasu','vicky','vijay','vinay']
# name=['p','r','a','v','a']
# # name.sort()
# # print(*name)     #   a a p r v
# name.sort(reverse=True)
# print(name)        #    ['v' ,'r', 'p', 'a', 'a']
# for i in name:
#     print(i)        # v
#                     # r
#                     # p
#                     # a
#                     # a

'''shift operator  (>>Right /2 and <<left *2)  '''
# a=30
# print(a>>1)         #  15
# print(a>>2)         #  7
# print(a>>3)         #  3 
# print(a>>4)         #  1
# b=3
# print(b<<1)          #  6
# print(b<<2)          #  12
# print(b<<3)          #  24
# print(b<<4)          #   48