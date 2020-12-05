directions = []
homes = {}
case = {'<':[-1,0],'>':[1,0],'v':[0,-1],'^':[0,1]}
visited = 1



with open("Day3.txt") as input:
  for line in input:
    for char in line:
      directions.append(char)
  input.close()
print(directions)
Sx = 0
Sy = 0
Rx = 0
Ry = 0
mod = [0,0]
homes['0,0'] = 2
turn = 0
for stop in directions:
  mod = case[stop]
  if turn == 0:
    Sx += mod[0]
    Sy += mod[1]
    x,y = Sx,Sy 
  else:
    Rx += mod[0]
    Ry += mod[1]
    x,y = Rx,Ry
  if (str(x)+','+str(y)) not in homes.keys():
    homes[str(x)+','+str(y)] = 0
    visited += 1
  homes[str(x)+','+str(y)] += 1
  turn = (turn + 1) % 2

print(visited)