# Day 1 Part 1

f = open("test1.txt", "r")
numbers = [int(line.strip('\n')) for line in f.readlines()]
print(type(numbers))
# print(numbers)
largerThanPrevious = 0

for i in range(1, len(numbers)):
  previous = numbers[i - 1]
  current = numbers[i]
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
    

print(largerThanPrevious)