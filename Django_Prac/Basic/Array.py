from array import array

##Taking input in python
a = input("YOUR TEXT :- ")
print(a)

##Declaring an array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, 9):
    # print(arr[i])  ## To print in new line everytime
    print(arr[i], end=" ")  ## tp print in only one line

## Can be printed just my the name call , as in java
num_array = list()
num = int(input("Enter how many elements you want :- "))
print('Enter numbers in array: ')

for i in range(0, num):
    n = input("num :")
    num_array.append(int(n))
print('ARRAY: ', num_array)

## INT
##Input take and  print using a loop
arr = []
size = int(input("SIZE PLEASE :- "))
for i in range(size):
    x = int(input())
    arr.append(int)

for i in range(0, 9):
    print(arr[i], end=" ")
