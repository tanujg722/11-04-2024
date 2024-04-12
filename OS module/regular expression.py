text= " my dog is great"
import re
pattern = "dog"
print(re.search(pattern,text))

pattern ="Tanuj"
print(re.search(pattern,text))

text2 = "My name is tanuj gupta and My age is 30"
pattern = 'My'
print(re.search(pattern,text2))