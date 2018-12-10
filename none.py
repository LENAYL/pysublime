# print("1024 * 768 = %d" % (1024 * 768))
# print('''line1
# ... line2
# ... line3''')
# print('''hello world \n
#  !!!''')
# print("%5d-%02d" % (3 , 1))
# print("%.2f"  % 3.1415926)
# print("%s %%" % 7)
# print("your score is %s zhan %s %%" % (59 , 7))
# print("the score of last year is %d and this year is %d enhance %.2f %%" %(71 , 85 , (85-71)/71))
# aa=1
# print(aa)
# print("she is a good girl %s" %("abd"))
# t=(1)
# print(t)
# age=20
# if age>=18:
# 	print("she is an adult and her age is %d" % 18)
# elif age>=6:
# 	print("she is a teenager")
# else :
	# print("she is a kid ")
# s=input("birth:")
# birth=int(s)
# if birth<2000:
# 	print("before 00")
# else :
# 	print("after 00")
# d=input("height:")
# a=input("weight:")
# height=float(d)
# weight=float(a)
# BMI=weight/(height*height)
# if BMI<18.5:
# 	print("太轻")
# elif 18.5<BMI<25:
# 	prinyt("正常")
# elif BMI>32:
# 	print("严重肥胖")
# else :
# 	print("肥胖")
# sum=0
# for x in range(101):
# 	sum=sum+x
# print(sum)
# sum=0
# n=99
# while n>0 :
# 	sum=sum+n
# 	n=n-2
# print(sum)

# L=['A','B','C']
# for x in L :
# 	print(x)
# n=0
# while n<10 :
# 	n=n+1
# 	if n%2==0 :
# 		continue
# 	print(n)
	
# print('END')
# s1=set([1,2,3])
# s2=set([2,3,4])
# print(s1&s2)
# print(s1|s2)
# def my_abbs(x):
# 	if x<0:
# 		return-x
# 	else:
# 		return x
# print(my_abbs(-20))
# import math
# def quadratic(a,b,c):
# 	d=b*b-4*a*c
# 	if d<0:
# 		print("none")
# 	else :
# 		x1=(-b+math.sqrt(d))/(2*a)
# 		x2=(-b-math.sqrt(d))/(2*a)
# 		return (x1,x2)
# print(quadratic(2,10,5))
# def power(x,n):
# 	s=1
# 	while n>0:
# 		n=n-1
# 		s=s*x
# 	return s
# print(power(3,3))
# def product(x,number):
# 	sum=1
# 	for i in number:
# 		sum=i*sum
# 	return (sum*x)
# print(product(2,[2,3,4]))
# def fact(n):
# 	if n==1:
# 		return 1
# 	return n*fact(n-1)
# print(fact(1000))
# def f(n):
# 	sum=1
# 	if n==1:
# 		return 1
# 	while n>1:
# 		sum=sum*n
# 		n=n-1
# 	return sum
# print(f(1000))
# 	
# L=[]
# n=1
# while 100 > n:
# 	L.append(n)
# 	n=n+2
# print(L)
# def trim(s):
# 	# while True:
# 	if s[0]==" ":
# 		return trim(s[1:])
# 	elif s[-1]==" ":
# 		return trim(s[:-1])
# 	else :
# 		return s
# # L=[, 2, 3, 1,]
# print(trim(' andhje '))
# print(trim(L))
# def find(l):
# 	max=-float("inf")
# 	min=float("inf")
# 	for i in l:
# 		if i>max:
# 			max=i
# 		if i<min:
# 			min=i
# 	return min,max
# l=[0, 1, 2, 3, 7, 9]
# print(find(l))
# print([x*x for x in range(1,11) if x%2==0])
# print([m+n for m in "ABC" for n in "abc"])
# import os
# print([d for d in os.listdir(".")])
# d={'x':'A', 'y':'B', 'z':'C'}
# print([k + '=' + v for k, v in d.items()])
# L1=['Hello', 'World', 18, 'Apple', None]
# L2=[]
# for i in L1:
# 	if isinstance(i,str):
# 		L2.append(i)
# L3=[x.lower() for x in L2]
# print(L3)
# L4=[x.lower() for x in L1 if isinstance(x,str)]
# print(L4)
# g=(x*x for x in range(10))
# print(g)
# print(next(g))
# print(next(g))
# for n in g:
# 	print(n)
# def fib(mmax):
# 	n=1
# 	L=[]
# 	m=0
# 	while n < mmax:
# 		if n <= 2:
# 			L.append(1)
# 			m=m+1
# 			n=n+1
# 		else:
# 			L.append(L[m-1] + L[m-2])
# 			m=m+1
# 			n=n+1
# 	return L
# print(fib(10))
# def product(line):
# 	L=[1]
# 	x=1
# 	while x < line:
# 		yield L
# 		L=[ L[0] ]+[ L[n] + L[n+1] for n in range(len(L)-1)] + [L[-1]]
# 		x=x+1
# 	return L
# LL=product(5)
# # print(product(10))
# for i in LL:
# 	print(i)
# def f(line):
# 	L=[1]
# 	x=1
# 	while x < line:
# 		yield L
# 		L= [2*len(L)+1] + [L[n] + L[n+1] for n in range(len(L)-1)] + [2*len(L)+1]
# 		x=x+1
# 	return L

