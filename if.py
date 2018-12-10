#!/usr/bin/python3
'''
age = int(input("Enter your age?"))

if age>=18:
        print("You are eligible to vote!!")
else:
        print("You are not eligible to vote!!")


'''

'''class Vote:
    age = int(input("enter your age"))
    if age >=18:
        print("you can go for vote")
    else:
        print("you can't go")



'''
class Vote:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def voting(self):
        if self.age>=18:
            print("you can go"+ name )
        else:
            print("you can't go")

age = int(input("enter your age"))
name = str(input("please enter your name"))
v1 = Vote(name, age)
v1.voting()
