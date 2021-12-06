# Day 1 Part 2

f = open("test1.txt", "r")
numbers = [int(line.strip('\n')) for line in f.readlines()]
windows = [sum(numbers[i : i + 3]) for i in range(len(numbers) - (len(numbers) % 3))]
# print(type(numbers))
print(windows)
largerThanPrevious = 0

for i in range(1, len(windows)):
  previous = windows[i - 1]
  current = windows[i]
  # nextNum = numbers[i + 1]
  # print('prev = ' + str(previous))
  # print('current = ' + str(current))
  # print('nextNum = ' + str(nextNum))
  if (i == 1):
    print(str(previous))

  if (current > previous):
    print(str(current) + '(increased)')
    largerThanPrevious += 1
  else:
    print(str(current))
    

# print('total increase = ' + str(largerThanPrevious))
print('{} = {}'.format('total increase', str(largerThanPrevious)))