# for i in f(10):
# 	print(i)
# def add(xx,y,f):
# 	return f(x)+f(y)
# x=-5
# y=-6
# f=abs
# print(add(x,y,f))
# print(list(range(10)))
# from functools import reduce
# name=['abd','AAA']
# def normalize(name):
# 	return name[0].upper() + name[1:].lower()
# # name=['abd', 'ASDE', 'ANSxsA']
# # print(normalize(name))
# # print(list(map(normalize,name))
# print(list(map(normalize,name)))
# from functools import reduce
# s=[1,2,3,4]
# def prob(s):
# 	def fn(x,y):
# 		return x*y
# 	return(reduce(fn,s))
# print(prob(s))
# def str2float(s):
# 	s0=s.split('.')
# 	s1=s0[0]
# 	s2=s0[1][::-1]
# 	dig={'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8 ,'9':9, '0':0}
# 	def f0(s):
# 		return dig[s]
# 	def f1(x,y=0):
# 		return x*10+y
# 	def f2(x,y=0):
# 		return x*0.1+y
# 	return reduce(f1,map(f0,s1)) + reduce(f2,map(f0,s2))*0.1
# s='123.123'
# print(str2float(s))
# def str2int(s):
# 	dig={'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8 ,'9':9, '0':0}
# 	return dig[s]
# s='123'
# print(list(map(str2int,s)))
# def fff(x,y):
# 	return x*10+y
# # print(reduce(fff,map(str2int,s)))
# def ff(s):
# 	name=s[0].upper() + s[1:].lower()
# 	return name
# ss=['adsf', 'AAASfc']
# print(list(map(ff,ss)))
# def prob(s):
# 	def f1(x,y):
# 		return x*y
# 	return reduce(f1,s)
# s=[1,2,3,4,5]
# print(prob(s))
# a='123.125'
# a=a.split('.')
# print(a)
# a=[1,2,3]
# a=a[::-1]
# print(a)
# def str2float(s):
# 	s0=s.split('.')
# 	s1=s0[0]
# 	s2=s0[1][::-1]
# 	dig={'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8 ,'9':9, '0':0}
# 	def char2int(ss):
# 		return dig[ss]
# 	def f1(x,y):
# 		return x*10+y
# 	def f2(x,y):
# 		return x*0.1+y
# 	return reduce(f1,map(char2int,s1)) +reduce(f2,map(char2int,s2))*0.1
# num='123.456'
# print(str2float(num))
# a=[123,456]
# a=a[::-1]
# print(a)
# dig={'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8 ,'9':9, '0':0}
# def char2int(ss):
# 	return dig[ss]
# print(list(map(char2int,['1', '2','3'])))
# def number(n):
# 	# num=[]
# 	# num=range(1,n,2)
# 	return range(1,n,2)
# print(list(number(10)))
# def odd_iter():
# 	n=1
# 	while True:
# 		n=n+2
# # 		yield n
# def not_divisible(n):
# 	return lambda x : x % n >0
# def primes():
# 	yield 2
# 	it=odd_iter()
# 	while True:
# 		n=next(it)
# 		yield n
# 		it = filter(not_divisible(n),it)
# for x in primes():
# 	if x<100:
# 		print(x)
# 	else:
# 		break
# def huishu(n):
# 	return lambda n: n==int(str(n)[::-1])
# def num():
# 	n=1
# 	while True:
# 		n=n+1
# 		yield n
# def f():
# 	a=num()
# 	while True:
# 		z=next(a)
# 		yield z
# 		a=filter(huishu(z),a)
# for i in f():
# 	if i<1000:
# 		print(i)
# 	else:
# 		break
# L=[('Bob',75), ('Adam',92), ('Lisa',88)]
# def fin(x):
# 	return x[1]
# print(sorted(L,key=fin))
# def f1():
# 	n=1
# 	while True:
# 		n=n+1
# 		yield n
# def f2(n):
# 	return lambda n: n==int(str(n)[::-1])
# def ff():
# 	yield 1
# 	num=f1()
# 	while True:
# 		n=next(num)
# 		yield n
# 		num=filter(f2(n),num)
# for i in ff():
# 	if i<1000:
# 		print(i)
# 	else:
# 		break
# def tri(line):
# 	L=[1]
# 	i=1
# 	while i < line:
# 		yield L
# 		L=[L[0]] + [L[n+1] + L[n] for n in range(len(L)-1)] + [L[-1]]
# 		i=i+1
# 	return L
# for x in tri(20):
# 	print(x)
# def f(line):
# 	L=[1]
# 	x=1
# 	while x < line:
# 		yield L
# 		L= [2*len(L)+1] + [L[n] + L[n+1] for n in range(len(L)-1)] + [2*len(L)+1]
# 		x=x+1
# 	return L
# for i in f(10):
# 	print(i)
# def creatcounter():
# 	def b():
# 		n=0
# 		while True:
# 			n+=1
# 			yield n
# 	i=b()
# 	def counter():
# 		return next(i)
# 	return counter
# f=creatcounter()
# print(f())
# L=list(filter(lambda n: n%2==0,range(1,20)))
# print(L)
# import sys
# print(sys.path)
# class Student(object):
# 	def __init__(self, name, score):
# 		self.name=name
# 		self.score=score
# 	def print_score(self):
# 		print("%s:%s" %(self.name, self.score))

