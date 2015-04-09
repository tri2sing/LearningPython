# f = scope.f1() 
# f() works
# f = f1()
# f() does not work
# scope.f1()() works
# f1()() does not work

y, z = 1, 2

def f1():
	x = 99
	print (x)
	def f2 ():
		x = 88
		print (x)
	return f2

def all_global ():
	global u
	u = y + z
	print (u)

def maker(n):
	def action(k):
		return k**n
	return action

# f= maker(2)
# f(3)
# f (4)
# g = maker(3)
# g(3)
# f(3)

def tester(start):
	state = start
	def nested(label):
		print (label, state)
	return nested
# reference to enclosing scope variable
# t = tester (0)
# t('eggs')
# t('ham')


def tester1(start):
	state = start
	def nested1(label):
		nonlocal state
		print (label, state)
		state += 1
	return nested1
# update of enclosing scope variable
# t1 = tester1 (0)
# t1('egg')
# t1('ham')
# t1('cake')
# t2 = tester1 (7)
# t2('egg')
# t2('ham')
# t2('cake')
# t1('grits')

