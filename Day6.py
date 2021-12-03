import re

lights = {}
x = 0
y = 0
instructions = []

with open("Day6.txt") as file:
  instructions = file.readlines()
  file.close()

###Build light array dictionary with all lights off "0"
while x < 1000:
  while y < 1000:
    coords = str(x)+','+str(y)
    lights[coords] = 0
    y += 1
  y = 0
  x += 1

for line in instructions:
  regex = re.search(r"(turn|toggle)( [a-z]*| )(.\d*,\d*)[a-z\s]*(\d+,\d+)",line)
  start = regex[3].split(',')
  startX = int(start[0].strip())
  startY = int(start[1].strip())
  end = regex[4].split(',')
  endX = int(end[0].strip())
  endY = int(end[1].strip())
  x = startX
  y = startY
  if regex[1] == 'turn':
    while x <= endX:
      while y <= endY:
        coords = str(x)+','+str(y)
        if regex[2].strip() == "on":
          lights[coords] += 1
        else:
          if lights[coords] > 0:
            lights[coords] -= 1
        y += 1
      x += 1
      y = startY
  else:
    while x <= endX:
      while y <= endY:
        coords = str(x)+','+str(y)
        lights[coords] += 2
        y += 1
      x += 1
      y = startY

sum = 0
for key in lights:
  sum += lights[key]
print(sum)