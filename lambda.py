x = lambda a: a + 10;

print(x(10))


x1 = lambda a,b: b + a;

print(x1(10,20))


def fun1(n):
  return lambda a : a * n

lambdafun = fun1(2)

print(lambdafun(10))
