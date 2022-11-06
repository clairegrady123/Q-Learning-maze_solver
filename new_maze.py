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

def main():


    #right
    Q_Table[[2,5,10,12,14,16,17,21,23,25,27,28,32,34,36,43,45,9,19,29,39,49], 2] = -1
    #Reward_Table[[2, 5, 10, 12, 14, 16, 17, 21, 23, 25, 27, 28, 32, 34, 36, 43, 45, 9, 19, 29, 39, 49], 2] = -100
    #left
    Q_Table[[3,6,11,13,15,17,18,22,24,26,28,29,33,35,37,44,46,0,10,20,30,40], 3] = -1
    #Reward_Table[[3, 6, 11, 13, 15, 17, 18, 22, 24, 26, 28, 29, 33, 35, 37, 44, 46, 0, 10, 20, 30, 40], 3] = -100
    #down
    Q_Table[[1,4,7,8,11,12,13,15,19,20,23,26,27,31,32,35,36,38,39,40,41,42,43,44,45,46,47,48,49], 0] = -1
    #Reward_Table[[1, 4, 7, 8, 11, 12, 13, 15, 19, 20, 23, 26, 27, 31, 32, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
             #49], 0] = -100
    #up
    Q_Table[[11, 14, 17, 18, 21, 22, 23, 25, 29, 30, 33, 36, 37, 41, 42, 45, 46, 48, 49, 0, 1, 2, 3, 4, 5, 6, 7, 8,
                  9], 1] = -1
    #Reward_Table[[11,14,17,18,21,22,23,25,29,30,33,36,37,41,42,45,46,48,49,0,1,2,3,4,5,6,7,8,9], 1] = -100
    print(Q_Table, "\n\n")
    #print("\n", type(Q_Table[3]))
    #Reward_Table[len(Q_Table) - 1] = 100
    current_state = 0
    previous_state = 0
    current_path = []
    all_paths = []
    print("Initial Current State - ", current_state)
    i = 0
    current_path.append(current_state)
    #print(Q_Table)
    #print(Reward_Table)
    #print(Reward)
    temp = 0
    #randomly select an index for the current state where the action != -1
    #for j in range(1000):
    current_state = 0
    current_path = []
    current_path.append(current_state)
    count = 0
    while current_state != 49:
        while True:
            index = random.randint(0, 3)
            print("Cs:", current_state, "index: ", index)
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
        #if current_state in current_path: #and current_state != 0:
            #current_path.append(current_state)
            # print("cs in current path: ", current_state)
            # while current_state in current_path and current_state != 0:
            #     previous = current_path.pop()
            #     prev_previous = current_path.pop()
            #     print("previous: ", previous, "prev-previous: ", prev_previous)
            # current_path.append(prev_previous)
            # if previous - prev_previous == 1:
            #     Q_Table[prev_previous][2] = -1
            #     print("Q1: ", Q_Table[prev_previous][2])
            #     break
            # elif prev_previous - previous == -1:
            #     Q_Table[prev_previous][3] = -1
            #     print("Q2: ", Q_Table[prev_previous][3])
            #     break
            # elif prev_previous - previous == 10:
            #     Q_Table[prev_previous][0] = -1
            #     print("Q3: ", Q_Table[prev_previous][0])
            #     break
            # elif prev_previous - previous == -10:
            #     Q_Table[prev_previous][1] = -1
            #     print("Q4: ", Q_Table[prev_previous][1])
            #     break
            # current_path = []
            # current_state = 0
        if current_state not in current_path:
        #elif current_state != 0 and current_state not in current_path:
            #Q[current_state, action] += alpha * (reward[current_pos[0], current_pos[1]] - Q[current_state, action])
            #Reward[previous_state][index] += alpha * (Reward_Table[current_state][index] - Reward[current_state][index])
            current_path.append(current_state)

        all_paths.append(current_path)
    longest = max(all_paths, key=len)
    shortest = min(all_paths, key=len)
    print("Longest: ", len(longest), longest)
    print("Shortest: ", len(shortest), shortest)
    #print(Q_Table)

    cs = 0

    for k in range(1):
        maxReward = np.argmax(Reward[cs])

    print("Max: ", maxReward)


if __name__ == '__main__':
    main()