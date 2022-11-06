import math
import re
import time
import numpy as np
import argparse
import tkinter
from tkinter import *

#print Q_Table in a readable format
def my_print(Q_Table):
    rows = len(Q_Table);
    cols = len(Q_Table[0])
    print("       0      1      2      3      4      5      6      7      8      9      10     11     12\
     13     14     15     16     17     18     19     20     21     22     23     24     25     26     27\
     28     29     30     31     32     33     34     35     36     37     38     39     40     41     42\
     43     44     45     46     47     48     49")
    for i in range(rows):
        print("%d " % i, end="")
        if i < 50: print(" ", end="")
        for j in range(cols): print(" %6.2f" % Q_Table[i, j], end="")
        print("")
    print("")

#create a list for all possible actions from a state that is passed in as an parameter
def get_actions(s):
    actions = []
    if s+10 < 50 and s+10 > -1:
        actions.append(s+10)
    if s-10 < 50 and s-10 > -1:
        actions.append(s-10)
    if s+1 < 50 and s+1 > -1 and ((s+1) % 10) != 0: #mod 10 because row length is 10
        actions.append(s+1)
    if s-1 < 50 and s-1 > -1 and (s % 10) != 0:
        actions.append(s-1)
    return actions

#choose a random action from the list of possible actions
def get_random_new_state(current_state):
    actions = get_actions(current_state)
    new_state = actions[np.random.randint(0, len(actions))]
    return new_state

#training function that chooses a random action from a list of possible actions for the current state.
def train(Rewards, Q_Table, gamma, learning_rate, goal, episodes):
    percentage = episodes//4
    percentage_const = 25
    training_path = []
    for i in range(0, episodes):
        current_state = 0
        training_path.append(current_state)
        while (True):
            #randomnly select a new state from list of possible actions for the current state
            new_state = get_random_new_state(current_state)
            #get a list of possible actions from the new state
            new_new_s = get_actions(new_state)
            #set max_q equal to negative one
            max_q = -1
            for j in range(len(new_new_s)):
                #iterates through each possible action
                nn_s = new_new_s[j]
                #find the associated q_value for each state action pair
                q_value = Q_Table[new_state, nn_s]
                #if q_value is greater than the current max_q(maximum q_value for all possible actions from new state
                #assign the q_value as the max_q
                if q_value > max_q:
                    max_q = q_value
            #Q_learning algorithm that computes the new Q_value for the state action pair (current_state to new_state)
            #This algorithm is based on the Bellman equation
            Q_Table[current_state][new_state] = ((1 - learning_rate) * Q_Table[current_state] \
                [new_state]) + (learning_rate * (Rewards[current_state][new_state] + \
                                         (gamma * max_q)))
            #assign the new state to the current state
            current_state = new_state
            #append the current state to the training path in order to display training visualisation
            training_path.append(current_state)
            #when goal is reached break from episode
            if current_state == goal:
                break
        #display the percentage of training completed
        if percentage == i:
            print(percentage_const, "percent of the training is complete!\n")
            percentage += episodes//4
            percentage_const += 25
    if episodes % 4 == 0:
        print("100 percent of the training is complete!\n")
    #return the training path
    return training_path
#Check to see if shortest path could not be found by checking if current state has already been visited
#If so, display message about increasing number of episodes, otherwise display the shortest path
def display_path(start, goal, Q_Table):
    current = start
    shortest_path = []
    shortest_path.append(current)
    count = 0
    flag = True
    while current != goal:
        next = np.argmax(Q_Table[current])
        if next in shortest_path:
            print("Unable to find the shortest path, try increasing the number of episodes\n")
            shortest_path = []
            flag = False
            break
        else:
            shortest_path.append(next)
            current = next
            count+=1
    if flag == True:
        print("The shortest path through the maze is:\n")
        print(shortest_path, "\n")
        shortest_path_arrows = []
        for s in range(len(shortest_path) - 1):
            if shortest_path[s+1] - shortest_path[s] == 10:
                shortest_path_arrows.append('\u2193')
            if shortest_path[s+1] - shortest_path[s] == -10:
                shortest_path_arrows.append('\u2191')
            if shortest_path[s+1] - shortest_path[s] == 1:
                shortest_path_arrows.append('\u2192')
            if shortest_path[s+1] - shortest_path[s] == -1:
                shortest_path_arrows.append('\u2190')
        print(shortest_path_arrows)
    return shortest_path