# bart=Student('Bart Simpson', 59)
# lisa=Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()
# class Person(object):
# # 这里就是初始化你将要创建的实例的属性
#     def __init__(self,hight,weight,age):
#         self.hight = hight
#         self.weight = weight
#         self.age = age

# # 定义你将要创建的实例所有用的技能
#     def paoniu(self):
#         print('你拥有泡妞的技能')

#     def eat(self):
#         print('you can eat')

# # 开始创建实例
# zhangsan=Person(170,50,29)
# lisi = Person(175,100,30)

# # 你的实例开始使用它的技能
# zhangsan.paoniu()
# lisi.eat()
# class Student(object):
# 	def __init__ (self, name, score):
# 		self.name=name
# 		self.score=score
# 	def print_score(self):
# 		print("%s:%s" %(self.name, self.score))
# 	def get_grade(self):
# 		if self.score > 80:
# 			print("%s : %s is A" %(self.name, self.score))
# 		else:
# 			print("%s : %s is B"%(self.name, self.score))

# zhangsan=Student('zhangsan', 89)
# lisi=Student('lisi',79)
# zhangsan.print_score()
# zhangsan.get_grade()
# lisi.print_score()
# lisi.get_grade()
# class Student(object):
# 	def __init__ (self, name, gender):
# 		self.name=name
# 		self.__gender=gender
# 	def get_gender(self):
# 		return self.__gender
# 	def set_gender(self,gender):
# 		if gender not  in ("male", "female"):
# 			return ValueError
# 		else:
# 			self.__gender=gender
# 		# return self.__gender
# 	# def valid_gender(self,gender):
# 	# 	if self.__gender 
# zhangsan=Student('zhangsan','male')
# print(zhangsan.get_gender())
# print(zhangsan.set_gender('feale'))
# print(type(123))
# class Student(object):
# 	count=0
# 	def __init__ (self, name):
# 		self.name=name
# 		Student.count=Student.count+1
# a=Student('a')
# B=Student('b')
# C=Student('c')
# print(Student.count)
# class Student (object):
# 	__slots__=('name', 'score')
# 	pass
# s=Student()
# s.name='A'
# s.score=99
# print(s.name)
# print(s.score)
# class GraduteStudent(Student):
# 	pass
# g=GraduteStudent()
# g.grade='C'
# print(g.grade)
	# def get_score(self):
	# 	return self.score
	# def set_score(self,value):
	# 	if not isinstance(value, int):
	# 		raise ValueError('score must be an integer')
	# 	if value < 0 or value >100 :
	# 		raise ValueError('score must between 0~100')
	# 	self._score=value
# class Screen (object):
# 	@property
# 	def width(self):
# 		return self._width

# 	@width.setter
# 	def width (self, value):
# 		self._width=value

# 	@property
# 	def heigth(self):
# 		return self.__heigth
	
