# Day 3 Part 2

from collections import Counter

f = open("day3.txt", "r")
bits = [line.strip('\n') for line in f.readlines()]

# print(bits)

x = len(bits[0])
# y = len(bits)

o2 = ''
co2 = ''

# for O2
bitsO2 = list(bits)
i = 0
# for i in range(x):
while (len(bitsO2) > 1):
  
  # print('{} = {}'.format('position', i))
  yO2 = len(bitsO2)
  bitColumnsO2 = []

  for j in range(yO2):
    bitColumnsO2.append((bitsO2[j])[i])
  
  bitZeroCount = Counter(bitColumnsO2)['0']
  bitOneCount = Counter(bitColumnsO2)['1']
  # print('{} = {}'.format('bitZero', bitZeroCount))
  # print('{} = {}'.format('bitOne', bitOneCount))

  if (bitOneCount >= bitZeroCount):
    bitsO2 = [bitO2 for bitO2 in bitsO2 if bitO2[i] == '1']

  else:
    bitsO2 = [bitO2 for bitO2 in bitsO2 if bitO2[i] == '0']

  # print('{} = {}'.format('bitsO2', bitsO2))
  i += 1

  if (len(bitsO2) == 1):
    o2 = bitsO2[0]

# for CO2
bitsCO2 = list(bits)
i = 0
# for i in range(x):
while (len(bitsCO2) > 1):
  # print('{} = {}'.format('position', i))
  
  yCO2 = len(bitsCO2)
  bitColumnsCO2 = []

  for j in range(yCO2):
    bitColumnsCO2.append((bitsCO2[j])[i])
  
  bitZeroCount = Counter(bitColumnsCO2)['0']
  bitOneCount = Counter(bitColumnsCO2)['1']
  # print('{} = {}'.format('bitZero', bitZeroCount))
  # print('{} = {}'.format('bitOne', bitOneCount))

  if (bitZeroCount <= bitOneCount):
    bitsCO2 = [bitsCO2 for bitsCO2 in bitsCO2 if bitsCO2[i] == '0']

  else:
    bitsCO2 = [bitsCO2 for bitsCO2 in bitsCO2 if bitsCO2[i] == '1']

  i += 1
  # print('{} = {}'.format('bitsCO2', bitsCO2))
  
  if (len(bitsCO2) == 1):
    co2 = bitsCO2[0]
  
print('{} = {}'.format('o2', o2))
print('{} = {}'.format('co2', co2))

o2 = int((o2), 2)
co2 = int(co2, 2)

print('{} = {}'.format('o2', o2))
print('{} = {}'.format('co2', co2))
print('{} = {}'.format('multiply', o2 * co2))