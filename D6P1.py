f = open("day6.txt", "r")
# initial = [line.strip(',') for line in f.readlines()]
initial = f.readline()
# print('Initial State: \t\t {}'.format(initial))

fish = [int(i) for i in initial.split(',')]

length = 80 - 1
for i in range(length):
  fishNum = len(fish)
  
  fish = [(f - 1) for f in fish]
  # print('After \t {} day(s): \t {}'.format(i + 1, ','.join(str(f) for f in fish)))

  newFish = 0
  for fishIndex, fishCount in enumerate(fish):
    # print('fish index {}'.format(fishIndex))
    # print('fish count {}'.format(fishCount))
    if fishCount == 0:
      fish[fishIndex] = 7
      newFish += 1


  for i in range(newFish):
    fish.append(9)

print(len(fish))

