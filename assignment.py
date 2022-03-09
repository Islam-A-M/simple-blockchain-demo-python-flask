import re
#1) Create a list of names and use a for loop to output the length of each name (len() ).
list_of_names=['Islam Ahmed','Ahmed','Max','n','N']
for name in list_of_names:
    print(name)
    #2) Add an if  check inside the loop to only output names longer than 5 characters.
    if len(name)>5:
        print(len(name))
    includes_n = re.search(r"n", name,flags=re.IGNORECASE)
    if  includes_n:
        print('includes n')
#4) Use a while  loop to empty the list of names (via pop() )
while len(list_of_names)>0:
    list_of_names.pop()
else:
    print('List poped')
    print(list_of_names)

