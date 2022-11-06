import random
import string

import numpy as np
shape = (50, 4)
width = 10
height = 5
start = (0,0)
goal = (4,9)
alpha = 0.01
gamma = 0.9
epsilon = 0.25
Q_Table = np.zeros(shape)
Reward_Table = np.zeros(shape)
Reward = np.zeros(shape)
actions = {"down": 0,"up" : 1,"right" : 2,"left" : 3} #possible actions
states = {}
k = 0
for i in range(height):
    for j in range(width):
        states[(i,j)] = k
        k+=1

def main():

    #right
    Q_Table[[2,5,10,12,14,16,17,21,23,25,27,28,32,34,36,43,45,9,19,29,39,49], 2] = -1
    Reward_Table[[2, 5, 10, 12, 14, 16, 17, 21, 23, 25, 27, 28, 32, 34, 36, 43, 45, 9, 19, 29, 39, 49], 2] = -100
    #left
    Q_Table[[3,6,11,13,15,17,18,22,24,26,28,29,33,35,37,44,46,0,10,20,30,40], 3] = -1
    Reward_Table[[3, 6, 11, 13, 15, 17, 18, 22, 24, 26, 28, 29, 33, 35, 37, 44, 46, 0, 10, 20, 30, 40], 3] = -100
    #down
    Q_Table[[1,4,7,8,11,12,13,15,19,20,23,26,27,31,32,35,36,38,39,40,41,42,43,44,45,46,47,48,49], 0] = -1
    Reward_Table[[1, 4, 7, 8, 11, 12, 13, 15, 19, 20, 23, 26, 27, 31, 32, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
             49], 0] = -100
    #up
    Q_Table[[11, 14, 17, 18, 21, 22, 23, 25, 29, 30, 33, 36, 37, 41, 42, 45, 46, 48, 49, 0, 1, 2, 3, 4, 5, 6, 7, 8,
                  9], 1] = -1
    Reward_Table[[11,14,17,18,21,22,23,25,29,30,33,36,37,41,42,45,46,48,49,0,1,2,3,4,5,6,7,8,9], 1] = -100
    print(Q_Table, "\n\n")
    Reward_Table[len(Q_Table) - 1] = 100
    current_state = 0
    previous_state = 0
    current_path = []
    all_paths = []
    print("Initial Current State - ", current_state)
    current_path.append(current_state)
    #randomly select an index for the current state where the action != -1
    for j in range(20000):
        current_state = 0
        current_path = []
        current_path.append(current_state)
        while current_state != 49:
            while True:
                index = random.randint(0, 3)
                if (Q_Table[current_state, index]) != -1:
                    break
            previous_state = current_state
            if index == 0:
                current_state += 10
            elif index == 1:
                current_state += -10
            elif index == 2:
                current_state += 1
            elif index == 3:
                current_state += -1
            if current_state not in current_path:
                current_path.append(current_state)

        all_paths.append(current_path)
    print(len(all_paths))
    longest = max(all_paths, key=len)
    shortest = min(all_paths, key=len)
    print("Longest: ", len(longest), longest)
    print("Shortest: ", len(shortest), shortest)

    cs = 0

    for k in range(1):
        maxReward = np.argmax(Reward[cs])

    print("Max: ", maxReward)


if __name__ == '__main__':
    main()