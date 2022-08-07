import tkinter as tk

from datetime import date
from tkcalendar import Calendar

class MyCalendar:
    """Class for opening calendars from GUI main window"""
    def __init__(self, master=None, side='left', images=None):
        # first we add some variables
        self.images = images

        # now we create the Calendar GUI
        self.second = tk.Toplevel()
        self.second.title("Calendar")
        self.second.geometry("200x280")
        # Add Calendar
        tday = date.today()
        self.cal = Calendar(self.second, selectmode = 'day',
                            year = tday.year, month = tday.month,
                            day = tday.day)
        
        self.cal.pack(pady = 20)
        
        # Add Button and Label
        tk.Button(self.second, text = "Get Date",
                    command = lambda: self.grad_date(side)).pack(pady = 20)

    def grad_date(self, side):
        cal_date = self.cal.get_date()
        self.images.set_image_date(side, cal_date)
        self.hide()
    
    def hide(self):
        self.second.withdraw()
        self.second.destroy()

    def show(self):
        self.second.deiconify()