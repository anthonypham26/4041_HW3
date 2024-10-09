from BinaryHeap import BinaryHeap, max_compare, min_compare

#Problem A:
def floats_high_to_low(float_list):
    sorted_floats = []
    heapA = BinaryHeap(max_compare)
    heapA.build_heap(float_list)
    heapA.display()
    while heapA.size() > 0:
        sorted_floats.append(heapA.pop())
    return sorted_floats


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
    while heapB.size() > 0:
        sorted_names.append(heapB.pop())
    return sorted_names


#Problem C:
def secondDigit_min_compare(a, b):
    a = int(str(abs(a))[1])
    b = int(str(abs(b))[1])
    return a < b

def secondDigit_low_to_high(int_list):
    sorted_ints = []
    heapC = BinaryHeap(secondDigit_min_compare)
    heapC.build_heap(int_list)
    heapC.display()
    while heapC.size() > 0:
        sorted_ints.append(heapC.pop())
    return sorted_ints

if __name__ == '__main__':
    list_a = [-16.915, 0.279, -35.794, 33.724, -43.779, -46.629, 14.696, 85.361, 38.644, -60.172]
    print(floats_high_to_low(list_a))

    list_b = ['Olivia', 'liam', 'Lepookie', 'Noah', 'ava', 'Ethan', 'Bron', 'Mason', 'isabella', 'James']
    print(sort_string_alpha(list_b))

    list_c = [231, 613, 12, -277, 96, -145, 38, 898, 125, 14]
    print(secondDigit_low_to_high(list_c))
