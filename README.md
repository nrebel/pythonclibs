# pythonclibs
Example of calling c functions from shared objects in python

This small example shows, how to call c-function from shared librarie in python.
This repo contains a _my_functions.c_ file, which includes two functions - an iterative and a recursive way to calculate the n-th 
fibonacci number.
Furthermore the same two functions are implemented in Python in _my_functions_py.py_

To create a share object, we need to link the .c file via:

```bash
$ cc -fPIC -shared -o my_functions.so my_functions.c
```

which create the shared object file _my_functions.so_

In the _call_c.py_ python script we call all four versions of the fibonacci function, i.e. iterative and recursive implemented in 
C respective in Python and for each function call the elapsed time is displayed.

Pretty simple example.

**Remark:**

The python module containing the implementations of the two functions must not have the same name as the shared object file has. Otherwise python tries to import the .so-file instead of the python module.
