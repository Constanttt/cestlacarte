import random
import matplotlib.pyplot as plt

rows = 30
cols = 30
emptyMap = [[0 for x in range(rows)] for y in range(cols)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def addPositions(posA, posB):
    result = [0, 0]
    for i in range(len(posA)):
            result[i] = posA[i] + posB[i]
    return result;

def invertPosition(pos):
    result = [0, 0]
    for i in range(len(pos)):
            result[i] = pos[i] * -1
    return result;

def generateOneLayer(value, maxTurns, maxLength):
    global rows, cols, emptyMap, directions
    
    lastDirection = [0, 0]
    randomDirection = []
    position = [round(rows/2), round(cols/2)]
    
    for i in range(0, maxTurns):
        randomDirection = directions[random.randint(0, len(directions) - 1)]
        randomLength = random.randint(1, maxLength)
        if randomDirection == invertPosition(lastDirection):
            randomDirection = invertPosition(randomDirection)
        lastDirection = randomDirection
        for j in range(0, randomLength):
            if(not((randomDirection[0] == -1 and position[0] == 0) or (randomDirection[0] == 1 and position[0] == cols - 1) or (randomDirection[1] == -1 and position[1] == 0) or (randomDirection[1] == 1 and position[1] == rows - 1))):
                emptyMap[position[0]][position[1]] = value
                position = addPositions(position, randomDirection)

for i in range(0, rows):
    for j in range(0, cols):
        emptyMap[i][j] = 0

generateOneLayer(1, 300, 30)
generateOneLayer(2, 200, 25)
generateOneLayer(3, 100, 20)
generateOneLayer(4, 50, 15)

file = open("map.csv", "w+")
for i in range(0, rows):
    for j in range(0, cols):
        file.write(str(emptyMap[i][j]) + ", ")
    file.write("\n")
file.close()

plt.imshow(emptyMap)
plt.savefig('map.jpeg')
