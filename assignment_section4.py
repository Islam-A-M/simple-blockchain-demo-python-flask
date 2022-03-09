#1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
person=[{'name':'Islam','age':29,'hobbies':['Football','biker','coding']},{'name':'Ahmed','age':19,'hobbies':['coding','chess']}]
#2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
names = [el['name'] for el in person]
print(names)
#3) Use a list comprehension to check whether all persons are older than 20.
print(all([el['age']>20 for el in person]))
#4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
person_copy = [el.copy() for el in person]
for count,el in  enumerate(person):
    for key,value in el.items() :
        if type(value)==list or set:
            person_copy[count][key]=el[key][:]
        if type(value)==dict:
            person_copy[count][key]=el[key].copy()
        


person_copy[0]['name']='soso'
person_copy[0]['hobbies'][0]=1

print(person_copy)
print('person_copy')

print(person)

#5) Unpack the persons of the original list into different variables and output these variables.
p1,p2 = person
print(p1)
print(p2)