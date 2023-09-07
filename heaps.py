# Max Heap Implementation and Methods

import random
import time

class MaxHeap:
    def __init__(self, arr=None):
        if arr is None:
            self.heap = []
        else:
            self.heap = arr.copy()
            # heapify tree
            for i in range((len(self.heap)-2)//2, -1, -1): 
                self._heapifyDown(i)
    
    def parent(self, i):
        return (i-1)//2
    
    def leftChild(self, i):
        return (2*i) + 1
    
    def rightChild(self, i):
        return (2*i) + 2
    
    def _heapifyUp(self, i):
        parent = self.parent(i)
        # swap 
        while i != 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            # update parent and i 
            i = parent
            parent = self.parent(i)

    def _heapifyDown(self, i):
        left = self.leftChild(i)
        right = self.rightChild(i)
        # determine if node[i]'s left/right children are bigger than it (aka breaking heap property)
        while (left < len(self.heap) and self.heap[i] < self.heap[left]) or (right < len(self.heap) and self.heap[i] < self.heap[right]):
            # left is biggest if right ind is out of bounds or left val > right val
            biggest = left if (right >= len(self.heap) or self.heap[left] > self.heap[right]) else right
            self.heap[i], self.heap[biggest] = self.heap[biggest], self.heap[i] # swap i with bigger child
            # recalculate left/right with new val for i
            i = biggest
            left = self.leftChild(i)
            right = self.rightChild(i)

    def insert(self, element):
        self.heap.append(element) 
        self._heapifyUp(len(self.heap)-1) # heapify up from last ele

    def getMax(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap) == 0:
            return None
        maxval = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0] # swap first element (max) with last element in list
        self.heap.pop() # remove last ele
        self._heapifyDown(0) # heapify down to restore properties
        return maxval

    def printHeap(self):
        print(self.heap)
       
def getInsertTime(heap, nums):
    startTime = time.time()
    for i in range(len(nums)):
        heap.insert(nums[i])
    endTime = time.time()
    return endTime - startTime

def getBuildTime(nums):
    startTime = time.time()
    heap = MaxHeap(nums)
    endTime = time.time()
    return endTime - startTime

def main():
    print("Heap methods with heap size = 100000")
    n = 100000
    numbers = list(range(1, n+1))
    sortedNums = numbers.copy()
    reversedSortedNums = sortedNums[::-1]
    randomNumbers = numbers.copy()
    random.shuffle(randomNumbers)
    
    # Method 1: elements inserted into heap one at a time
    a = MaxHeap()
    b = MaxHeap()
    c = MaxHeap()

    time1 = getInsertTime(a, sortedNums)
    time2 = getInsertTime(b, reversedSortedNums)
    time3 = getInsertTime(c, randomNumbers)
    
    print()
    print("Method 1: inserting elements into max heap one at a time")
    print()
    print(f"Sorted numbers time: {time1:.4f}")
    print(f"Reversed sorted numbers time: {time2:.4f}")
    print(f"Random numbers time: {time3:.4f}")
    print()
    
    # Method 2: pass in all elements at once to create heap
    time1 = getBuildTime(sortedNums)
    time2 = getBuildTime(reversedSortedNums)
    time3 = getBuildTime(randomNumbers)
    
    print("Method 2: building max heap with all elements passed in at once")
    print()
    print(f"Sorted numbers time: {time1:.4f}")
    print(f"Reversed sorted numbers time: {time2:.4f}")
    print(f"Random numbers time: {time3:.4f}")
    print()

if __name__ == '__main__':
    main()