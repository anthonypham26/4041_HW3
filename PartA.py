from BinaryHeap import BinaryHeap, max_compare, min_compare

#Problem A:
def floats_high_to_low(float_list):
    sorted_floats = []
    heapA = BinaryHeap(max_compare)
    heapA.build_heap(float_list)
    heapA.display()
    for nodes in range(heapA.size()):
        sorted_floats.append(heapA.pop())
    return sorted_floats

list_a = [-16.915, 0.279, -35.794, 33.724, -43.779, -46.629, 14.696, 85.361, 38.644, -60.172]
print(floats_high_to_low(list_a))

sting_list = ['Olivia', 'Liam', 'Lepookie', 'Noah', 'Ava', 'Ethan', 'Bron', 'Mason', 'Isabella', 'James']

int_list = [23, 6, 0, 77, 99, 41, 31, 89, 12, 14]

