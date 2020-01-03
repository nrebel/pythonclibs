from ctypes import *
import my_functions_py as my_functions
import time

number = 10

so_file = "/home/pi/spiel/pylib/my_functions.so"
my_functions = CDLL(so_file)

print(type(my_functions))

start = time.time()
print ("python fibonacci recursive: ",my_functions.fib_rek(number))
end = time.time()
print("Time elapsed: ",end-start)

start = time.time()
print("python fibonacci iterative: ",my_functions.fib_it(number))
end = time.time()
print("Time elapsed: ",end-start)

start = time.time()
print("c lib call fibonacci recursice: ",my_functions.fib_rek(number))
end = time.time()
print("Time elapsed: ",end-start)

start = time.time()
print("c lib call fibonacci iterative: ",my_functions.fib_it(number))
end = time.time()
print("Time elapsed: ",end-start)
