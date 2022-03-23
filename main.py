import random

key = ""
for i in range(0,7): key += str(random.randint(0,1))

print(f"Key is {key}")
key = list(key)

string = input("String> ")

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

string = toBinary(string)

newstring = ""

for item in string:
  x = list(str(item))
  NEWINT = 0

  for j in x:
    currentVar = key[NEWINT]
    
    curr = int(j) ^ int(currentVar)
  
    NEWINT += 1
  
    newstring = newstring + str(curr)

print(newstring)