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
    def __init__(self, x, y, flip_speed=10, toggle=False):
        self.x = x
        self.y = y
        self.flip_speed = flip_speed
        self.toggle = toggle

        self.wheel_item = []
        self.count = 0
        for i in range(9):
            self.wheel_item.append(root.canvas.create_image(self.x, self.y, image=wheel_images[i]))
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

    def negate_motion(self):
        if self.toggle:
            self.toggle = False
        else:
            self.toggle = True
            self.wheel_time()
            self.flip_speed = randrange(19, 34)


#todo Temporary function
def stop_all():
    wheels_are_stopped = False

    # First loop to check if at least one is spinning, if so stop it
    for wheel in wheels:
        if wheel.toggle:
            wheel.negate_motion()
            wheels_are_stopped = True

    # If wheels were already all stopped, start them all
    if not wheels_are_stopped:
        for wheel in wheels:
            wheel.negate_motion()

# *********************************************************************


root = Window()

wheel_images = GetImages()

# Reorganized the wheels into a list to make iteration easier, but
# can be changed if it's not handy enough
wheels = [Wheel(200, 300, 200), Wheel(400, 300, 300), Wheel(600, 300, 100)]

#todo root.canvas create_window, then put an image inside, tag image and use http://effbot.org/zone/tkinter-canvas-find-withtag.htm
stop_all_button = Button(root.mainframe, text="Start/Stop", command = stop_all)
stop_wheel_1 = Button(root.mainframe, text="Wheel 1", command=wheels[0].negate_motion)
stop_wheel_2 = Button(root.mainframe, text="Wheel 2", command=wheels[1].negate_motion)
stop_wheel_3 = Button(root.mainframe, text="Wheel 3", command=wheels[2].negate_motion)
stop_all_button.pack(side=LEFT)
stop_wheel_1.pack(side=LEFT)
stop_wheel_2.pack(side=LEFT)
stop_wheel_3.pack(side=LEFT) # these can be centred later

root.mainloop()
