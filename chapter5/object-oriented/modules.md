### Modules

Modules are reusable code for use across other scripts. Modules are single files in either .py, .pyc or .pyo format.

### Module Structure

```py
divisor_count_to_find = 500

def triangle_number(n):
    return n*(n+1)/2
    
def divisors(tn):
    counter = 0
    n_sqrt = int(pow(tn, 0.5))
    for i in range(1, n_sqrt + 1):
        if tn%i == 0:
            counter += 2
    if n_sqrt * n_sqrt == tn:
        counter -= 1
    return counter
    
def start():
    start_number = 1
    div_numbers = 0
    while (div_numbers < divisor_count_to_find):
        tn = triangle_number(start_number)
        div_numbers = divisors(tn)
        start_number += 1
    print(div_numbers)
    print(tn)
    
if __name__ == '__main__':
    start()
```

### Using Modules

```py
import triangle
triangle.start()
triangle.triangle_number(10)
triangle.divisors(10)
triangle.divisor_count_to_find = 100

triangle.start()
# 576 76576500.0 112 73920.0
```