# 	@heigth.setter
# 	def heigth (self,  value):
# 		self._heigth=value

# 	@property
# 	def resolution(self):
# 		return self._width* self._heigth

# a=Screen()
# a.width=100
# a.heigth=200
# print(a.resolution)
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise

# bar()
# from functools import reduce

# def str2num(s):
# 	try:
# 		return int(s)
# 	except:
# 		return float(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)
# import unittest
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 60 and self.score < 80:
#             return 'B'
#         elif self.score >= 80 and self.score <= 100:
#             return 'A'
#         elif self.score >= 0 and self.score < 60:
#             return 'C'
#         else:
#             raise ValueError
# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()
#
# if __name__ == '__main__':
#     unittest.main()
# import   OS
# f=open('C:/Users/NANA/Desktop/test/test.txt','r')
# print(f.read())
# # f.read()
# f.close()
# try:
#     f=open('C:/Users/NANA/Desktop/test/test.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# with open('C:/Users/NANA/Desktop/test/test.txt','r') as f:
#     s=f.read()
#     print(s)
# import os
# print(os.name)
# print(os.environ)
# print(os.environ.)
# import pickle
# d=dict(name='bob',age=20,score=90)
# # print(pickle.dumps(d))
# f=open('dump.txt','wb')
# pickle.dump(d,f)
# f.close
# print(d)
# start='na'*4+'\n'
# print(start)
# print(start[::-1])
# # print(start)
# print(len(start))
# setup='a dog goes into a bar ...'
# print(setup.strip('.'))
# print(setup.capitalize())
# print(setup.title())
# print(setup.upper())
# print(setup.lower())
# print(setup.swapcase())
# min_sec=60
# hon_min=60
# seconds_per_hour=min_sec * hon_min
# print(seconds_per_hour)
# day_hour=24
# total_seconds=day_hour * seconds_per_hour
# print(total_seconds)
# print(list('cat'))
# a_tuple=('ready', 'fire', 'aim')
# print(list(a_tuple))
# print(set('bbbads'))
# years_list=list()
# years_list=[1994, 1995, 1996, 1997, 1998, 1999]
# print(years_list[3])
# print(years_list[-1])
# things=['mozzarella', 'cinderella', 'salmonella']
# print(things[0].upper())
# things[0]=things[0].upper()
# del things[-1]
# # things.remove('salmonella')
# print(things)
# surprise=['Groucho', 'Chico', 'Harpo']
# surprise[-1]=surprise[-1].lower()
# surprise[-1]=surprise[-1][::-1].capitalize()
# print(surprise)
# e2f={'dog':'chien', 'cat':'chat', 'walrus':'morse'}
# # print(e2f)
# # print(e2f['walrus'])
# f2e={}
# for english, french in e2f.items():
#     f2e[french]=english
# print(f2e)
# set(e2f.keys())
# life={
#     'animals':{
#         'cat':['henri', 'grumpy', 'lucy'],
#         'octopi':{},
#         'emus':{}
#
#     },
#     'plant':{},
#     'others':{}
#
# }
# print(list(life.keys()))
# print(life['animals'].keys())
# count=1
# while count<=5 :
#     print(count)
#     count+=1
# while True :
#     value=input('integer , please [q to quit]')
#     if value =='q':
#         break
#     number=int(value)
#     if number %2==0 :
#         continue
#     print(number, 'squared is', number*number)
# accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
# 'person': 'Col. Mustard'}
# for key, value in accusation.items():
#     print(key)
#     print(value)
# for i in accusation.items():
#     print(i)
# cheeses=[]
# found_one=False
# for cheese in cheeses:
#     found_one=True
#     print('This shop has some lovely', cheese)
#     break
# else:
#     print('This shop is not much of a cheese shop is, is it?')
# for i in range(1,27,3):
#     print(i)
# print(list(range(20,15,-2)))
# number_list=[number for number in range(1,20) if number %2==0]
# print(number_list)
# def agree():
#     return True
# print(agree())
# global animal
# animal = 'fruitbat'
# def change_and_print_global():
#     # global animal
#     animal = 'wombat'
#     print('inside change_and_print_global:', animal)
# change_and_print_global()
# print(animal)
# guess_me=7
# if guess_me < 7:
#     print('too low')
# elif guess_me==7:
#     print('just right')
# else:
#     print('too high')
#
# start=1
# while True:
#     if start< guess_me:
#         print('too low')
#     elif start==guess_me:
#         print('found it')
#         break
#     else:
#         print('opps')
#         break
#     start+=1
# list_1=[3,2,1,0]
# for i in list_1:
#     print(i)
# list=[number for number in range(10) if number%2==0]
# print(list)
# dict={key: key*key for key in range(10)}
# print(dict)
# set={number for number in range(10) if number%2!=0}
# print(set)
# for thing in ('Got %s' % number for number in range(10)):
#     print(thing)
# def good():
#     return ['Harry', 'Ron', 'Hermione']
# print(good())
# def get_odds(t):
#     i=0
#     while i < t:
#         if i%2!=0:
#             yield i
#         i+=1
# def get_odds(t):
#     for number in range(1,t,2):
#         yield number
# for n in get_odds(9):
#     print(n)
# for count, number in enumerate(get_odds(9),1):
#     if count==3:
#         print('The third number is', number)
#         break
# def test(func):
#     def new_func(*args, **kargs):
#         print('start')
#         result = func(*args, **kargs)
#         print('end')
#         return result
#     return new_func
# @test
# def greeting():
#     print('hello')
# greeting()
# titles = ['Creature of Habit', 'Crewel Fate']
# plots = ['A nun turns into a monster', 'A haunted yarn shop']
# dict_1=dict(zip(titles, plots))
# print(dict_1)
# class Duck():
#     def __init__(self,input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         return self.hidden_name
#     def set_name(self, input_name):
#         self.hidden_name = input_name
#     # name = property(get_name, set_name)
# A = Duck('B')
# print(A.hidden_name)
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#     @property
#     def diameter(self):
#         return 2 * self.radius
# c=Circle(5)
# print(c.diameter)
# class Thing():
#     pass
# # print(Thing)
# example=Thing()
# # print(example)
# class Thing2():
#     def __init__(self):
#         self.letter = 'abc'
# something=Thing2()
# print(something.letter)
#        letter='abc'
# print(Thing2.letter)
# class Element():
#     def __init__(self, name, symbol,number):
#         self.__name=name
#         self.__symbol=symbol
#         self.__number=number
#     # def dump(self):
#     #     print('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))
#         # print(self.symbol)
# # hydrogen=Element('Hydrogen', 'H', 1)
# # print(hydrogen.name)
# #     def getter(self):
# #         return (self.__name, self.__symbol, self.__number)
#     @property
#     def name(self):
#         return self.__name
# dict={'name':'Hydrogen', 'symbol':'H', 'number':1}
# hydrogen=Element(**dict)
# # print(hydrogen.getter())
# print(hydrogen.name)
# class Bear():
#     @property
#     def eats(self):
#         return 'berries'
# b=Bear()
# print(b.eats)
# n = 42
# f=7.03
# s='string cheese'
# # # print('%d %f %s'  %(n, f, s))
# # print('{2} {1} {0}'.format(n, f, s))
# # d = {'n': 42, 'f': 7.03, 's': 'string cheese'}
# # print('{0[f]} {0[s]} {0[n]} {1}'.format(d, 'other'))
# print('{2:<5.5s} {1:>5.2f} {0:<2d}'.format(n, f, s))
# print('{2:^5.5s} {1:^5.2f} {0:^2d}'.format(n, f, s))
# from io import StringIO
# f = StringIO('hello world\n I am lena\n !')
# # print(f.write('hello!!!'))
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip)
# print(f.getvalue())
# import re
# source='Young Frankenstein'
# m=re.search('Y', source)
# if m:
#     print(m.group())
# import re
# source = '''I wish I may, I wish I might Have a dish of fish tonight.'''
# print(re.findall('wish|fish',source))
# # if m:
#     print(m.group())
# import random
# print('猜数字！')
# mim = int(input('最小值：'))
# max = int(input('最大值：'))
# num = random.randint(mim, max)
# guess = "guess"
# i = 0
# while guess != num:
#     i += 1
#     guess = int(input("请输入你猜的数字："))
#     if guess == num:
#         print('congratulation！')
#     elif guess < num:
#         print('你的数猜小了！')
#     else:
#         print('你的数猜大了')
# print('你共猜了%d次'%i)

