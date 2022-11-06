import time
import numpy as np


# =============================================================

def my_print(Q_Table):
    # hard-coded hack for this problem only
    rows = len(Q_Table);
    cols = len(Q_Table[0])
    print("       0      1      2      3      4      5\
      6      7      8      9      10     11     12\
     13     14     15     16     17     18     19     20     21     22     23     24     25     26     27\
     28     29     30     31     32     33     34     35     36     37     38     39     40     41     42\
     43     44     45     46     47     48     49")
    for i in range(rows):
        print("%d " % i, end="")
        if i < 50: print(" ", end="")
        for j in range(cols): print(" %6.2f" % Q_Table[i, j], end="")
        print("")
    print("")


def get_actions(s, Actions, no_states):
    # given a state s and a feasibility matrix F
    # get list of possible next states
    actions = []

    if s+10 < 50 and s+10 > -1 and Actions[s, s+10] == 1:
        actions.append(s+10)
    if s-10 < 50 and s-10 > -1 and Actions[s, s-10] == 1:
        actions.append(s-10)
    if s+1 < 50 and s-1 > -1 and Actions[s, s+1] == 1:
        actions.append(s+1)
    if s-1 < 50 and s-1 > -1 and Actions[s, s-1] == 1:
        actions.append(s-1)
    #print("State: ", s, " Actions: ", actions)
    # for j in range(no_states):
    #     if Actions[s, j] == 1:
    #         actions.append(j)
    #         #print("State: ", s, " Actions: ", actions)
    return actions


def get_random_new_state(current_state, Actions, no_states):
    # given a state s, pick a feasible next state
    actions = get_actions(current_state, Actions, no_states)
    new_state = actions[np.random.randint(0, len(actions))]
    #print("new state: ", new_state)
    return new_state




def train(Actions, Rewards, Q_Table, gamma, learning_rate, goal, no_states, max_epochs):
    # compute the Q matrix
    for i in range(0, max_epochs):
        current_state = 0

        while (True):
            new_state = get_random_new_state(current_state, Actions, no_states)
            new_new_s = get_actions(new_state, Actions, no_states)
            max_q = -1
            for j in range(len(new_new_s)):
                nn_s = new_new_s[j]
                q_value = Q_Table[new_state, nn_s]
                if q_value > max_q:
                    max_q = q_value
            # Q = [(1-a) * Q]  +  [a * (rt + (g * maxQ))]
            Q_Table[current_state][new_state] = ((1 - learning_rate) * Q_Table[current_state] \
                [new_state]) + (learning_rate * (Rewards[current_state][new_state] + \
                                         (gamma * max_q)))

            #result = list(map(sum, Q_Table))
            #print(i, j, sum(result))
            current_state = new_state
            if current_state == goal:
                #print("i: ", i, "current state: ", current_state, "goal: ", goal)
                break
    return i


def display_path(start, goal, Q_Table):
    # go to goal from start using Q
    current = start
    shortest_path = []
    shortest_path.append(current)
    count = 0
    flag = True
    while current != goal:
        next = np.argmax(Q_Table[current])
        if next in shortest_path:
            print("Unable to find the shortest path, try increasing the number of episodes\n")
            flag = False
            break
        else:
            shortest_path.append(next)
            current = next
            count+=1
    if flag == True:
        print("The shortest path through the maze is:\n")
        print(shortest_path, "\n")
        print("The shortest path takes", count, "moves!\n")



def main():
    start_time = time.time()
    print("\nInitialising the maze in memory\n")

    Actions = np.zeros(shape=[50, 50], dtype=int)
    Rewards = np.zeros(shape=[50, 50], dtype=float)
    Q_Table = np.zeros(shape=[50, 50], dtype=float)
    moves_one = [0,0,1,2,12,10,20,21,31,32,22,31,30,40,41,42,43,33,34,44,34,24,25,35,24,14,13,3,4,5,15,16,26,27,16,6,7,8,9,19,18,28,38,39,38,37,47,47,49]
    moves_two = [1,10,2,12,11,20,21,31,32,22,23,30,40,41,42,43,33,34,44,45,24,25,35,36,14,13,3,4,5,15,16,26,27,17,6,7,8,9,19,18,28,38,39,29,37,47,46,48,49]
    for i in range(len(moves_one)):
        Actions[moves_one[i], moves_two[i]] = 1
        Actions[moves_two[i], moves_one[i]] = 1
        Rewards[moves_one[i], moves_two[i]] = 0.1
        Rewards[moves_two[i], moves_one[i]] = 0.1
    Actions[48][49] = 1
    Rewards[48][49] = 10


    start = 0
    goal = 49
    no_states = 50  # number of states
    gamma = 0.5
    learning_rate = 0.5
    max_epochs = 10
    print("Training\n")
    train(Actions, Rewards, Q_Table, gamma, learning_rate, goal, no_states, max_epochs)
    display_path(start, goal, Q_Table)
    #my_print(Actions)



    end_time = time.time()
    print("Total elapsed time was", round(((end_time - start_time) * 1000), 2), "milliseconds!\n")


if __name__ == "__main__":
    main()