#create horizontal lines on gui
def horizontal(k,l,j, canvas):
    canvas.create_line(k, j, l, j, width=3, fill="black")
#create vertical lines on gui
def vertical(i,l,j,canvas):
    canvas.create_line(l, i, l, j, width=3, fill="black")
#recreate the maze on the gui
def create_grid(canvas):
     i = 10
     j = 74
     k = 10
     l = 74
     for n in range(5):
         for m in range(10):
             hor = [0, 1]
             if n == 0:
                 if m == 1 or m == 4 or m == 7 or m == 8:
                    horizontal(k,l,j,canvas)
                 if m == 2 or m == 5:
                     vertical(i, l, j, canvas)
             elif n == 1:
                 if m == 1 or m == 2 or m == 3 or m == 5 or m == 9:
                    horizontal(k,l,j,canvas)
                 if m == 0 or m == 2 or m == 4 or m == 6 or m == 7:
                     vertical(i, l, j, canvas)
             elif n == 2:
                 if m == 0 or m == 3 or m == 6 or m == 7:
                    horizontal(k,l,j,canvas)
                 if m == 1 or m == 3 or m == 5 or m == 7 or m == 8:
                     vertical(i, l, j, canvas)
             elif n == 3:
                 if m == 1 or m == 2 or m == 5 or m == 6 or m == 8 or m == 9:
                    horizontal(k,l,j,canvas)
                 if m == 2 or m == 4 or m == 6:
                     vertical(i, l, j, canvas)
             elif n == 4:
                 if m == 3 or m == 5:
                     vertical(i, l, j, canvas)
             l += 64
             k += 64

         i+=64
         j+=64
         l=74
         k=10
#moves the circle through the maze
def move_maze(i, x, y, circle, delay, path, canvas, root, count):
    global running
    canvas.move(circle, x, y)
    if running:
        if i < len(path) - 1:
            curr_x_val = ((path[i] % 10) * 2 + 1) * 32 + 10
            curr_y_val = (math.floor(path[i] / 10) * 64) + 42
            new_x_val = ((path[i+1] % 10) * 2 + 1) * 32 + 10
            new_y_val = (math.floor(path[i+1] / 10) * 64) + 42
            if path[i] == 0 and path[i-1] == 49:
                count+=1
                change_episode_text(root, "Episode {}".format(count))
            root.after(delay, lambda: move_maze(i, (new_x_val - curr_x_val), (new_y_val - curr_y_val), circle, delay, path, canvas, root, count))
            i+=1  
#displays the current episode of training phase
def change_episode_text(root, e):
    episode_no.config(text=e)
#displays which path you are viewing
def change_path_text(root, p):
    path_type.config(text=p)    
#stops the program
def stop_program():
    global running
    running = False
def start_program():
    global running
    running = True