# import random
#
# rang1 = int(input("请设置本局游戏的最小值:"))
# rang2 = int(input("请设置本局游戏的最大值:"))
# num = random.randint(rang1, rang2)
# guess = "guess"
# print("数字猜谜游戏！")
# i = 0
# while guess != num:
#     i += 1
#     guess = int(input("请输入你猜的数字："))
#
#     if guess == num:
#         print("恭喜，你猜对了！")
#     elif guess < num:
#         print("你猜的数小了...")
#     else:
#         print("你猜的数大了...")
#
# print("你总共猜了%d" % i + "次", end='')




# -*- coding:utf-8 -*-
# import requests
# import json
# import re
# lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(191232) + '&lv=1&kv=1&tv=-1'
# lyric = requests.get(lrc_url)
# json_obj = lyric.text
# print(json_obj)
# j = json.loads(json_obj)     #将字符串转化为字典
# print(j)
# lrc = j['lrc']['lyric']
# print(lrc)
# pat = re.compile(r'\[.*\]')   #r 不用转义
# print(pat)
# lrc = re.sub(pat, "", lrc)
# print(lrc)
# lrc = lrc.strip()
# print(lrc)
# -*- coding:utf-8 -*-
# import requests
# import json
# import re
# from bs4 import BeautifulSoup
# singer_url = 'http://music.163.com/artist?id=' + str(6460)
# web_data = requests.get(singer_url)
# soup = BeautifulSoup(web_data.text, 'lxml')
# singer_name = soup.select("#artist-name")
# r = soup.find('ul', {'class': 'f-hide'}).find_all('a')
# r = (list(r))
# music_id_set=[]
# for each in r:
#     song_name = each.text  # print(each.text)
#     song_id = each.attrs["href"]
#     music_id_set.append(song_id[9:])
# print(music_id_set)

