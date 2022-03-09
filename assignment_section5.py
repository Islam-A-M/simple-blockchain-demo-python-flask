# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.


def normal_function(function):
    print(function(10))
    
# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.

normal_function(lambda arg: arg/2)
# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.     
def normal_function2(function,*arg):
     for x in arg:
         print(function(x))
normal_function2(lambda arg: arg/2,10,15,20)

# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.
def normal_function2(function,*arg):
     for x in arg:
         print('{:^20}'.format(function(x)))
normal_function2(lambda arg: arg/2,10,15,20)
