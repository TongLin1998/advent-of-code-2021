# Day 2 Part 2

f = open("day2.txt", "r")
commands = [line.strip('\n').split(' ') for line in f.readlines()]
# print(commands)

horizontal = 0
depth = 0
aim = 0

for command in commands:
  magnitude = int(command[1])

  if (command[0] == 'forward'):
    horizontal += magnitude
    depth += (magnitude * aim)
  else:
    if (command[0] == 'up'):
      aim -= magnitude
    else:
      aim += magnitude

print('{} = {}'.format('horizontal', horizontal))
print('{} = {}'.format('depth', depth))
print('{} = {}'.format('multiply', horizontal * depth))