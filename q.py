import random
import string

import numpy as np
shape = (50, 4)
width = 50
height = 4
start = (0,0)
goal = (4,9)

Q_Table = np.zeros(shape)
Reward = np.full((width, height), -1)
Reward[[width-1], 0:4] = 100
actions = {"down": 0,"up" : 1,"right" : 2,"left" : 3} #possible actions
states = {}
k = 0
for i in range(height):
    for j in range(width):
        states[(i,j)] = k
        k+=1

def main():

    #for i in range(50):
        #Q_Table[[i], 4] = i
    #right
    Reward[[2,5,10,12,14,16,17,21,23,25,27,28,32,34,36,43,45,9,19,29,39], 2] = -100
    #left
    Reward[[3,6,11,13,15,17,18,22,24,26,28,29,33,35,37,44,46,0,10,20,30,40], 3] = -100
    #down
    Reward[[1,4,7,8,11,12,13,15,19,20,23,26,27,31,32,35,36,38,39,40,41,42,43,44,45,46,47,48], 0] = -100
    #up
    Reward[[11,14,17,18,21,22,23,25,29,30,33,36,37,41,42,45,46,48,0,1,2,3,4,5,6,7,8,9], 1] = -100

    current_state = [0]
    previous_state = [0]
    current_path = []
    all_paths = []
    print("Initial Current State - ", current_state)
    i = 0
    current_path.append(current_state)
    print(Reward)
    print(Q_Table)
    #randomly select an index for the current state where the action != -1
    #for j in range(100):
    current_state = 0
    current_path = []
    i = 0
    current_path.append(current_state)
    while current_state <= 49:
        while True:
            index = random.randint(0, 3)
            print(index, current_state)
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
        if current_state in current_path and current_state == previous_state + 10 or current_state == previous_state - 10 or current_state == previous_state + 1 or current_state == previous_state - 1:
            Reward[previous_state][index] += -0.2
            current_path.append(current_state)
        elif current_state not in current_path:
            Reward[previous_state][index] += -0.04
            current_path.append(current_state)
        i+=1
    all_paths.append(current_path)
    print(len(all_paths))
    longest = max(all_paths, key=len)
    shortest = min(all_paths, key=len)
    print("Longest: ", len(longest), longest)
    print("Shortest: ", len(shortest), shortest)
    print(Q_Table)
    print(Reward)
    # cs = 0
    #
    # print(cs)
    # #print(Q_Table)
    # reward_list = []
    # for k in range(3):
    #     if (Q_Table[cs, k]) != -1:
    #         index2 = Q_Table[cs, k]
    #         print(index2)
    #         ps = cs
    #         if index2 == 0:
    #             reward_list.append(k)
    #             #cs += 10
    #         elif index2 == 1:
    #             reward_list.append(k)
    #             #cs += -10
    #         elif index2 == 2:
    #             reward_list.append(k)
    #             #cs += 1
    #         elif index2 == 3:
    #             reward_list.append(k)
    #             #cs += -1
    #
    # print("reward_list", reward_list)
    # biggest_reward = -100000
    # if (Reward[cs].any()) != 0 and Reward[cs].any() > biggest_reward:
    #     biggest_reward = Reward[cs].any()
    # print("biggest_reward", biggest_reward)


if __name__ == '__main__':
    main()