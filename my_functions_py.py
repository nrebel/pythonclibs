def fib_it(n):
  if n<2:
    return 1
  fib1 = 0
  fib2 = 1
  tmp = 0
  for i in range(1,n+1):
    tmp = fib1 + fib2
    fib1 = fib2
    fib2 = tmp
  return fib2

def fib_rek(n):
  if n<2:
    return 1
  return fib_rek(n-1) + fib_rek(n-2)
