import re 

strings = []
nice = 0
naughty = 0

with open("Day5.txt") as file:
  for line in file:
    strings.append(line.strip())
  file.close()


for string in strings: 
  print(string) 
  valid = False
  i = 0
  while i < len(string)-1:
    test = string[i:i+2]
    print(test)
    if re.search(test, string[i+2:]):
      valid = True
      break
    i += 1
  i = 0
  if valid:
    valid = False
    while i < len(string)-2:
      #print(string[i]+' '+string[i+1]+' '+string[i+2])
      if (string[i] == string[i+2] and not string[i] == string[i+1]):
        valid = True
        break
      i += 1
    if valid:
      nice += 1
  

print(nice)
