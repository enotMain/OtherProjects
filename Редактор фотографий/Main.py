import random
from tkinter import Tk, Canvas, E, W, N, S
from tkinter.ttk import Button

from PIL import Image, ImageDraw, ImageTk  # Подключим необходимые библиотеки

# Создание окна
root = Tk();
root.title("Photo editor")

# Переменные для работы с фотографией
image = Image.open("temp.jpg")
image.save("lastVersion.jpg", "JPEG")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

# Создание Canvas с загрузкой исходной фотографии
canvas = Canvas(root, width=width, height=height)
imageCanvas = ImageTk.PhotoImage(image)
canvas.create_image(width / 2, height / 2, image=imageCanvas)

# Функция, которая делает фотографию серой
def make_grey():

    global image, imageCanvas, draw, pix

    image = Image.open("lastVersion.jpg")
    pix = image.load()
    draw = ImageDraw.Draw(image)

    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = (a + b + c) // 3
            draw.point((i, j), (s, s, s))

    image.save("lastVersion.jpg", "JPEG")
    image = Image.open("lastVersion.jpg")
    imageCanvas = ImageTk.PhotoImage(image)
    canvas.create_image(width / 2, height / 2, image=imageCanvas)

# Функция, которая делает фотографию сепия
def make_sepia():

    global image, imageCanvas, draw, pix

    image = Image.open("lastVersion.jpg")
    pix = image.load()
    draw = ImageDraw.Draw(image)

    depth = 30
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = (a + b + c) // 3
            a = s + depth * 2
            b = s + depth
            c = s
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))

    image.save("lastVersion.jpg", "JPEG")
    image = Image.open("lastVersion.jpg")
    imageCanvas = ImageTk.PhotoImage(image)
    canvas.create_image(width / 2, height / 2, image=imageCanvas)

# Функция, которая переводит фотографию в режим негатив
def make_negative():

    global image, imageCanvas, draw, pix

    image = Image.open("lastVersion.jpg")
    pix = image.load()
    draw = ImageDraw.Draw(image)

    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))

    image.save("lastVersion.jpg", "JPEG")
    image = Image.open("lastVersion.jpg")
    imageCanvas = ImageTk.PhotoImage(image)
    canvas.create_image(width / 2, height / 2, image=imageCanvas)

# Функция, которая добавляет шумы
def add_noise():

    global image, imageCanvas, draw, pix

    image = Image.open("lastVersion.jpg")
    pix = image.load()
    draw = ImageDraw.Draw(image)

    factor = 70
    for i in range(width):
        for j in range(height):
            rand = random.randint(-factor, factor)
            a = pix[i, j][0] + rand
            b = pix[i, j][1] + rand
            c = pix[i, j][2] + rand
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            if c < 0:
                c = 0
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))

    image.save("lastVersion.jpg", "JPEG")
    image = Image.open("lastVersion.jpg")
    imageCanvas = ImageTk.PhotoImage(image)
    canvas.create_image(width / 2, height / 2, image=imageCanvas)

# Функция, которая делает фотографию яркой
def make_light():

    global image, imageCanvas, draw, pix

    image = Image.open("lastVersion.jpg")
    pix = image.load()
    draw = ImageDraw.Draw(image)

    factor = 100
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0] + factor
            b = pix[i, j][1] + factor
            c = pix[i, j][2] + factor
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            if c < 0:
                c = 0
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))

    image.save("lastVersion.jpg", "JPEG")
    image = Image.open("lastVersion.jpg")
    imageCanvas = ImageTk.PhotoImage(image)
    canvas.create_image(width / 2, height / 2, image=imageCanvas)

# Функция, которая делает фотографию темной
def make_dark():

    global image, imageCanvas, draw, pix

    image = Image.open("lastVersion.jpg")
    pix = image.load()
    draw = ImageDraw.Draw(image)

    factor = -100
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0] + factor
            b = pix[i, j][1] + factor
            c = pix[i, j][2] + factor
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            if c < 0:
                c = 0
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))

    image.save("lastVersion.jpg", "JPEG")
    image = Image.open("lastVersion.jpg")
    imageCanvas = ImageTk.PhotoImage(image)
    canvas.create_image(width / 2, height / 2, image=imageCanvas)

