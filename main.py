from tkinter import *
from tkinter import ttk
from random import randrange

class Window(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Fruit Machine")

        self.title("Fruit Machine")
        self.geometry('800x650')#todo make this 800x600, it's current state is before displaying temporary button

        self.mainframe = ttk.Frame(self)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.pack(expand=True)

        self.canvas = Canvas(self.mainframe, width=800, height=600, bg= 'black')
        self.canvas.pack()


class GetImages(object):
    def __init__(self):

        self.wheel_images = []
        # Creates a list of Number.png formatted as string
        for each in range(1,10):
            self.wheel_images.append("images\\" + str(each) + ".png")

        # Re-creates list with the image in it's place
        for each in range(len(self.wheel_images)):
            self.wheel_images[each] = PhotoImage(file=self.wheel_images[each])

    def __getitem__(self, index):
        return self.wheel_images[index]


class Wheel(object):


    def __init__(self, x, y, flip_speed=10, toggle= False):

        self.x = x
        self.y = y
        self.flip_speed = flip_speed
        self.toggle = toggle

        self.wheel_item = []
        self.count = 0
        for i in range(9):
            self.wheel_item.append(root.canvas.create_image(self.x, self.y, image = wheel_images[i]))
        self.wheel_time()

    def wheel_time(self):
        root.canvas.after(self.flip_speed, self.wheel_count)

    def wheel_count(self):
        root.canvas.lower(self.wheel_item[self.count])
        if self.toggle:

            if self.count == 8:
                self.count = 0
            else:
                self.count += 1
            root.canvas.update()
            self.wheel_time()


def stop_all(): #todo Temporary function
    if wheel_1.toggle and wheel_2.toggle and wheel_3.toggle:
        wheel_1.toggle, wheel_2.toggle, wheel_3.toggle = False, False, False
    elif not wheel_1.toggle and not wheel_2.toggle and not wheel_3.toggle:
        wheel_1.toggle = True
        wheel_2.toggle = True
        wheel_3.toggle = True

        wheel_1.wheel_time()
        wheel_2.wheel_time()
        wheel_3.wheel_time()

        stop_milli = randrange(3001,5002)

        wheel_1.flip_speed = randrange(19, 34)
        wheel_2.flip_speed = randrange(19, 34)
        wheel_3.flip_speed = randrange(19, 34)

        print(wheel_1.flip_speed, wheel_2.flip_speed, wheel_3.flip_speed)
        print(stop_milli)

        root.canvas.after(stop_milli, stop_all) #todo instead of stop all, make a stop definition for each wheel

# *********************************************************************


root = Window()

wheel_images = GetImages()

wheel_1 = Wheel(200, 300, 200)

wheel_2 = Wheel(400, 300, 300)

wheel_3 = Wheel(600, 300, 100)

#todo root.canvas create_window, then put an image inside, tag image and use http://effbot.org/zone/tkinter-canvas-find-withtag.htm
button = Button(root.mainframe, text="Start/Stop", command = stop_all)
button.pack()

root.mainloop()
