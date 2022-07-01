import heapq

class MinHeap:
    def __init__(self):
        self.data = []
    
    def heapify(self, i):
        """
        method that maintains heap property.
        """
        c1, c2 = self.left_child(i), self.right_child(i) 
        if i >= len(self.data):
            return
        minIndex = -1
        if c1 < len(self.data) and self.data[c1] < self.data[i]:
            minIndex = c1
            self.data[i] = self.data[c1]
        if c2 < len(self.data) and self.data[c2] < self.data[i]:
            self.data[i] = self.data[c2]
            minIndex = c2
        if minIndex != -1:
            self.heapify(minIndex)

    def insert(self, val):
        """
        Insert val in heap
        """
        # insert and do a down to up heapify

    def left_child(self, i):
        return 2 *i + 1

    def right_child(self, i):
        return 2 *i + 2
    
    def parent(self, i):
        return i // 2

    def exists(self, val):
        """
        returns true if val exists in heap, else false
        """
        return val in self.data
    
    def pop(self, val):
        """
        Deletes min value from the heap.
        """
        if not self.data:
            return
        
        

    def createHeap(self, lst):
        """
        Takes a list of integers and creates a min heap.
        (overwrites existing heap)
        """
        self.data = lst
        for i in range(len(lst)):
            self.heapify(i)

# Ad Hoc testing
# if __name__ == "__main__":
#     lst = [5, 1, 4, 7, 8, 2, 10, 3, 12]
#     heap = MinHeap()
#     heap_c = heapq.heapify(lst)
#     heap.createHeap(lst)
#     print(heap.data)
#     # Compare heaps
#     for _ in range(len(heap_c)):
#         assert heap_c.heappop() == heap.pop()

