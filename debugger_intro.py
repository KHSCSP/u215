# this function has no errors
# we'll use this to become familiar with the debugger tool
# TODO add breakpoint, run with debugger
def prob1():
    num1 = 5
    num2 = 10
    ans = num1+num2
    ans = ans + 3
    ans = ans/2
    print(ans)

# this function does have an error
# let's analyze with the debugger
def prob2():
    num1 = 0
    num2 = 5
    num3 = 10
    ans = num2+num3
    ans = ans/num1
    print(ans)


# this function also has an error
def prob3():
    my_list = []
    num = 5
    for i in range(num):
        if my_list[i] > 0:
            print("positive")
        else:
            print("negative")    

# prob1()
prob2()
# prob3()
