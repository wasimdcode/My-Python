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
    Get the absolute path to a resource, whether running as a script
    or as a PyInstaller bundle.
    """
    if getattr(sys, '_MEIPASS', False):
        # PyInstaller creates a temp folder and stores resources in _MEIPASS
        base_path = sys._MEIPASS
    else:
        # In normal Python execution, use the directory of this script
        base_path = os.path.dirname(os.path.abspath(__file__))

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
    # Load the PNG icon via resource_path()
    icon_path = resource_path("w.png")
    icon_img = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_img)

    # Set the window icon
    entrance.iconphoto(True, icon_photo)
    # Get screen dimensions
    screen_width = entrance.winfo_screenwidth()
    screen_height = entrance.winfo_screenheight()

    # Use 100% of screen for app size
    app_width = int(screen_width * 1)
    app_height = int(screen_height * 1)

    # Center the window
    x = int((screen_width / 2) - (app_width / 2))
    y = int((screen_height / 2) - (app_height / 2))

    # Set dynamic window size and position
    entrance.geometry(f"{app_width}x{app_height}+{x}+{y}")

    # This is Used For Entrance Background
    # For Accessing Image
    img_path = resource_path("wOYO.png")
    original_img = Image.open(img_path)
    img = Image.open(resource_path("wOYO.png"))


    # Function to resize and reposition elements when window size changes
    def resize_and_reposition(event=None):
        # Get current window size
        window_width = entrance.winfo_width()
        window_height = entrance.winfo_height()
        
        # If the window hasn't been fully initialized yet, use app_width and app_height
        if window_width <= 1:
            window_width = app_width
        if window_height <= 1:
            window_height = app_height
        
        # Resize image to match window size
        resized_img = original_img.resize((window_width, window_height))
        
        # Update the PhotoImage
        global logo
        logo = ImageTk.PhotoImage(resized_img)
        
        # Update the background label
        logo_label.config(image=logo)
        logo_label.place(x=0, y=0, width=window_width, height=window_height)
        
        # Calculate center position for welcome label - positioned slightly above center
        label_x = window_width // 2
        label_y = int(window_height * 0.48)  # Positioned at 48% of window height
        entrancelabel.place(relx=0.5, rely=0.50, anchor="center")
        
        # Calculate position for button - positioned below the label
        button_x = window_width // 2
        button_y = int(window_height * 0.56)  # Positioned at 56% of window height
        start_button.place(relx=0.5, rely=0.60, anchor="center")

    # Create Label to display background image
    logo_label = tk.Label(entrance)

    # For Showing Welcome Text Message
    entrancelabel = tk.Label(entrance, text="Welcome To WOYO - India's Finest Hotel Booking Experience", 
                            font=("Bahnschrift SemiBold", 17, "bold"), 
                            bg="white", fg="black")

    # This is The Button Styling
    bstyle = ttk.Style()
    # Button's Formatting/Styling
    bstyle.configure('TButton',
                    foreground='#d40e15',
                    background='black',
                    font=('Bahnschrift', 20, 'bold'),
                    padding=(10, 5))

    # Creating the Button and Giving it Style that we Created
    start_button = ttk.Button(entrance, text="START BOOKING", style='TButton', command=open_form)

    # Initial resize and positioning
    entrance.update_idletasks()  # Make sure the window is updated
    resize_and_reposition()  # Initial call to set up the image and positions

    # Bind the resize event to the window
    entrance.bind("<Configure>", resize_and_reposition)

    # This is the End of Window and It's for Window Stay Opened
    entrance.mainloop()

    # Checks if Scipt is run directly (not imported)
    # Calls the function to start the program
        
# Calling Entrance Function
Entrance()