"""
Created on Thu Apr 26 16:43:21 2018 @author: kartini
"""
import numpy as np
import random
Soal = np.loadtxt('DataTugasML3.txt')

Result = []
for i, reward in enumerate(Soal):
    for j, item in enumerate(reward):
        UP= 0
        RIGHT= 0
        DOWN= 0
        LEFT= 0
        if (i != 0): UP = Soal[i-1][j]
        if (i != len(Soal) - 1): DOWN = Soal[i+1][j]
        if (j != 0): LEFT = Soal[i][j-1]
        if (j != len(Soal) -1 ): RIGHT = Soal[i][j+1]
        Result.append([UP, RIGHT, DOWN, LEFT])

PossibleMovement = []
for i, x in enumerate(Result):
    tmp = []
    for j, z in enumerate(x):
        if (z != 0):
            tmp.append(j)
    PossibleMovement.append(tmp)
    
Q = []
for i, reward in enumerate(Soal):
    for j, item in enumerate(reward):
          Q.append([0,0,0,0])

def nextState(CurrentState, Action):
    row = 0
    col = 0
    while (CurrentState > 9):
        row = row + 1      
        CurrentState = CurrentState - 10

    col = CurrentState    
    if (Action == 0): row = row - 1
    if (Action == 1): col = col + 1
    if (Action == 2): row = row + 1        
    if (Action == 3): col = col - 1        
    
    result = col    
    while (row != 0):
        result += 10
        row = row - 1        
    return result

log = []
GAMMA = 1
episode = 1000
goalState = 9

for i in range(episode):
    state = random.randint(0,99)
    while (state != goalState):
        index = random.randint(0, len(PossibleMovement[state]) - 1)
        actionIndex = PossibleMovement[state][index]
        actionValue = Result[state][actionIndex]

        next_state = nextState(state, actionIndex)        
        notZeroArray = [x for x in Q[next_state] if x != 0 == 0]        
        value_next_state = notZeroArray
        
        if (value_next_state == []): value_next_state = 0
        
        QValue = actionValue + (GAMMA * np.amax(value_next_state))
        Q[state][actionIndex] = QValue
        
        state = next_state
        log.append([state, actionIndex])

currentState = 90
log2 = []
score = 0
while (currentState != goalState):
    max = -9999
    for i, item in enumerate(Q[currentState]):
        if (item > max and item != 0): max = item

    actionIndex = Q[currentState].index(max)
    score += Q[currentState][actionIndex]
    next_state = nextState(currentState, actionIndex)
    log2.append([currentState, actionIndex, score])
    currentState = next_state
print(currentState, 'You are arrived!')