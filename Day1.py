floor = 0
instructions = ""
basement_visited = False

with open("Day1.txt") as input:
  instructions = input.readline()
  input.close()

i = 0
while i < len(instructions):
  if instructions[i] == '(':
    floor += 1
  else:
    floor -= 1
  if not basement_visited and floor < 0:
    print(i+1)
    basement_visited = True
  i += 1

print(floor)
