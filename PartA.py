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

# list_a = [-16.915, 0.279, -35.794, 33.724, -43.779, -46.629, 14.696, 85.361, 38.644, -60.172]
# print(floats_high_to_low(list_a))

#Problem B:
"""Comparison function for a ascii min heap that preserves alphabetical order."""
def ascii_min_compare(a, b):
    a = a[0]
    b = b[0]
    if ((a.isupper()) and (b.islower())):
        return ord(a) < (ord(b) - 32)
    elif ((a.islower()) and (b.isupper())):
        return (ord(a) - 32) < ord(b)
    else :
        return a < b

def sort_string_alpha(string_list):
    sorted_names = []
    heapB = BinaryHeap(ascii_min_compare)
    heapB.build_heap(string_list)
    heapB.display()
    for nodes in range(heapB.size()):
        sorted_names.append(heapB.pop())
    return sorted_names

# string_list = ['Olivia', 'liam', 'Lepookie', 'Noah', 'ava', 'Ethan', 'Bron', 'Mason', 'isabella', 'James']
# print(sort_string_alpha(string_list))

#Problem C:
int_list = [23, 61, 00, 77, 96, 45, 38, 89, 12, 14]

