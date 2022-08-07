#!/usr/bin/env python3

from datetime import date, datetime
import requests

from PIL import Image, ImageTk
from io  import BytesIO

class MyImages:
    """Class for handling application images."""
    def __init__(self, cv, mapit):
        """Initialize this class:
            image_dates: datestrings used to identify the correct 
                            images for download (mmddyyyy)
            images: holds the actual current images being displayed
            cv: image canvasses in the main window
            mapit: image canvassas mapped in the main window
        """
        tday = date.today()
        self.image_dates = {
            'left':f"{tday.month:02d}{tday.day:02d}{tday.year}", 
            'right':f"{tday.month:02d}{tday.day:02d}{tday.year}"
        }
        self.images = {
            'left':None,
            'right':None
        }
        self.cv = cv
        self.mapit = mapit
    
    def set_image_date(self, side='left', cal_date='None'):
        """Update the image on the left or right side.
            side: left or right side of the GUI main window
            cal_date: raw date returned by the calendar instance (mm/dd/yy)
        """
        if not cal_date:
            return False
        else:
            cdate = self.parse_cal_date(cal_date)
            if self._is_valid_day(cal_date):
                self.image_dates[side] = cdate
                self.load_image(side)
                self.update_image(side)

    def _is_valid_day(self, cal_date):
        """Check to see if the returned calendar date falls 
            within the available images dates
        """
        first = datetime.strptime("1/1/16", "%m/%d/%y")
        past = datetime.strptime(cal_date, "%m/%d/%y")
        present = datetime.now()
        if first.date() < past.date() < present.date():
            return True
        else:
            print(f"The date {cal_date} is "\
                "outside the valid range (1/1/16-present)")
            return False

    def parse_cal_date(self, cal_date):
        """Parse the returned calendar date string and format 
            it into the image date string.
        """
        # expecting a date in mm/dd/yy format
        mon, day, yr = cal_date.split('/')
        if mon and day and yr:
            return f"{int(mon):02d}{int(day):02d}20{int(yr):02d}"

    def load_image(self, side='left'):
        """Load the image from the website into local memory, referenced by the self.images variable"""
        url = f"https://usicecenter.gov/File/DownloadArchive?prd=3{self.image_dates[side]}"
        print(f"Loading: {url}")
        r = requests.get(url)
        image = Image.open(BytesIO(r.content))
        # we want to resize so that it fits within the GUI main window canvas
        resized = image.resize((528,408), Image.ANTIALIAS)
        self.images[side] = ImageTk.PhotoImage(resized)

    def get_image(self, side='left'):
        """Getter for downloading a specific image in memory."""
        return self.images[side]

    def update_image(self, side='left'):
        """Update the given side canvas in the GUI main window"""
        self.cv[side].itemconfig(self.mapit[side], image=self.images[side])