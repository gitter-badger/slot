from tkinter import *
from tkinter import ttk


class Window(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Fruit Machine")

        self.title("Fruit Machine")
        self.geometry('800x600')

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

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.wheel_item = []
        self.count = 0
        for i in range(9):
            self.wheel_item.append(root.canvas.create_image(self.x, self.y, image = wheel_images[i]))

    def wheel_time(self):
        print("made it")
        root.canvas.after(10, self.wheel_count)

    def wheel_count(self):
        root.canvas.lower(self.wheel_item[self.count])
        if self.count == 7:
            self.count = 0
        else:
            self.count += 1
        root.canvas.update()
        return self.wheel_time()



# *********************************************************************


root = Window()

wheel_images = GetImages()
wheel_1 = Wheel(400, 300)
wheel_1.wheel_time()

root.mainloop()
