# -*- coding: utf-8 -*-
"""iotlabtest1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bw19L5nPfe8aCpAK2b8mkVUxK8KXoWbQ
"""

#Question no 1
li = [10, 21,3, 4, 45, 66, 93]
for num in li:
    if num % 2 != 0:
        print(num, end=" ")

#Question no 2
li = [1, 2,3, 4, 5, 6,7,8,9,10]
sum = 0
for num in li:
    sum += num
print(sum)

#Question no 3
def r_li(li):
    left = 0
    right = len(li)-1
    while (left < right):
        t = li[left]
        li[left] = li[right]
        li[right] = t
        left += 1
        right -= 1
    return li
 
li = [1, 2,3, 4, 5, 6,7,8,9,10]
print(r_li(li))

li = [1, 2,3, 4, 5, 6,7,8,9,10]
li.reverse()
print(li)

#Question no 4
def two_largest(inlist):
    largest = 0
    second_largest = 0
    for item in inlist:
        if item > largest:
            second_largest = largest
            largest = item
        elif largest > item > second_largest:
            second_largest = item
    return largest, second_largest
if __name__ == "__main__":
    inlist = [6,8,5,1, 2, 3]
    print(two_largest(inlist))

#Question no 5
def two_largest(inlist):
    largest = 0
    s_largest = 0
    for item in inlist:
        if item > largest:
            s_largest = largest
            largest = item
        elif largest > item > s_largest:
            s_largest = item
    return  s_largest
if __name__ == "__main__":
    inlist = [6,8,5,1, 2, 3]
    print(two_largest(inlist))

#question no 6

def r_li(li):
    left = 0
    right = len(li)-1
    while (left < right):
        t = li[left]
        li[left] = li[right]
        li[right] = t
        left += 1
        right -= 1
    return li
li=["b","a","f","c"]
li.sort()
r_li(li)

print(li)

#question no 7
string="heloworldhelo"
a=[]
for el in string:
    if el not in a:
        a.append(el)
for i in range(len(a)):
    print(a[i],end="")

#question no 8
a=input("enter the character")
if (a=="A"or a=="a"or a=="E"or a=="e"or a=="I"or a=="i"or a=="O"or a=="o"or a=="U"or a=="u"):
  print("given character is voval : ",a)
else:
  print("given character is consonant : ",a)

#question no 9
a=int(input("enter the number :> "))
sum=1
for i in range (1,a+1):
  sum=sum*i

print(sum)

#question no 10

li1 = [1, 4, 5, 6, 5]
li2 = [3, 5, 7, 2,6,4,6,7]

for i in li2 :
    li1.append(i)
li1.sort()
print (str(li1))