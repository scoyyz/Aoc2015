import re 

strings = []
nice = 0
naughty = 0

with open("Day5.txt") as file:
  for line in file:
    strings.append(line.strip())
  file.close()


for string in strings: 
  #print(string) 
  if re.search(r"(\w{2})\1", string):
    if re.search(r"(\w)\w\1", string):
      nice += 1

print(nice)
