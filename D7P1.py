import statistics as stat
import math
import numpy as np

f = open("day7.txt", "r")
crabs = [int(crab) for crab in f.readline().split(',')]
crabs = np.asarray(crabs)
# print(crabs)

minX = min(crabs)
maxX = max(crabs)
medianX = int(stat.median(crabs))
mean = round(stat.mean(crabs))
limit = round(mean / 2)

# print(minX)
# print(maxX)
# print(mean)
# print(medianX)
# print(limit)

leastFuel = float("inf")
# print(stat.mean(crabs))

forwardIndex = math.ceil(medianX)
backwardIndex = math.floor(medianX)
limitCounter = 0
totalCycle = 0

for i in range(mean):
  # print('=============================')
  # print('Iteration {}'.format(i + 1))
  # print('=============================')

  # forward
  if forwardIndex <= maxX:
    difference = np.absolute(crabs - forwardIndex)
    fuel = sum(difference)
    
    # print(crabs)
    # print(difference)
    # print(fuel)

    if fuel < leastFuel:
      leastFuel = fuel

  else:
    continue

  # backward
  if backwardIndex >= minX:
    difference = np.absolute(crabs - backwardIndex)
    fuel = sum(difference)
    
    # print(crabs)
    # print(difference)
    # print(fuel)

    if fuel < leastFuel:
      leastFuel = fuel

  else:
    continue

  if limitCounter == limit:
    totalCycle = i
    break
  
  limitCounter += 1
  forwardIndex += 1
  backwardIndex -= 1
  # print()

print(totalCycle)
print(leastFuel)
