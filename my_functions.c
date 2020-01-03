#include <stdio.h>

int square(int i) {
  return i * i;
}

long int fib_rek(int n) {
  if (n<2)
    return 1;
  return fib_rek(n-1) + fib_rek(n-2);
}

long int fib_it(int n) {
  if (n<2)
    return 1;
  int fib1 = 0;
  int fib2 = 1;
  int tmp=0;
  for (int i=1; i<=n; ++i) {
    tmp = fib1 + fib2;
    fib1 = fib2;
    fib2 = tmp;
  }
  return fib2;
}
