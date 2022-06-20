'''
    Creating a function for binary search algorithm using iterative method.
'''

def BinarySearch_iteration(list,key):
    first=0
    last=len(list)
    
    while first<=last:
        mid=(first+last)//2
        if list[mid-1]==key:
            return True
        elif list[mid-1]>key:
            last=mid
        else:
            first=mid+1
    return False

print(BinarySearch_iteration([1,2,3,4,5,6,7,8,9], 5))
print(BinarySearch_iteration([1,2,3,4,5,6,7,8,9], 15))


