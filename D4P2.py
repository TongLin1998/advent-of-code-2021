# Day 4 Part 2

import copy
from pprint import pprint

def findIndex(rows):
  for boardIndex, boardRows in enumerate(originalBoards):
    if rows == boardRows:
      return boardIndex

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

originalBoards = copy.deepcopy(boards)
bingoedBoard = []
end = False

for sequenceIndex, sequenceNum in enumerate(sequence):
  for boardNum, boardRows in enumerate(boards):
    for rowNum, row in enumerate(boardRows):
      for index, value in enumerate(row):
        if value == sequenceNum:
          bingo[boardNum][rowNum][index] = value
  
  if sequenceIndex >= 4:
    
    print('currentSeq = {}'.format(sequenceNum))

    indexToBePopped = []

    for bingoBoardNum, bingoBoardRows in enumerate(bingo):
      # pprint(bingoBoardRows)
      # check rows
      boardRow = [sum(row) for row in boards[bingoBoardNum]]
      bingoRow = [sum(row) for row in bingoBoardRows]
      
      boardColumn = [sum(col) for col in zip(*boards[bingoBoardNum])]
      bingoColumn = [sum(col) for col in zip(*bingoBoardRows)]

      # print('board sum')
      # print(boardColumn)
      # print(bingoColumn)
      # print('======================')

      
      for rowIndex, rowSum in enumerate(boardRow):
        if bingoRow[rowIndex] == rowSum:
          print('board {} bingo at {}th round with num {} and row {}'.format(bingoBoardNum, sequenceIndex, sequenceNum, rowIndex))
          if len(boards) == 1:
            lastWinner = boards[0]
            lastNum = sequenceNum
            end = True
            break
          # boardEnd = bingoBoardNum
          # print('bingo board num {}'.format(bingoBoardNum))
          indexToBePopped.append(bingoBoardNum)
          # print(indexToBePopped)

      for colIndex, colSum in enumerate(boardColumn):
        if bingoColumn[colIndex] == colSum:
          print('board {} bingo at {}th round with num {} and col {}'.format(bingoBoardNum, sequenceIndex, sequenceNum, colIndex))
          if len(boards) == 1:
            lastWinner = boards[0]
            lastNum = sequenceNum
            end = True
            break
          # print(boardEnd)

          indexToBePopped.append(bingoBoardNum)
          # print(indexToBePopped)
        # elif bingoColumn[rowIndex] == rowSum:
        #   print('board {} bingo at {}th round with num {} and col {}'.format(bingoBoardNum, sequenceIndex, sequenceNum, rowIndex))
        #   if len(boards) == 1:
        #     lastWinner = boards[0]
        #     lastNum = sequenceNum
        #     end = True
        #   # print(boardEnd)

        #   indexToBePopped.append(bingoBoardNum)
        #   print(indexToBePopped)

        if end:
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

    
    # print(indexToBePopped)
    if len(indexToBePopped):
      offset = 0
      print('to be popped {}'.format(indexToBePopped))
      for index in indexToBePopped:
        boards.pop(index - offset)
        bingo.pop(index - offset)
        print('popped {}'.format(index))
        offset += 1

      pprint(bingo)

  if end:
    break

#         if value == sequenceNum:
#           bingo[boardNum][rowNum][index] = value

print('==================')
print('ended')
print('==================')

pprint(originalBoards)

for boardIndex, boardRows in enumerate(originalBoards):
  if boardRows == lastWinner:
    lastWinnerBoardIndex = boardIndex
    break

winnerNum = lastNum
winnerBoard = originalBoards[lastWinnerBoardIndex]
winnerBingo = bingo[0]

pprint(winnerBingo)

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

