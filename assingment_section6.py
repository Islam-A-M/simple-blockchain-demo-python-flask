# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random

def random_number():
    return str(random.random())+ str(random.randint(1, 11))
print(random_number())
# 2) Use the datetime library together with the random number to generate a random, unique value.
from datetime import datetime
def millieseconds():
    dt_obj = datetime.now()
    millisec = dt_obj.timestamp() * 1000
    print(dt_obj)
    return millisec
print(str(millieseconds())+str(random_number()))