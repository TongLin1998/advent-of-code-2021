import statistics as stat
import math
import numpy as np
from numpy.lib.function_base import diff
import scipy.special

f = open("day7test.txt", "r")
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

forwardIndex = math.ceil(mean)
backwardIndex = math.floor(mean)
limitCounter = 0
totalCycle = 0

for i in range(mean):
  # print('=============================')
  # print('Iteration {}'.format(i + 1))
  # print('=============================')

  # forward
  if forwardIndex <= maxX:
    difference = np.absolute(crabs - forwardIndex)
    nonZeroDifference = np.asarray([sum(range(value + 1)) for value in difference])
    
    fuel = sum(nonZeroDifference)
    
    # print(crabs)
    # print(difference)
    # print(nonZeroDifference)
    # print(fuel)

    if fuel < leastFuel:
      limit = 0
      leastFuel = fuel

  else:
    continue

  # backward
  if backwardIndex >= minX:
    difference = np.absolute(crabs - backwardIndex)
    nonZeroDifference = np.asarray([sum(range(value + 1)) for value in difference])
    
    fuel = sum(nonZeroDifference)
    
    # print(crabs)
    # print(difference)
    # print(nonZeroDifference)
    # print(fuel)

    if fuel < leastFuel:
      limit = 0
      leastFuel = fuel

  else:
    continue

  if limitCounter == limit:
    totalCycle = i
    break
  
  if i == (mean - 1):
    totalCycle = i

  limitCounter += 1
  forwardIndex += 1
  backwardIndex -= 1
  # print()

print()
print('summary')
print(totalCycle + 1)
print(leastFuel)
