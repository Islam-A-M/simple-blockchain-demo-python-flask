def helper_function(args):
      for argument in args:
        print(argument)

def unlimited_arguments(*args, **keyword_aruments):
    print(args)
    helper_function(args)
   # print(keyword_aruments)
    for key,argument in keyword_aruments.items():
            helper_function(argument)

unlimited_arguments(*[1,2],3,4,5,Hello=[6,7,8])

