import random
import time
from tkinter import *
from tkinter import ttk

def create_maze(width, height):
    width = width + 1
    height = height + 1
    window = Tk()
    window.title("Maze")
    canvas = Canvas(window, width=width*64,
                        height=height*64, bg = "white")

    canvas.create_rectangle(10, 10, 650, 330, outline="black", width=3)

    create_grid(canvas)
    l = [0, 10, 20, 21, 31, 30, 40, 41, 42, 43, 33, 34, 24, 14, 13, 3, 4, 5, 15, 16, 6, 7, 8, 9, 19, 18, 28, 38, 37, 47, 48, 49]
    for i in range(len(l)):
        placement = (l[i] * 2 + 1) * 32 + 10
        create_circle(placement, placement, 10, canvas)
    canvas.pack()
    window.mainloop()

def create_circle(x, y, r, canvas):
    "Create dot with fill colour: (x,y): center coordinates, r: radius "
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1,fill='green', outline='green')

def horizontal(k,l,j, canvas):
    canvas.create_line(k, j, l, j, width=3)

def vertical(i,l,j,canvas):
    canvas.create_line(l, i, l, j, width=3)

def create_grid(canvas):
     # canvas.create_line(10,74, 74, 74) #horizontal
     # canvas.create_line(74, 10, 74, 74) # vertical
     # canvas.create_line(74, 74, 138, 74)  # horizontal
     # canvas.create_line(136, 10, 138, 74)  # vertical
     i = 10
     j = 74
     k = 10
     l = 74
     for n in range(5):
         for m in range(10):
             #canvas.create_line(k, j, l, j)# horizontal
             #canvas.create_line(l, i, l, j)  # vertical
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


    #canvas.create_line(10, 30, 30, 30)  # horizontal
    #canvas.create_line(30, 10, 30, 30)  # vertical




def display_lines(x1, y1, x2, y2, color, canvas):
    x_plus = x1     ## all lines are evenly spaced
    y_plus = y1

    # for ctr in range(8):
    #     canvas.create_line(x1, y1, x2, y2, fill = color)
    #     x1 += x_plus
    #     x2 += x_plus
    #     y1 += y_plus
    #     y2 += y_plus

def main():

    # root = Tk()
    #
    # content = ttk.Frame(root)
    # root.title("Maze")
    # frame = ttk.Frame(content, width=1000, height=500)
    # #frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
    #
    # ok = ttk.Button(content, text="Okay")
    # cancel = ttk.Button(content, text="Cancel")
    #
    # content.grid(column=0, row=0)
    # frame.grid(column=0, row=0, columnspan=3, rowspan=2)
    # ok.grid(column=3, row=3)
    # cancel.grid(column=4, row=3)
    create_maze(10, 5)

    #root.mainloop()


if __name__ == "__main__":
    main()