# def rev(x):
#     num = 0
#     num1 = x
#     if x < 0 or x%10 == 0:
#         return 0
#     else:
#         while x > num:
#             num = num*10 + x%10
#             x = x//10
#         return x == num or x == (num // 10)
# print(rev(121))


# def reverse(x):
#     """
#     :type x: int
#     :rtype: int
#     """
#     num = 0
#     if x == 0:
#         return 0
#     if x < 0:
#         x = -x
#         while x != 0:
#             num = num * 10 + x % 10
#             x = x / 10
#         num = -num
#     else:
#         while x != 0:
#             num = num * 10 + x % 10
#             x = x // 10
#
#     if num > pow(2, 31) - 1 or num < pow(-2, 31):
#         return 0
#     return num
#
# print(reverse(121))


# print(121%10)
# str = 'MCMXCIV'
# num = 0
# table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# i = 0
# pre_value = 0
# while i < len(str):
#     num = num + table.get(str[i])
#
#     if pre_value < table.get(str[i]):
#         num = num - 2 * pre_value
#     pre_value = table.get(str[i])
#     i += 1
# print(num)

# def strsss(strs):
#     if strs is None:
#         return ''
#     if len(strs) == 1:
#         return strs[0]
#     min_len = min([len(x) for x in strs])
#     end = 0
#     while end < min_len:
#         for i in range(1, len(strs)):
#             if strs[i][end] != strs[i - 1][end]:
#                 return strs[0][:end]
#         end += 1
#     return strs[0][:end]
#
# s = ["flower","flow","flight"]
# print (strsss(s))
# for x in range(1,7):
#     print(x)
# def fun(s):
#     if len(s) == 1:
#         return False
#     strs = [ '{}', '[]', '()']
# # for i in range(len(s)):
#     t = len(s)
#     i = 0
#
#     for e in strs:
#         # while i < len(s):
#         for i in range (len(s)):
#             j = i + 1
#             while j <= t:
#             # for j in range(i + 1, t):
#                 if s[i] == e[0] and s[j] == e[1]:
#                     i += 1
#                     t = j - 1
#                 else:
#                     j += 1
#
#                     # j -= 1
#                     # return True
#                 # else:
#                 #     return False
#                 # return False
# string = '({})'
# print(fun(string))
# a = {'a': '1', 'b': '2', 'c': '3'}
# for i in a:
#     print(i)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# import os
# class Solution:
#     def mergeTwoLists(l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         newnode = ListNode(0)
#         new = newnode
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#         p1 = l1
#         p2 = l2
#         while p1 is not None and p2 is not None:
#             if p1.val < p2.val:
#                 new.next = p1
#                 p1 = p1.next
#             else:
#                 new.next = p2
#                 p2 = p2.next
#             new = new.next
#         # else:
#         #     if p1 is None:
#         #         new.next = l2
#         #     if p2 is None:
#         #         new.next = l1
#
#         if p1 == None:
#             new.next = p2
#         elif p2 == None:
#             new.next = p1
#         return newnode.next
#
# #
# l1 = [1,2,4]
# l2 = [1,3,4]
# print(Solution.mergeTwoLists(l1, l2))
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         newnode = ListNode(0)
#         new = newnode
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#         p1 = l1
#         p2 = l2
#         while p1 is not None and p2 is not None:
#             if p1.val < p2.val:
#                 new.next = p1
#                 p1 = p1.next
#             else:
#                 new.next = p2
#                 p2 = p2.next
#             new = new.next
#         # else:
#         #     if p1 is None:
#         #         new.next = l2
#         #     if p2 is None:
#         #         new.next = l1
#
#         if p1 == None:
#             new.next = p2
#         elif p2 == None:
#             new.next = p1
#         return newnode.next
#
# s = Solution()
# print(s.mergeTwoLists(ListNode([1,2,4]),ListNode([1,3,4])))
# class Node(object):
#     def length(self):
#     # """返回链表的长度"""
#     # # 如果链表为空，返回长度0
#         if self.is_empty():
#             return 0
#         count = 1
#         cur = self._head
#         while cur.next != self._head:
#             count += 1
#             cur = cur.next
#         return count
# n = Node()
# first = ListNode(1)
# second = ListNode(2)
# third = ListNode(3)
# first.nest = second
# # second.next = third
# # # s = [1, 2]
# # print(n.length(first))
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         newnode = ListNode(0)
#         new = newnode
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#         p1 = l1
#         p2 = l2
#         while p1 is not None and p2 is not None:
#             if p1.val < p2.val:
#                 new.next = p1
#                 p1 = p1.next
#             else:
#                 new.next = p2
#                 p2 = p2.next
#             new = new.next
#         # else:
#         #     if p1 is None:
#         #         new.next = l2
#         #     if p2 is None:
#         #         new.next = l1
#
#         if p1 == None:
#             new.next = p2
#         elif p2 == None:
#             new.next = p1
#         return newnode.next
# s = Solution()
#
# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)
# l2 = ListNode(1)
# l2.next = ListNode(2)
# l2.next.next = ListNode(3)
#
# l = s.mergeTwoLists(l1,l2)
# while l is not None:
#     print(l.val)
#     l = l.next

