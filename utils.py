"""
A collection of utilities for working with lists.
"""

"""
Finds the largest value in the list.
"""
def largest(lst):
    max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max

"""
Sorts the list according to the "natural order" of the values.
Sorts ascending if "asc" is True, and descending if it is False.
"""
def sort(lst, asc):
    for i in range(len(lst)):
        if asc:
            idx = findSmallest(lst, i)
        else:
            idx = findLargest(lst, i)
        swap(lst, i, idx)
    return lst

"""
Helper function to find the largest element in the list starting
at index "start"
"""
def findLargest(lst, start):
    max = lst[start]
    idx = start
    for i in range(start, len(lst)):
        if lst[i] > max:
            max = lst[i]
            idx = i
    return idx

"""
Helper function to find the smallest element in the list starting
at index "start"
"""
def findSmallest(lst, start):
    max = lst[start]
    idx = start
    for i in range(start, len(lst)):
        if lst[i] < max:
            max = lst[i]
            idx = i
    return idx

"""
Helper function to swap two values in a list
"""
def swap(lst, a, b):
    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp


"""
Function to determine whether a list contains a target value
using binary search
"""
def search(lst, target):
    low = 0
    high = len(lst) - 1
    found = False
    while high >= low and not found:
        mid = (high + low) // 2
        if (lst[mid] == target):
            found = True
        elif (lst[mid] > target):
            high = mid - 1
        elif (lst[mid] < target):
            low = mid + 1
    return found

"""
Some test cases for the sort and search functions
"""
def main():
    a = [5, 7, 1, 8, 3]
    print(largest(a))
    sort(a, True)
    print(a)
    print(search(a, 7))

if __name__ == "__main__":
  main()