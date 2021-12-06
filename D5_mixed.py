import copy
from pprint import pprint
from collections import Counter

# store input start -> end
# loop
  # calc difference (end - start)
  # determine whether go x or y
  # if x
    # start from x1, add difference until x2
  # if y
    # start from y1, add difference until y2
# check tiles with overlap
# get total overlap

f = open("day5.txt", "r")
lines = [line.strip('\n') for line in f.readlines()]
commands = [command.split(' -> ') for command in lines]
# split = [[c for c in coord.split(',')] for coord in commands]
# pprint(commands)

stringCommands = [[c.split(',') for c in command] for command in commands]
# print(stringCommands)
intCommands = [[[int(a) for a in s] for s in string] for string in stringCommands]

#         X
# ------------------> 
# [[[0, 9], [5, 9]],  |
#  [[8, 0], [0, 8]],  |
#  [[9, 4], [3, 4]],  |
#  [[2, 2], [2, 1]],  |
#  [[7, 0], [7, 4]],  | Y
#  [[6, 4], [2, 0]],  |
#  [[0, 9], [2, 9]],  |
#  [[3, 4], [1, 4]],  |
#  [[0, 0], [8, 8]],  |
#  [[5, 5], [8, 2]]]  V

distance = []
xLargest = 0
yLargest = 0

for coords in intCommands:
  x1 = coords[0][0]
  x2 = coords[1][0]
  y1 = coords[0][1]
  y2 = coords[1][1]
  xDiff = (x2 - x1)
  yDiff = (y2 - y1)
  distance.append([xDiff, yDiff])

  if x2 > x1:
    if x2 > xLargest:
      xLargest = x2
  else:
    if x1 > xLargest:
      xLargest = x1

  if y2 > y1:
    if y2 > yLargest:
      yLargest = y2
  else:
    if y1 > yLargest:
      yLargest = y1

# print(distance)
emptyList = [0]
coordMap = [emptyList * (yLargest + 1) for i in range(xLargest + 1)]
# pprint(coordMap)
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for commandIndex, commands in enumerate(intCommands):
  x1 = commands[0][0]
  x2 = commands[1][0]
  y1 = commands[0][1]
  y2 = commands[1][1]
  xDiff = (x2 - x1)
  yDiff = (y2 - y1)
  direction = ''

  if xDiff == 0:
    direction = 'y'
  elif yDiff == 0:
    direction = 'x'
  else:
    direction = 'xy'
  
  # print(direction)
  # print('start {}, {}'.format(x1, y1))
  # print('end {}, {}'.format(x2, y2))
  # print('diff {}, {}'.format(xDiff, yDiff))

  if direction == 'x':
    for i in range(abs(xDiff) + 1):
      if xDiff > 0:
        coordMap[y1][x1 + i] += 1
      else:
        coordMap[y1][x1 - i] += 1

  elif direction == 'y':
    for i in range(abs(yDiff) + 1):
      if yDiff > 0:
        coordMap[y1 + i][x1] += 1
      else:
        coordMap[y1 - i][x1] += 1

  else:
    for i in range(abs(xDiff) + 1):
      if xDiff > 0 and yDiff > 0:
        # print('{},{}'.format(y1+i, x1+i))
        coordMap[y1 + i][x1 + i] += 1
      elif xDiff > 0 and yDiff < 0:
        # print('{},{}'.format(y1-i, x1+i))
        coordMap[y1 - i][x1 + i] += 1
      elif xDiff < 0 and yDiff > 0:
        # print('{},{}'.format(y1+i, x1-i))
        coordMap[y1 + i][x1 - i] += 1
      else:
        # print('{},{}'.format(y1-i, x1-i))
        coordMap[y1 - i][x1 - i] += 1
      
      # pprint(coordMap)

  # print(direction)
    
  # pprint(coordMap)
# pprint(coordMap)
# [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#  [0, 1, 1, 2, 1, 1, 1, 2, 1, 1],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [2, 2, 2, 1, 1, 1, 0, 0, 0, 0]]
flattenedCoord = [value for coord in coordMap for value in coord]
# print(flattenedCoord)

count = Counter(flattenedCoord)
print(count)
# print(count[])

overlap = 0

for c in count:
  if c > 1:
    overlap += count[c]

print(overlap)