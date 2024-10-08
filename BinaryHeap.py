import math
import sys

class BinaryHeap:
    """A binary heap that depends on a compare function"""

    def __init__(self, compareFunction):
        """Constructor takes in a compare function (determines min / max heap)"""
        self.compareFunction = compareFunction
        self.heap = []

    def left(self, index):
        """Left node in a binary heap"""
        return 2*(index)+1

    def right(self, index):
        """Right node in a binary heap"""
        return 2*(index)+2

    def parent(self, index):
        """Parent node"""
        if index > 0:
            return (index+1)/2 - 1
        else:
            return -1

    def build_heap(self, list):
        """Builds a heap from a list"""
        self.heap = list
        for i in range(int(len(self.heap)/2-1), -1, -1):
            self.heapify(i)

    def size(self):
        """Returns the size of the heap."""
        return len(self.heap)

    def pop(self):
        """Pops the optimal element (min or max) and heapifies the full heap."""
        if (len(self.heap) > 0):
            top = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap.pop()
            self.heapify(0)
            return top
        else:
            return None
        
    def heapify(self, index):
        """Heapifies any subnode in the binary heap"""
        L = self.left(index)
        R = self.right(index)
        optimal = index
        if (L < len(self.heap) and self.compareFunction(self.heap[L], self.heap[index])):
            optimal = L
        if (R < len(self.heap) and self.compareFunction(self.heap[R], self.heap[optimal])):
            optimal = R
        if (optimal != index):
            tmp = self.heap[index]
            self.heap[index] = self.heap[optimal];
            self.heap[optimal] = tmp
            self.heapify(optimal)

    def display(self):
        """Display the heap for debug mode."""
        if (len(self.heap) == 0):
            return
        currentLevel = 0
        for i in range(0, len(self.heap)):
            level = int(math.log(i+1)/math.log(2))
            maxLevels = (math.log(len(self.heap))/math.log(2))
            spacing = ""
            for j in range(0, int(math.pow(2, maxLevels-level))):
                spacing = spacing + " "
            if (currentLevel < level):
                print("")
                currentLevel = level
            sys.stdout.write(spacing)
            sys.stdout.write(str(self.heap[i]))
        print("")



def max_compare(a, b):
    """Comparison function for a max heap."""
    return a > b

def min_compare(a, b):
    """Comparison function for a min heap."""
    return a < b


if __name__=="__main__":
    heap = BinaryHeap(max_compare)
    list = [8, 5, 12, 12, 15, 20, 8, 5, 18, 5]
    heap.build_heap(list)
    heap.display()
    