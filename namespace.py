def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('ai =', a)

    inner_function()
    print('ai2 =', a)


a = 10
outer_function()
print('ai3 =', a)