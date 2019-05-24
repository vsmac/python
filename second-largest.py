#!/usr/bin/python3 
class SecondLargest:
    def second(self):
        a = 0
        b = 0
        for i in list:
            if i > a:
               a = i
        print("value of a is", a )
        for i in list:
            if b > i  or b < a:
                b = i
        print("value of b is", b )
list = [int(i) for i in input().split()]
p1 = SecondLargest()
p1.second()
