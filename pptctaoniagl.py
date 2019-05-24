#!/usr/bin/python

n=int(input("Enter the number of elements to be inserted: "))
l=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    l.append(elem)
avg=sum(l)/n
print("Average of elements in the list", round(avg,2))




