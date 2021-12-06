# Day 2 Part 1

f = open("day2.txt", "r")
commands = [line.strip('\n').split(' ') for line in f.readlines()]
# print(commands)

horizontal = 0
depth = 0

for command in commands:
  magnitude = int(command[1])

  if (command[0] == 'forward'):
    horizontal += magnitude
  else:
    if (command[0] == 'up'):
      depth -= magnitude
    else:
      depth += magnitude

print('{} = {}'.format('horizontal', horizontal))
print('{} = {}'.format('depth', depth))
print('{} = {}'.format('multiply', horizontal * depth))