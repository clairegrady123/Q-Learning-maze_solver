from tkinter import *

# def create_circle(x, y, r, canvas):
#     "Create dot with fill colour: (x,y): center coordinates, r: radius "
#     x0 = x - r
#     y0 = y - r
#     x1 = x + r
#     y1 = y + r
#     return canvas.create_oval(x0, y0, x1, y1, fill='green', outline='green')

def move_maze(i, x, y):
    test = [0, 10, 20, 21, 31, 30, 40, 41, 42, 43, 33, 34, 24, 14, 13, 3, 4, 5, 15, 16, 6, 7, 8, 9, 19, 18, 28, 38, 37, 47, 48, 49]
    canvas.move(circle, x, y)
    if i < len(test) - 1:
        if test[i] - test[i+1] == -10:
            i += 1
            root.after(500, lambda: move_maze(i, 0, 64))
        elif test[i] - test[i+1] == 10:
            i += 1
            root.after(500, lambda: move_maze(i, 0, -64))
        elif test[i] - test[i+1] == -1:
            i += 1
            root.after(500, lambda: move_maze(i, 64, 0))
        elif test[i] - test[i+1] == 1:
            i += 1
            root.after(500, lambda: move_maze(i, -64, 0))

def horizontal(k, l, j, canvas):
    canvas.create_line(k, j, l, j, width=3)

def vertical(i, l, j, canvas):
    canvas.create_line(l, i, l, j, width=3)

def create_grid(canvas):
    i = 10
    j = 74
    k = 10
    l = 74
    for n in range(5):
        for m in range(10):
            if n == 0:
                if m == 1 or m == 4 or m == 7 or m == 8:
                    horizontal(k, l, j, canvas)
                if m == 2 or m == 5:
                    vertical(i, l, j, canvas)
            elif n == 1:
                if m == 1 or m == 2 or m == 3 or m == 5 or m == 9:
                    horizontal(k, l, j, canvas)
                if m == 0 or m == 2 or m == 4 or m == 6 or m == 7:
                    vertical(i, l, j, canvas)
            elif n == 2:
                if m == 0 or m == 3 or m == 6 or m == 7:
                    horizontal(k, l, j, canvas)
                if m == 1 or m == 3 or m == 5 or m == 7 or m == 8:
                    vertical(i, l, j, canvas)
            elif n == 3:
                if m == 1 or m == 2 or m == 5 or m == 6 or m == 8 or m == 9:
                    horizontal(k, l, j, canvas)
                if m == 2 or m == 4 or m == 6:
                    vertical(i, l, j, canvas)
            elif n == 4:
                if m == 3 or m == 5:
                    vertical(i, l, j, canvas)

            l += 64
            k += 64

        i += 64
        j += 64
        l = 74
        k = 10

def exit_program():
    root.destroy()

root = Tk()
root.title("Maze")
content = Frame(root)
canvas = Canvas(root, width=11 * 64, height=11 * 64, bg="white")
canvas.create_rectangle(10, 10, 650, 330, outline="black", width=3)
create_grid(canvas)
circle = canvas.create_oval(32, 32, 52, 52, fill="green")
canvas.pack()

exit = Button(root, text="Exit", command=exit_program)
exit.pack()
#run = Button(root, text="Run")
#run.pack()
#run.bind("<Button-1>", please)
test = [0, 10, 20, 21, 31, 30, 40, 41, 42, 43, 33, 34, 24, 14, 13, 3, 4, 5, 15, 16, 6, 7, 8, 9, 19, 18, 28, 38, 37, 47, 48, 49]

root.after(50, lambda:move_maze(0, 0, 0))
root.mainloop()



# if __name__ == "__main__":
#     main()