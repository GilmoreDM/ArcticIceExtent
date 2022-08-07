#!/usr/bin/env python3

import tkinter as tk

from myImage import MyImages
from myCalendar import MyCalendar

class MyWindow:
    def __init__(self, master, *args, **kwargs) -> None:
        # first establish some variables
        # mapit: contains maps to the image canvasses
        # cv: the image canvassas
        # calendar: MyCalendar instances
        self.mapit = {'left':None, 'right':None} 
        self.cv = {'left':None, 'right':None}
        self.calendar = {'left':None, 'right':None}

        # now let's build our GUI
        self.master = master
        self.frame = tk.Frame(self.master)
        # create the main window
        self.master.title("Year to Year Comparison of Sea Ice Extent")
        w, h, x, y = 1054, 600, 80, 100
        self.master.geometry(f"{w}x{h}+{x}+{y}")

        # create a frame to hold the select menu and images
        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(side='top', fill='both', expand='yes')

        # create two frames with years starting with 2016
        # (second year images were available; comparing to the previous year)
        self.left_frame = tk.Frame(self.top_frame)
        self.left_frame.pack(side='left', fill='both', expand='yes')

        # button to launch the left side calendar
        tk.Button(self.left_frame, text="Show/Hide Calendar", 
                command=lambda: self.launch_calendar('left')).pack(pady=10)

        # create the right side frame
        self.right_frame = tk.Frame(self.top_frame)
        self.right_frame.pack(side='left', fill='both', expand='yes')

        # button to launch the right side calendar
        tk.Button(self.right_frame, text="Show/Hide Calendar", 
                command=lambda: self.launch_calendar('right')).pack(pady=10)

        # create a canvas for the left side image
        self.cv['left'] = tk.Canvas(self.left_frame, bg='white')
        self.cv['left'].pack(side='top', fill='both', expand='yes')
        # place the first image map in the canvas
        self.mapit['left'] = self.cv['left'].create_image(
                                            10, 10, image=None, anchor='nw')

        # create a canvas for the right side image
        self.cv['right'] = tk.Canvas(self.right_frame, bg='white')
        self.cv['right'].pack(side='top', fill='both', expand='yes')
        # place the first image map in the canvas
        self.mapit['right'] = self.cv['right'].create_image(
                                            10, 10, image=None, anchor='nw')
        
        # create the images object here so we pass full versions of cv, map
        self.images = MyImages(self.cv, self.mapit)

    def launch_calendar(self, side):
        self.calendar[side] = MyCalendar(self.master, side, self.images)


if __name__ == "__main__":
    root = tk.Tk()
    app = MyWindow(root)
    root.mainloop()
