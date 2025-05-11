import datetime
from datetime import datetime  
import tkinter as tk
from tkinter import END, BooleanVar, Checkbutton, ttk
import PIL 
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import winsound
from tkinter import messagebox as mb
import re
import check
def open_entrance():
    def open_form():
        entrance.destroy()
        check.open_form()
    entrance = tk.Tk()
    entrance.title("WOYO")
    img = Image.open("wOYO.png")
    img = img.resize((1500,750))
    logo = ImageTk.PhotoImage(img)
    logo_label = tk.Label(entrance, image=logo)
    logo_label.place(x=-2, y=-2)
    entrancelabel = tk.Label(entrance, text="Welcome To WOYO - India's Finest Hotel Booking Experience", font=("Bahnschrift SemiBold", 19, "bold"),bg="white", fg="black")

    entrancelabel.place(x=412, y=360)
    entrance.geometry("1450x750+50+50")
    entrance.resizable(0,0)


    bstyle = ttk.Style()
    bstyle.configure('TButton',
                    foreground='#d40e15',
                    background='black',
                    font=('Bahnschrift',20,'bold'),
                    padding=(10,5))
    start_button = ttk.Button(entrance, text="START BOOKING",style='TButton',command=open_form)

    start_button.place(x=650, y=425)
    entrance.mainloop()
    if __name__ == "__check__":
        check()
open_entrance()