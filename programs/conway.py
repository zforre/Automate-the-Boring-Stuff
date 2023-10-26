# conways game of life

import random, time, copy

WIDTH = 60
HEIGHT = 20

# create list for cells
nextCells = []

for x in range(WIDTH):
    column = [] # creates new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # add living cell
        else:
            column.append(' ') # add dead cell
    nextCells.append(column) # nextCells is a list of column lists

while True: # main program loop
    print('\n\n\n\n\n') # separate each step with a new line
    currentCells = copy.deepcopy(nextCells)

    #print currentCells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # prints the # or ' '
        print() # new line at end of row

    # calculate next steps cells based on current steps cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighboring coordinates
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # top left is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # top is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # top right is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # left is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # right is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom left is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # bottom is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # bootom right is alive

            # set cell based on rules of conways game of life
            if currentCells[x][y] == '#' and(numNeighbors == 2 or numNeighbors == 3):
                # living cells wth 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cells with 3 neighbors become alive
                nextCells[x][y] = '#'
            else:
                # everything else dies
                nextCells[x][y] = ' '
    time.sleep(1) # add a second pause to reduce flicker