#define gui
def gui():
    global episode_no, path_type, training_path, shortest_path
    root = Tk()
    root.title("Maze")
    root.configure(background="white")
    canvas = Canvas(root, width=10.25 * 64, height=5.25 * 64, bg="DodgerBlue")
    canvas.create_rectangle(10, 10, 650, 330,fill="white", outline="black", width=3)
    create_grid(canvas)
    canvas.pack()
    canvas2 = Canvas(root, width=11*64, height=2*64, bg="DodgerBlue")
    canvas2.create_text(350, 50, text="If you would like to switch between displaying the training phase and the shortest path,", justify="center")
    canvas2.create_text(350, 70, text=" please click stop before changing from one to the other!", justify="center")
    canvas2.pack()
    episode_no = Label(root)
    episode_no.configure(background="white", fg="black")
    path_type = Label(root)
    path_type.configure(background="white", fg="black")
    path_type.pack(side=tkinter.LEFT)
    def exit_program():
        root.destroy()
    def shortest_path_program(path):
        start_program()       
        canvas.delete("train")
        canvas.delete("sp")
        circle = canvas.create_oval(32, 32, 52, 52, fill="green", tags="sp")
        change_path_text(root, "  This is the Shortest Path Through the Maze")
        episode_no.pack_forget()
        root.after(1, lambda: move_maze(0, 0, 0, circle, 350, shortest_path, canvas, root, 0))
    def training_path_program(path):
        start_program()
        canvas.delete("sp")
        canvas.delete("train")
        episode_no.pack(side=tkinter.LEFT)
        circle = canvas.create_oval(32, 32, 52, 52, fill="red", tags="train")
        change_path_text(root, "  Displaying the Training Phase:")
        root.after(1, lambda: move_maze(0, 0, 0, circle, 5, training_path, canvas, root, 0))
    exit = Button(root, text="Exit", command=exit_program)
    exit.pack(side=tkinter.RIGHT)
    stop = Button(root, text="Stop", command=stop_program)
    stop.pack(side=tkinter.RIGHT)
    training = Button(root, text="Display Training",  command=lambda: training_path_program(training_path))
    training.pack(side=tkinter.RIGHT)
    short_path = Button(root, text="Display Shortest Path", command=lambda:shortest_path_program(shortest_path))
    short_path.pack(side=tkinter.RIGHT)
    root.mainloop()

       
#main function that drives the program
def main():
    global training_path, shortest_path, running
    running = True
    start_time = time.time()
    start = 0
    goal = 49
    gamma = 0.3
    learning_rate = 0.5
    episodes = 100
    parser = argparse.ArgumentParser(exit_on_error=False, description='Options to Change the Hyper Parameters')
    parser.add_argument('--episodes', type=int, required=False, default=episodes, help = 'Integer value for number of episodes')
    parser.add_argument('--gamma', type=float, required=False, default=gamma, help='Floating point number for value of gamma')
    parser.add_argument('--learning_rate', type=float, required=False, default=learning_rate, help='Floating point number for value of learning_rate')
    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        print("You must choose an option --episodes, --gamma, --learning_rate or --help!\]n")
    episodes = args.episodes
    gamma = args.gamma
    learning_rate = args.learning_rate
    f = open("commandLine.txt", "r")
    print(f.read())

    print("\nInitialising the maze in memory!\n")

    Rewards = np.zeros(shape=[50, 50], dtype=float)
    Q_Table = np.zeros(shape=[50, 50], dtype=float)
    #define possible actions to populate the Rewards table
    moves_one = [0,0,1,2,12,10,20,21,31,32,22,31,30,40,41,42,43,33,34,44,34,24,25,35,24,14,13,3,4,5,15,16,26,27,16,6,7,8,9,19,18,28,38,39,38,37,47,47,49]
    moves_two = [1,10,2,12,11,20,21,31,32,22,23,30,40,41,42,43,33,34,44,45,24,25,35,36,14,13,3,4,5,15,16,26,27,17,6,7,8,9,19,18,28,38,37,29,39,47,46,48,49]
    for i in range(len(moves_one)):
        Rewards[moves_one[i], moves_two[i]] = 1
        Rewards[moves_two[i], moves_one[i]] = 1
    Rewards[48][49] = 5
    print("Training started!\n")
    training_path = train(Rewards, Q_Table, gamma, learning_rate, goal, episodes)
    end_time = time.time()
    print("Total elapsed time was", round(((end_time - start_time) * 1000), 2), "milliseconds!\n")
    shortest_path = display_path(start, goal, Q_Table)
    if len(shortest_path) > 0:
        gui()
        start_program()
    #The print Q_Table is commented out as I thought it might be overwhelming to look at but
    #obviously feel free to uncomment it if you want to look
    #my_print(Q_Table)

if __name__ == "__main__":
    main()

