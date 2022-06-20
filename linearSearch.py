'''Defining a function which take two arguments
    1. List
    2. key(which is the object that has to be searched from the list) 
'''


def LinearSearch(list, key):
    
    for i in range(len(list)):
        print(list[i])
        if list[i]==key:
            return i
    return None


'''
    Defining funtion in order to obtain the index of the 
    searched object(if found) in a better way
'''
def verify(idx):
    if idx is not None:
        return (f'The index of the searched number is '+str(idx))
    else:
        return False

'''
    Writing loop in case a user wants to search multiple times inside multiple arrays
'''
f='y'
while(f=='y'):
    arr=[]
    arr_length=int(input('Enter the length of list you want to define '))
    arr=list(map(str,input("elements of array:- ").strip().split()))
    key=input("Enter the element you want to search for ")
    k=LinearSearch(arr, key)
    print(verify(k))
    f=input("Do you want to continue? (y/n) ")