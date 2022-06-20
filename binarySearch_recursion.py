'''
    Defining function for binary search using recursion method.
'''
def BinarySearch_recurrsion(list,key):
    if not len(list):
        return False
    mid=len(list)//2
    if list[mid]==key:
        return True
    elif list[mid]>key:
        return BinarySearch_recurrsion(list[:mid], key)
    else:
        return BinarySearch_recurrsion(list[mid+1:], key)

print(BinarySearch_recurrsion([1,2,3,4,5,6,7,8,9], 13))
print(BinarySearch_recurrsion([1,2,3,4,5,6,7,8,9], 5))