# Функция, которая делает фотографию черно-белой
def make_black_and_white():

    global image, imageCanvas, draw, pix

    image = Image.open("lastVersion.jpg")
    pix = image.load()
    draw = ImageDraw.Draw(image)

    factor = -50
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = a + b + c
            if s > (((255 + factor) // 2) * 3):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))

    image.save("lastVersion.jpg", "JPEG")
    image = Image.open("lastVersion.jpg")
    imageCanvas = ImageTk.PhotoImage(image)
    canvas.create_image(width / 2, height / 2, image=imageCanvas)

# Функция, которая переворачивает фотографию по вертикали
def up_to_down():

    global image, imageCanvas, draw, pix

    image = Image.open("lastVersion.jpg")
    pix = image.load()
    draw = ImageDraw.Draw(image)

    for i in range(width):
        for j in range(height//2):
            a = pix[i, j][0]
            a1 = pix[i, height - j - 1][0]
            b = pix[i, j][1]
            b1 = pix[i, height - j - 1][1]
            c = pix[i, j][2]
            c1 = pix[i, height -j - 1][2]
            draw.point((i, j), (a1, b1, c1))
            draw.point((i, height - j - 1), (a, b, c))

    image.save("lastVersion.jpg", "JPEG")
    image = Image.open("lastVersion.jpg")
    imageCanvas = ImageTk.PhotoImage(image)
    canvas.create_image(width / 2, height / 2, image=imageCanvas)

# Функция, которая переворачивает фотографию по горизонтали
def left_to_right():

    global image, imageCanvas, draw, pix

    image = Image.open("lastVersion.jpg")
    pix = image.load()
    draw = ImageDraw.Draw(image)

    for i in range(width//2):
        for j in range(height):
            a = pix[i, j][0]
            a1 = pix[width - i - 1, j][0]
            b = pix[i, j][1]
            b1 = pix[width - i - 1, j][1]
            c = pix[i, j][2]
            c1 = pix[width - i - 1, j][2]
            draw.point((i, j), (a1, b1, c1))
            draw.point((width - i - 1, j), (a, b, c))

    image.save("lastVersion.jpg", "JPEG")
    image = Image.open("lastVersion.jpg")
    imageCanvas = ImageTk.PhotoImage(image)
    canvas.create_image(width / 2, height / 2, image=imageCanvas)

# Загрузка исходника
def make_original():

    global image, imageCanvas

    image = Image.open("temp.jpg")
    image.save("lastVersion.jpg", "JPEG")
    image = Image.open("lastVersion.jpg")
    imageCanvas = ImageTk.PhotoImage(image)
    canvas.create_image(width / 2, height / 2, image=imageCanvas)

canvas.grid(row=1, column=0, columnspan=10, padx=5, pady=5, sticky=E+W+S+N)

# Создание кнопок
btn_grey = Button(text="Grey", command=lambda: make_grey())
btn_sepia = Button(text="Sepia", command=lambda: make_sepia())
btn_original = Button(text="Original", command=lambda: make_original())
btn_negative = Button(text="Negative", command=lambda: make_negative())
btn_noise = Button(text="Noise", command=lambda: add_noise())
btn_light = Button(text="Light", command=lambda: make_light())
btn_dark = Button(text="Dark", command=lambda: make_dark())
btn_black_and_white = Button(text="Black and white", command=lambda: make_black_and_white())
btn_up_to_down = Button(text="Up to down", command=lambda: up_to_down())
btn_left_to_right = Button(text="Left to right", command=lambda: left_to_right())

# Расположение кнопок на сетке окна
btn_original.grid(row=0, column=0, padx=5, pady=5, sticky=E+W+S+N)
btn_grey.grid(row=0, column=1, padx=5, pady=5, sticky=E+W+S+N)
btn_sepia.grid(row=0, column=2, padx=5, pady=5, sticky=E+W+S+N)
btn_negative.grid(row=0, column=3, padx=5, pady=5, sticky=E+W+S+N)
btn_noise.grid(row=0, column=4, padx=5, pady=5, sticky=E+W+S+N)
btn_light.grid(row=0, column=5, padx=5, pady=5, sticky=E+W+S+N)
btn_dark.grid(row=0, column=6, padx=5, pady=5, sticky=E+W+S+N)
btn_black_and_white.grid(row=0, column=7, padx=5, pady=5, sticky=E+W+S+N)
btn_up_to_down.grid(row=0, column=8, padx=5, pady=5, sticky=E+W+S+N)
btn_left_to_right.grid(row=0, column=9, padx=5, pady=5, sticky=E+W+S+N)

del draw

root.mainloop()