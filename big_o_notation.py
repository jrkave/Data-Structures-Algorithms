# Big O Notation

import time

def runtime(func, n):
    # Get time
    startTime = time.time()
    # Call function
    func(n)
    # Get time again
    endTime = time.time()
    # Return elapsed time
    return endTime - startTime

# O(N)
def funcA(n):
    total = 0                  
    for i in range(n):         
        total += 1           

# O(N^2)
def funcB(n):
    total = 0                  
    for i in range(n):      
        for j in range(n):     
            total += 1        

# O(N^2)
def funcC(n):
    total = 0                 
    for i in range(n):         
        for j in range(i):     
            total += 1         

# O(N^2)
def funcD(n):
    total = 0                   
    for i in range(n):         
        for j in range(i):      
            if (j % 2 == 0):  
                total += 1 


### Function Unit Testing ###

# Test Function A
print("Function A: ")
print(f"N = 100 | Runtime =", runtime(funcA, 100))
print(f"N = 1000 | Runtime =", runtime(funcA, 1000))
print(f"N = 10000: | Runtime =", runtime(funcA, 10000))
print()

# Test Function B
print("Function B: ")
print(f"N = 100: | Runtime =", runtime(funcB, 100))
print(f"N = 1000: | Runtime =", runtime(funcB, 1000))
print(f"N = 10000: | Runtime =", runtime(funcB, 10000))
print()

# Test Function C
print("Function C: ")
print(f"N = 100: | Runtime =", runtime(funcC, 100))
print(f"N = 1000: | Runtime =", runtime(funcC, 1000))
print(f"N = 10000: | Runtime =", runtime(funcC, 10000))
print()

# Test Function D
print("Function D: ")
print(f"N = 100: | Runtime =", runtime(funcD, 100))
print(f"N = 1000: | Runtime =", runtime(funcD, 1000))
print(f"N = 10000: | Runtime =", runtime(funcD, 10000))
print()

