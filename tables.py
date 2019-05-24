#!/usr/bin/python3
class Table():
  n=int(input("Enter the number to print the tables for:"))
  for i in range(1,11):
      print(n,"x",i,"=",n*i)
Table()
