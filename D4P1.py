# Day 4 Part 1

import copy
from pprint import pprint

f = open("day4.txt", "r")
lines = [line.strip('\n') for line in f.readlines()]

sequence = [int(line) for line in lines[0].split(',')]
rawBoards = lines[2 : ]

boards = []
# boardIndex = 0
tempList = []

for index, value in enumerate(rawBoards):
  if (len(value)):
    values = value.split(' ')
    
    while '' in values: 
      values.remove('')

    tempList.append([int(v) for v in values])

  else:
    boards.append(tempList)
    tempList = []

boards.append(tempList)

# initialBingo = [None, None, None, None, None]
initialBingo = [0, 0, 0, 0, 0]
multipliedInitialBingo = [copy.deepcopy(initialBingo) for i in range(5)]
bingo = [copy.deepcopy(multipliedInitialBingo) for i in range(len(boards))]

for sequenceIndex, sequenceNum in enumerate(sequence):
  for boardNum, boardRows in enumerate(boards):
    for rowNum, row in enumerate(boardRows):
      for index, value in enumerate(row):
        if value == sequenceNum:
          bingo[boardNum][rowNum][index] = value
  
  if sequenceIndex >= 4:
    end = False
    boardEnd = 0
    for bingoBoardNum, bingoBoardRows in enumerate(bingo):
      # check rows
      boardRow = [sum(row) for row in boards[bingoBoardNum]]
      bingoRow = [sum(row) for row in bingoBoardRows]
      
      boardColumn = [sum(col) for col in zip(*boards[bingoBoardNum])]
      bingoColumn = [sum(col) for col in zip(*bingoBoardRows)]
      
      for rowIndex, rowSum in enumerate(boardRow):
        if bingoRow[rowIndex] == rowSum:
          print('board {} bingo at {}th round with num {} and row {}'.format(bingoBoardNum, sequenceIndex, sequenceNum, rowIndex))
          end = True
          boardEnd = bingoBoardNum
          numEnd = sequenceNum
          # print(boardEnd)
          break

        elif bingoColumn[rowIndex] == rowSum:
          print('board {} bingo at {}th round with num {} and col {}'.format(bingoBoardNum, sequenceIndex, sequenceNum, rowIndex))
          end = True
          boardEnd = bingoBoardNum
          numEnd = sequenceNum
          # print(boardEnd)
          break
      

      # for colIndex, colSum in enumerate(boardColumn):
      #   if bingoColumn[colIndex] == colSum:
      #     print('board {} bingo at {}th round with num {} and col {}'.format(bingoBoardNum, sequenceIndex, sequenceNum, colIndex))
      #     end = True
      #     boardEnd = bingoBoardNum
      #     # print(boardEnd)
      #     break

      if end:
        break
    if end:
      break
#         if value == sequenceNum:
#           bingo[boardNum][rowNum][index] = value

winnerNum = numEnd
winnerBoard = boards[boardEnd]
winnerBingo = bingo[boardEnd]

total = 0

for rowIndex, row in enumerate(winnerBingo):
  for index, value in enumerate(row):
    if value == 0:
      total += winnerBoard[rowIndex][index]

# total = [sum(row) for row in winnerBingo]
# colSum = [sum(col) for col in zip(*winnerBingo)]

# total = rowSum + colSum
score = total * winnerNum

# pprint(bingo)

print(total)
print(score)