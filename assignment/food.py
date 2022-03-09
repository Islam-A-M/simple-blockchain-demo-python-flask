
# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).
class Food:
    def __init__(self,name,kind):
        self.name =name
        self.kind=kind
    
    def describe(self):
        print( 'name:{} , kind : {}'.format(self.name,self.kind))
    def __repr__(self):
        return str(self.__dict__)
banana= Food('banana','fruit')
banana.describe()
Carrots= Food('Carrots','vegetable')
Carrots.describe()

# 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.
# class Food:
#     name = ''
#     kind = ''
#     def __init__(self,name,kind):
#         self.name =name
#         self.kind=kind
#     @staticmethod
#     def describe(name,kind):
#         print( 'name:{} , kind : {}'.format(name,kind))
# Food.name='banana'
# Food.kind='fruits'
# Food.describe(Food.name,Food.kind)
# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.
class Meat(Food):
    def __init__(self, name):
        super().__init__(name,'Meat')
    def cook(self):
        print('Cooking')
        
class Fruit(Food):
   def __init__(self, name):
       super().__init__(name,'Fruit')
   def clean(self):
       print('cleaning')
       
banana = Fruit('banana')
banana.clean()
banana.describe()
pork = Meat('pork')
pork.cook()
pork.describe()
print(pork)
# 4) Overwrite a “dunder” method to be able to print your “Food” class.