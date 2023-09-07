# Hash Tables and Collision Resolution Techniques

import random

TABLE_SIZE = 1001

class HashTable(object):
    
    def __init__(self, size):
        self.size = size
        self.table = [None]*size
        
    def h1(self, x):
        return x % self.size # mod by self.size to ensure wrapping
    
    def h2(self, x):
        return 7 - (x % 7)
    
    def f(self, x, i):
        return i * self.h2(x)
    
    def linearProbe(self, x, i):
        return (self.h1(x) + i) % self.size
    
    def linearProbe(self, j):             
        return (j + 1) % self.size
    
    def quadraticProbe(self, x, i):
        return (self.h1(x) + (i*i)) % self.size
    
    def doubleHashProbe(self, x, i):
        return (self.h1(x) + self.f(x, i)) % self.size
    
    def insert(self, x, method="linear"):
        i = 0
        collisions = 0
        j = self.h1(x)
        # collision occurred
        while self.table[j] is not None and i < self.size - 1:  
            collisions += 1
            i += 1
            if method == "quadratic":
                j = self.quadraticProbe(x, i)
            elif method == "double hash":
                j = self.doubleHashProbe(x, i)
            else:
                j = self.linearProbe(x, i)
        # x can't be inserted (table is full or infinite loop occurred)
        if self.table[j] is not None:
            print(f"{x} could not be inserted")
        else:
            # put x in slot
            self.table[j] = x
        return collisions

def main():
    # create random sequence of integers
    print()
    print("generating random sequence of 10000 integers with values 1 to 10001...")
    print()
    randomSequence = [random.randint(1, TABLE_SIZE * 10) for _ in range(10000)]
    
    hashTable = HashTable(TABLE_SIZE)
    collisionCount = 0
    i = 0
    for i in range(500):
        collisionCount += hashTable.insert(randomSequence[i])
        i += 1
    print(f"linear probing collisions: {collisionCount}")
    print()
    
    # quadratic probing
    hashTable = HashTable(TABLE_SIZE) # reset table
    collisionCount = 0 # reset count
    i = 0
    for i in range(500):
        collisionCount += hashTable.insert(randomSequence[i], method="quadratic")
    print(f"quadratic probing collisions: {collisionCount}")
    print()
    
    # double hashing
    hashTable = HashTable(TABLE_SIZE) # reset table
    collisionCount = 0 # reset count
    i = 0
    for i in range(500):
        collisionCount += hashTable.insert(randomSequence[i], method="double hash")
    print(f"double hashing collisions: {collisionCount}")
    print()
    
if __name__ == '__main__':
    main()
    