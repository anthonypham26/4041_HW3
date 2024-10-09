from BinaryHeap import BinaryHeap, max_compare, min_compare

class PriorityQueue(BinaryHeap):

    def insert(self, key):
        """Insert a new element into the heap"""
        self.heap.append(key)
        last_idx = self.size() - 1
        self.increase_key(last_idx, key) 

    def maximum(self):
        """Return the maximum (or minimum) element in the heap"""
        return self.heap[0]

    def increase_key(self, index, new_key):
        """Increases the key at a given index"""
        if new_key < self.heap[index]:
            raise ValueError("New key is smaller than current key.")
        self.heap[index] = new_key
        while index > 0 and self.compareFunction(self.heap[index], self.heap[self.parent(index)]):
            parent_idx = self.parent(index)
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index] #swap if True
            index = parent_idx #update the index of the new_key

if __name__ == '__main__':
    heap = PriorityQueue(max_compare)
    lst = [3, 70, 235, 81, 993, 423, 64, 0, 1946]
    heap.build_heap(lst)
    heap.display()

    print("A) ADDING 5 to the heap")
    heap.insert(5)  # Call insert with only the key value
    heap.display()
    print("A) ADDING 4041 to the heap")
    heap.insert(4041)
    heap.display()

    print("B) Popping off an item")
    extracted = []
    extracted.append(heap.pop())
    heap.display()
    print("B) Popping off 2nd item")
    extracted.append(heap.pop())
    heap.display()
    print("Printing out Extracted list:")
    print(extracted)

    print("C) Adding Low Priority: 87")
    heap.insert(87)
    heap.display()
    print("C) Adding Low Priority: 2")
    heap.insert(2)
    heap.display()

    print("D) Adding High Priority: 999")
    heap.insert(999)
    heap.display()
    print("D) Adding High Priority: 723")
    heap.insert(723)
    heap.display()
    
    print("E) Popping off an item")
    popped = []
    popped.append(heap.pop())
    heap.display()
    print("E) Popping off 2nd item")
    popped.append(heap.pop())
    heap.display()
    print("High Priority Removed First")
    print(popped)
    heap.display()





