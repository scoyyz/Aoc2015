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
  valid = False #setting test value
  i = 0
  while i < len(string)-1: #iterate through string
    test = string[i:i+2] #sets test to equal a substring starting at index i and ending at index i+2
    print(test)
    if re.search(test, string[i+2:]): #searches for an instance of pattern "test" in the remainder of the string starting after index i+2
      valid = True #if the regex search is successful, set valid to true
      break
    i += 1
  i = 0
  if valid: #confirming that first test passed
    valid = False #resetting valid test to make sure both tests pass
    while i < len(string)-2: #interate through string
      #print(string[i]+' '+string[i+1]+' '+string[i+2])
      if (string[i] == string[i+2] and not string[i] == string[i+1]): #test if index i equals index i+2, while also not equaling i+1
        valid = True
        break
      i += 1
    if valid:
      nice += 1
  

print(nice)
