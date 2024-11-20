import os
import sys

list1 =[]

def check ():
    k = int(input("input 0 to stop adding numbers: "))
    if k != 0:
        list1.append(k)
        check()
    else: 
        print("These are the results: ")
        
'''def sol ():
    list1.sort(reverse = True)
    y = list1[0] * list1[1] * list1[2]
    print(str(list1[0])+ " x " +str(list1[1])+ " x " +str(list1[2])+ " = " +str(y))
'''
print("\nEnter your numbers and we will calculate the product for the highest 3 values.")

check()
#sol()
list1copy = []
list1copy.extend(list1)
list2copy = []
list2copy.extend(list1)
print(list1copy)
sum = 0
for i in range (len(list1copy)) :
    for j in range (i+1, len(list1copy)) :
        if list1copy [i] > list1copy [j]:
            tmp = list1copy [i]
            list1copy [i] = list1copy [j]
            list1copy [j] = tmp

for i in range (len(list2copy)) :
    for j in range (i+1, len(list2copy)) :
        if list2copy [i] < list2copy [j]:
            tmp = list2copy [i]
            list2copy [i] = list2copy [j]
            list2copy [j] = tmp

for i in range (len(list1)) :
    sum = sum + list1[i]
print(list1)
print (list1copy)
print (list2copy)
print(sum)

