def outer_function():
    global a
    a = 20

    def inner_function():
        
        a = 30
        print('ai =', a)

    inner_function()
    print('a2 =', a)


a = 10
outer_function()
print('a3 =', a)