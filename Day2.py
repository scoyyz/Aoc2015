gifts = []
total = 0
ribbon = 0

with open("Day2.txt") as file:
  gifts = file.readlines()
  file.close()

for gift in gifts:
  x,y,z = gift.split('x')
  l = int(x)
  w = int(y)
  h = int(z)
  sides = [l,w,h]
  sides.sort()
  side1 = l*w 
  side2 = w*h 
  side3 = l*h 
  smallest = side1
  if side2 < smallest:
    smallest = side2
  if side3 < smallest:
    smallest = side3
  total += 2*side1+2*side2+2*side3+smallest
  ribbon += sides[0]*2 + sides[1]*2 + (l*w*h)

print(total)
print(ribbon)