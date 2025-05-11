# This is the Entrance Page
# Tkinter for GUI 
import tkinter as tk
# TTK for TK theme Widget
from tkinter import ttk
# PIL for Using Images
from PIL import Image, ImageTk
# This is our Form Page it's imported for Accessing that file
import Second
import sys, os

def resource_path(relative_path):
    """
    Get the absolute path to a resource, whether running in P y
    or as a PyInstaller bundle.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# For Coming Back from Form Window by Using this function
def Entrance():
    # Function When Clicked on the Button
    def open_form():
    # For Closing Entrance Window
        entrance.destroy()
    # For Opening Second Window Form
        Second.Form()
    
    # This is the Starting Point of Window
    entrance = tk.Tk()
    # For Title
    entrance.title("WOYO")

    # This is Used For Entrance Background
    # For Accessing Image
    img_path = resource_path("wOYO.png")
    img = Image.open(img_path)
    # For Resize Image
    img = img.resize((1500,750))
    # Convet PIL image to Tkinter format
    logo = ImageTk.PhotoImage(img)
    # Create Label to display image
    logo_label = tk.Label(entrance, image=logo)
    # Position logo at any alignment
    logo_label.place(x=-2, y=-2)

    # For Showing Welcome Text Message
    entrancelabel = tk.Label(entrance, text="Welcome To WOYO - India's Finest Hotel Booking Experience", font=("Bahnschrift SemiBold", 19, "bold"),bg="white", fg="black")
    # For Label's Alignment
    entrancelabel.place(x=412, y=360)
    # For Adjusting Width Height and X-axis & Y-axis
    entrance.geometry("1450x750+50+50")
    # This Disable the Maximize Button
    entrance.resizable(0,0)

    # This is The Button Styling
    bstyle = ttk.Style()
    # Button's Formatting/Stylling
    bstyle.configure('TButton',
                    foreground='#d40e15',
                    background='black',
                    font=('Bahnschrift',20,'bold'),
                    padding=(10,5))
    # Creating the Button and Giving it Style that we Created
    start_button = ttk.Button(entrance, text="START BOOKING",style='TButton',command=open_form)
    # For Button Placement
    start_button.place(x=650, y=425)

    # This is the End of Window and It's for Window Stay Opened
    entrance.mainloop()

    # Checks if Scipt is run directly (not imported)
    if __name__ == "__main__":
        Second() #Calls the function to start the program
        
# Calling Entrance Function
Entrance()