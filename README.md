Author: Claire Grady
Version: 1.0
Date: 22nd August 2022

Compiling Instructions (see CL information below):
python3 cgrady3.py

Command Line Arguments:
usage: cgrady3.py [-h] [--episodes EPISODES] [--gamma GAMMA] [--learning_rate LEARNING_RATE]
    Options to Change the Hyper Parameters
    optional arguments:
    -h, --help            show this help message and exit
    --episodes EPISODES   Integer value for number of episodes
    --gamma GAMMA         Floating point number for value of gamma
    --learning_rate LEARNING_RATE
                          Floating point number for value of learning_rate
Default Values: 'episodes': 100, 'gamma': 0.3, 'learning_rate': 0.5

Author: Claire Grady
Version: 1.0
Program: Uses a form of Q-Learning to find the shortest path through a maze
Algorithm: The algorithm trains for a certain number of episodes (default is 100). During
training, a random new state is chosen from a list of possible actions from the previous state.
It then looks up the Q values for all possible actions from the new state and stores the
highest value as max_q. This max_q value as well as the learning_rate, gamma(discount factor),
current Q and Reward values for that state action pair are used in the formula to compute the
new Q_value and insert it into the Q_Table. This formula is based on the Bellman equation.
When the training is complete, the shortest path found can be extracted by selecting the
action associated with the highest value in the Q_Table for the current state and continuing
this process until the goal state is reached (assuming the shortest path was found).
