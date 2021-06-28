from tkinter import *

canvas_width = 850
canvas_height = 500
brush_size = 3

oval_size_x = 50
oval_size_y = 50

rectangle_size_x = 50
rectangle_size_y = 50

what_func = 1

color = "black"

root = Tk()
root.title("Paint on Python")


def paint(event):

    global brush_size
    global color

    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size

    canvas.create_oval(x1, y1, x2, y2,
                       fill=color, outline=color)


def brush_size_change(new_size):
    global brush_size
    brush_size = new_size


def color_change(new_color):
    global color
    color = new_color


def choose_func_oval():
    global what_func
    what_func = 0

    choose_func()


def choose_func_rect():
    global what_func
    what_func = 1

    choose_func()


def choose_func():

    if what_func == 0:
        root.bind("<Button-1>", create_oval)
    else:
        root.bind("<Button-1>", create_rectangle)


def create_oval(event):

    x1 = event.x - oval_size_x
    x2 = event.x + oval_size_x
    y1 = event.y - oval_size_y
    y2 = event.y + oval_size_y

    canvas.create_oval(x1, y1, x2, y2,
                       outline=color, width=5)


def create_rectangle(event):

    x1 = event.x - rectangle_size_x
    x2 = event.x + rectangle_size_x
    y1 = event.y - rectangle_size_y
    y2 = event.y + rectangle_size_y

    canvas.create_rectangle(x1, y1, x2, y2,
                            outline=color, width=5)


def canvas_clear():
    canvas.delete(ALL)


def create_message():
    canvas.create_text(canvas_width / 2, canvas_height / 2, text=message_entry.get(),
                       justify=CENTER, font="Times 30", fill=color)


canvas = Canvas(root,
                width=canvas_width, height=canvas_height,
                bg="white")
root.bind("<B1-Motion>", paint)

red_button = Button(text="Red", width=15,
                    command=lambda: color_change("red"))
yellow_button = Button(text="Yellow", width=15,
                       command=lambda: color_change("yellow"))
black_button = Button(text="Black", width=15,
                      command=lambda: color_change("black"))
blue_button = Button(text="Blue", width=15,
                     command=lambda: color_change("blue"))
green_button = Button(text="Green", width=15,
                      command=lambda: color_change("green"))
white_button = Button(text="White", width=15,
                      command=lambda: color_change("white"))
cyan_button = Button(text="Cyan", width=15,
                     command=lambda: color_change("cyan"))

size_1_btn = Button(text="1", width=15,
                    command=lambda: brush_size_change(1))
size_3_btn = Button(text="3", width=15,
                    command=lambda: brush_size_change(3))
size_6_btn = Button(text="6", width=15,
                    command=lambda: brush_size_change(6))
size_9_btn = Button(text="9", width=15,
                    command=lambda: brush_size_change(9))
size_12_btn = Button(text="12", width=15,
                     command=lambda: brush_size_change(12))
size_15_btn = Button(text="15", width=15,
                     command=lambda: brush_size_change(15))
size_18_btn = Button(text="18", width=15,
                     command=lambda: brush_size_change(18))

create_oval_btn = Button(text="Create oval", width=15,
                         command=lambda: choose_func_oval())
create_rectangle_btn = Button(text="Create rectangle", width=15,
                              command=lambda: choose_func_rect())
canvas_clear_btn = Button(text="Clear", width=15,
                          command=lambda: canvas_clear())
message_button = Button(text="Entry text",
                        command=lambda: create_message())

message_entry = Entry()

canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E+W+S+N)

red_button.grid(row=0, column=0)
yellow_button.grid(row=0, column=1)
black_button.grid(row=0, column=2)
blue_button.grid(row=0, column=3)
green_button.grid(row=0, column=4)
white_button.grid(row=0, column=5)
cyan_button.grid(row=0, column=6)

size_1_btn.grid(row=1, column=0)
size_3_btn.grid(row=1, column=1)
size_6_btn.grid(row=1, column=2)
size_9_btn.grid(row=1, column=3)
size_12_btn.grid(row=1, column=4)
size_15_btn.grid(row=1, column=5)
size_18_btn.grid(row=1, column=6)

create_oval_btn.grid(row=3, column=0)
create_rectangle_btn.grid(row=3, column=1)
canvas_clear_btn.grid(row=3, column=2)
message_entry.grid(row=3, column=3)
message_button.grid(row=3, column=4)

root.mainloop()