class MinHeap:

    def __init__(self, size, data):
        self.maxSize = size
        self.size = 0
        # self.heap = [None] * size
        self.heap = [0] * size

    def parent(self, index):
        return index // 2

    def leftChild(self, index):
        return index * 2

    def rightChild(self, index):
        return index * 2 + 1

    def siftUp(self, index):
        while index > 1 and self.heap[self.parent(index) - 1] > self.heap[index - 1]:
            self.heap[index - 1] = self.heap[self.parent(index) - 1]
            self.heap[self.parent(index) - 1] = self.heap[index - 1]
            index = self.parent(index)

    def siftDown(self, index):
        maxIndex = index
        left = self.leftChild(index)
        if left <= self.size and self.heap[left - 1] < self.heap[maxIndex - 1]:
            maxIndex = left
        right = self.rightChild(index)
        if right <= self.size and self.heap[right - 1] < self.heap[maxIndex - 1]:
            maxIndex = right
        if index != maxIndex:
            self.heap[index - 1] = self.heap[maxIndex - 1]
            self.heap[maxIndex - 1] = self.heap[index - 1]
            self.siftDown(maxIndex)

    def heapify(self, arr):
        self.size = self.maxSize = len(arr)
        self.heap = arr.copy()
        for i in range(self.size // 2, 0, -1):
            self.siftDown(i)

    def heapSort(self):
        save = self.size
        while self.size > 1:
            self.heap[0] = self.heap[self.size - 1]
            self.heap[self.size - 1] = self.heap[0]
            self.size -= 1
            self.siftDown(1)
        self.size = save

    def empty(self):
        return self.size == 0

    def insert(self, dato):
        if self.size == self.maxSize:
            raise RuntimeError("Lleno")
        self.heap[self.size] = dato
        self.size += 1
        self.siftUp(self.size)

    def extractMin(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.siftDown(1)
        return result

    def getMin(self):
        return self.heap[0]

    def remove(self, index):
        self.heap[index - 1] = float('-inf')
        self.siftUp(index)
        self.extractMin()

    def changePriority(self, index, dato):
        oldp = self.heap[index - 1]
        self.heap[index - 1] = dato
        if dato < oldp:
            self.siftUp(index)
        else:
            self.siftDown(index)

    def display(self):
        for i in range(self.size):
            print(self.heap[i], end=" ")
        print()