# class Node(object):
#     """节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
#
# class SinCycLinkedlist(object):
#     """单向循环链表"""
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         """判断链表是否为空"""
#         return self._head == None
#
#     def length(self):
#         """返回链表的长度"""
#         # 如果链表为空，返回长度0
#         if self.is_empty():
#             return 0
#         count = 1
#         cur = self._head
#         print(cur.next)
#         # print(cur.next.next)
#         # print(cur.next.item)
#         print(self._head.item)
#         while cur.next != self._head:
#             count += 1
#             cur = cur.next
#         return count
#
#     def travel(self):
#         """遍历链表"""
#         if self.is_empty():
#             return
#         cur = self._head
#         print (cur.item,)
#         while cur.next != self._head:
#             cur = cur.next
#             print (cur.item,)
#         print ("")
#
#
#     def add(self, item):
#         """头部添加节点"""
#         node = Node(item)
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#         else:
#             #添加的节点指向_head
#             node.next = self._head
#             # 移到链表尾部，将尾部节点的next指向node
#             cur = self._head
#             while cur.next != self._head:
#                 cur = cur.next
#             cur.next = node
#             #_head指向添加node的
#             self._head = node
#
#     def append(self, item):
#         """尾部添加节点"""
#         node = Node(item)
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#         else:
#             # 移到链表尾部
#             cur = self._head
#             while cur.next != self._head:
#                 cur = cur.next
#             # 将尾节点指向node
#             cur.next = node
#             # 将node指向头节点_head
#             node.next = self._head
#
#     def insert(self, pos, item):
#         """在指定位置添加节点"""
#         if pos <= 0:
#             self.add(item)
#         elif pos > (self.length()-1):
#             self.append(item)
#         else:
#             node = Node(item)
#             cur = self._head
#             count = 0
#             # 移动到指定位置的前一个位置
#             while count < (pos-1):
#                 count += 1
#                 cur = cur.next
#             node.next = cur.next
#             cur.next = node
#
#     def remove(self, item):
#         """删除一个节点"""
#         # 若链表为空，则直接返回
#         if self.is_empty():
#             return
#         # 将cur指向头节点
#         cur = self._head
#         pre = None
#         # 若头节点的元素就是要查找的元素item
#         if cur.item == item:
#             # 如果链表不止一个节点
#             if cur.next != self._head:
#                 # 先找到尾节点，将尾节点的next指向第二个节点
#                 while cur.next != self._head:
#                     cur = cur.next
#                 # cur指向了尾节点
#                 cur.next = self._head.next
#                 self._head = self._head.next
#             else:
#                 # 链表只有一个节点
#                 self._head = None
#         else:
#             pre = self._head
#             # 第一个节点不是要删除的
#             while cur.next != self._head:
#                 # 找到了要删除的元素
#                 if cur.item == item:
#                     # 删除
#                     pre.next = cur.next
#                     return
#                 else:
#                     pre = cur
#                     cur = cur.next
#             # cur 指向尾节点
#             if cur.item == item:
#                 # 尾部删除
#                 pre.next = cur.next
#
#     def search(self, item):
#         """查找节点是否存在"""
#         if self.is_empty():
#             return False
#         cur = self._head
#         if cur.item == item:
#             return True
#         while cur.next != self._head:
#             cur = cur.next
#             if cur.item == item:
#                 return True
#         return False
#
# if __name__ == "__main__":
#     ll = SinCycLinkedlist()
#     ll.add(1)
#     ll.add(2)
#     ll.append(3)
#     ll.insert(2, 4)
#     ll.insert(4, 5)
#     ll.insert(0, 6)
#     print("length:",ll.length())
#     ll.travel()
#     print (ll.search(3))
#     print (ll.search(7))
#     ll.remove(1)
#     print ("length:",ll.length())
#     ll.travel()
# class Solution:
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return len(nums)
#         # i = 0
#         # while i < len(nums):
#         #     if nums[i] == val:
#         #         del nums[i]
#         #     else:
#         #         i += 1
#         # return len(nums)
#         j = 0
#         for i in range(0, len(nums)):
#             if nums[i] != val:
#                 nums[j] = nums[i]
#                 j += 1
#         # return j
#         return nums[:j]    # 取前j个元素
# class Solution:
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         if len(nums) == 0:
#             return len(nums)
#         i = 0
#         while i < len(nums):
#             if nums[i] == val:
#                 del nums[i]
#             else:
#                 i += 1
#         return len(nums)
# s = Solution()
# a = [1,2, 3, 4, 5, 3, 3]
# val = 3
# print(s.removeElement(a, val))
# str = [0,1,2,3,4,5,6,7,8,9]
# print(str[1:3])
# class Solution:
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if len(needle) > len(haystack) or len(needle) ==0:
#             return 0
#         i = 0
#         while i <= (len(haystack) - len(needle)):
#             if haystack[i: (i + len(needle))] == needle:
#                 print(haystack[i: (i + len(needle))])
#                 print(needle)
#
#                 return i
#                 break
#             else:
#                 i += 1
#         return -1
#
# s = Solution()
# print(s.strStr('mississippi','pi'))
# print()
# class Solution:
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if len(nums) == 0:
#             nums.insert(0, target)
#             return 0
#         if target < nums[0]:
#             nums.insert(0, target)
#             return 0
#         if target > nums[len(nums) - 1]:
#             nums.insert(len(nums), target)
#             return len(nums) - 1
#         i = 0
#         while i < len(nums):
#             if nums[i] < target:
#                 i += 1
#             elif target < nums[i]:
#                 nums.insert(i, target)
#                 return i
#                 # break
#             else :
#                 return i
#                 # break
# class Solution:
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         l = 0
#         r = len(nums)
#         while l < r:
#             mid = l + int((r - l)/2)
#             if nums[mid] < target:
#                 l = mid + 1
#             elif nums[mid] > target:
#                 r = mid
#             else:
#                 return mid
#         return r
# s = Solution()
# nums =[1,2,3,4,5]
# target = 0
# print(s.searchInsert(nums, target))
# s = '1'
# print(len(s[0]),s[0])
# s.insert(2)
# print(len(s[0]),s[0])
# # strs[][] = ''
# strs = ['1','1124']
# # strs[0] = 1
# print(strs[1][2])
# for k in range(1,30):
#     print (k)
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # dic = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        strs = ['1', '11']
        new_strs = ''
        # strs[0] = '1'
        # if str[n-1] == 1:
        #     return 1
        i = 0
        j = 1
        t = 0
        k=0
        # for k in range(1,31):
        while k < 30:
            for i in range(0,(len(strs[k])-1)):
                if strs[k][i] == strs[k][i+1]:
                    j += 1
                else:
                    new_strs[t] = j
                    new_strs[t+1] = strs[k][i]
                    t += 2
                    j = 1
                    strs.append(new_strs)
            k += 1
        return strs[n-1]
s = Solution()
print(s.countAndSay(4))