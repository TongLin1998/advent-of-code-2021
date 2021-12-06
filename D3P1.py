# Day 3 Part 1

from collections import Counter

f = open("day3.txt", "r")
bits = [line.strip('\n') for line in f.readlines()]

# print(bits)

x = len(bits[0])
y = len(bits)

mostCommonBit = ''
leastCommonBit = ''

for i in range(x):
  bitColumns = []
  for j in range(y):
    # print((bits[i])[j])
    bitColumns.append((bits[j])[i])
  
  bitZeroCount = Counter(bitColumns)['0']
  bitOneCount = Counter(bitColumns)['1']

  if (bitZeroCount > bitOneCount):  
    mostCommonBit += '0'
    leastCommonBit += '1'

  else:
    mostCommonBit += '1'
    leastCommonBit += '0'


# print('{} = {}'.format('most common bit', mostCommonBit))
# print('{} = {}'.format('least common bit', leastCommonBit))

mostCommonBit = int(mostCommonBit, 2)
leastCommonBit = int(leastCommonBit, 2)

print('{} = {}'.format('most common bit', mostCommonBit))
print('{} = {}'.format('least common bit', leastCommonBit))
print('{} = {}'.format('multiply', mostCommonBit * leastCommonBit))
