import math

value = 4 # it ia  value
print(math.floor(4.34)) # Here it is converted in integers
print(math.ceil(4.35)) # Here it is converted in rounds off

#numpy
print(math.sqrt(16)) 
print(math.pow(2, 3)) 
print(math.sin(math.pi/2)) 
print(math.cos(math.pi))   
print(math.log(10))        
print(math.exp(2))         

print(math.pi)       
print(math.e)


import random
# random modules
print(random.randint(1, 100))  # Random integer between 1 and 100.

random.seed(12)
print(random.randint(1, 100)) # always got the same output due to seed funvtion

items = [1, 2, 3, 4, 5]
random.shuffle(items) # Random shuffle of a sequence
print(items)

print(random.choice([1, 2, 3, 4, 5])) # Random choice from a sequence
print(random.uniform(1, 10)) # Random float from a uniform distribution