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
def open_booking_form():

        def click_sound():
                winsound.PlaySound("click.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        click_sound()
        entrance.destroy()
        form = tk.Tk()
        form.title("WOYO BOOKING FORM")
        form.geometry("1100x750+50+50")
        form.resizable(0,0)
        form.configure(background='#fdd36e')

        imgf = Image.open("form.png")
        imgf = imgf.resize((600,750))
        logo = ImageTk.PhotoImage(imgf)
        logo_label = tk.Label(form, image=logo, border=0)
        logo_label.place(x=490, y=-1)
        
        

        formFrame = tk.LabelFrame(form, text="PERSONAL DETAILS", bg="#fdd36e",padx=54, pady=20, font=("Bahnschrift", 10, 'bold', 'underline'),bd=3, relief=tk.SUNKEN)
        formFrame.place(x=50, y=20)

        
        FullnameL = ttk.Label(formFrame, text="Full Name : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        FullnameL.grid(row=0, column=0, sticky='w')
        FullnameE = ttk.Entry(formFrame,width=20,font=('Consolas', 10))
        FullnameE.grid(row=0, column=1)


        PhoneL = ttk.Label(formFrame, text="Phone Number : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        PhoneL.grid(row=1, column=0, sticky='w')
        PhoneE = ttk.Entry(formFrame,width=20,font=('Consolas', 10))
        PhoneE.grid(row=1, column=1)

        
        EmailL = ttk.Label(formFrame, text="E-Mail : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        EmailL.grid(row=2, column=0, sticky='w')
        EmailE = ttk.Entry(formFrame,width=20,font=('Consolas', 10))
        EmailE.grid(row=2, column=1)
        def clear_all_fields():
                click_sound()
                # Clear personal details
                FullnameE.delete(0, tk.END)
                PhoneE.delete(0, tk.END)
                EmailE.delete(0, tk.END)

                # Clear booking details
                UsernameE.delete(0, tk.END)
                PasswordE.delete(0, tk.END)
                PassConfirmE.delete(0, tk.END)

                # Reset account details
                GuestE.delete(0, tk.END)
                GuestE.insert(0, "1")

                CheckInE.set_date(datetime.today())
                CheckOutE.set_date(datetime.today())

                RoomType.set('')     # or set to default like 'Single'
                Location.set('')      # or set to default like 'Delhi'

                # Clear special request
                SpecialReq.delete("1.0", tk.END)
        def validate_form():
                name = FullnameE.get().strip()
                phone = PhoneE.get().strip()
                email = EmailE.get().strip()

                username = UsernameE.get().strip()
                password = PasswordE.get()
                confirm = PassConfirmE.get()

                Checkin = CheckInE.get()
                Checkout = CheckOutE.get()
                room_type = RoomType.get()
                location = Location.get()
                special = SpecialReq.get("1.0", END).strip()

                try:
                        guests = int(GuestE.get())
                except ValueError:
                        mb.showerror("Error", "Number of Guests must be a numeric value.")
                        return

                # 🔸 Full Name Validation
                if not name:
                        mb.showerror("Error", "Full Name is required.")
                        return
                # Allow letters, spaces, apostrophes, hyphens
                if not re.match(r"^[A-Za-z\s'-]+$", name):
                        mb.showerror("Error", "Full Name must contain only letters, spaces, hyphens (-), or apostrophes (').")
                        return
                if len(name) < 2:
                        mb.showerror("Error", "Full Name must be at least 2 characters long.")
                        return

                # 🔸 Phone Number Validation
                if not phone:
                        mb.showerror("Error", "Phone Number is required.")
                        return
                # Accept formats like +911234567890 or 1234567890
                if not re.match(r"^\+?\d{10,15}$", phone):
                        mb.showerror("Error", "Phone Number must be 10-15 digits, optionally starting with '+'.")
                        return

                # 🔸 Email Validation
                if not email:
                        mb.showerror("Error", "Email is required.")
                        return
                # Basic email pattern: something@domain.com
                if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email):
                        mb.showerror("Error", "Enter a valid email address.")
                        return
                
                # 🔸 Username validation
                if not username:
                        mb.showerror("Error", "Username is required.")
                        return
                if len(username) < 4:
                        mb.showerror("Error", "Username must be at least 4 characters long.")
                        return
                if not re.match(r'^[A-Za-z0-9_]+$', username):
                        mb.showerror("Error", "Username can only contain letters, numbers, and underscores (_). No spaces or symbols.")
                        return

                # 🔸 Password validation
                if not password:
                        mb.showerror("Error", "Password is required.")
                        return
                if len(password) < 8:
                        mb.showerror("Error", "Password must be at least 8 characters long.")
                        return
                if ' ' in password:
                        mb.showerror("Error", "Password cannot contain spaces.")
                        return
                if not re.search(r'[A-Z]', password):
                        mb.showerror("Error", "Password must contain at least one uppercase letter.")
                        return
                if not re.search(r'[a-z]', password):
                        mb.showerror("Error", "Password must contain at least one lowercase letter.")
                        return
                if not re.search(r'\d', password):
                        mb.showerror("Error", "Password must contain at least one digit.")
                        return
                if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                        mb.showerror("Error", "Password must contain at least one special character.")
                        return

                # 🔸 Confirm password
                if password != confirm:
                        mb.showerror("Error", "Passwords do not match.")
                        return
                
                # 🔹 Guests validation
                if guests <= 0:
                        mb.showerror("Error", "Guests must be greater than 0.")
                        return
                if room_type == "Single" and guests > 1:
                        mb.showerror("Error", "Only 1 guest allowed for Single room.")
                        return
                if room_type == "Double" and guests > 2:
                        mb.showerror("Error", "Only 2 guests allowed for Double room.")
                        return

                # 🔹 Date format and logic validation
                try:
                        checkin_date = datetime.strptime(Checkin, "%d/%m/%Y")
                        checkout_date = datetime.strptime(Checkout, "%d/%m/%Y")
                        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

                        if checkin_date < today:
                                mb.showerror("Invalid Date", "Check-in date cannot be in the past.")
                        elif checkout_date <= checkin_date:
                                mb.showerror("Invalid Date", "Check-out date must be after check-in date.")
                        else:
                                mb.showinfo("Valid Dates", "Dates are valid!")
                except ValueError:
                        mb.showerror("Format Error", "Dates must be in DD/MM/YYYY format.")

                # 🔹 Room and location validation
                if room_type not in ["Single", "Double", "Suite"]:
                        mb.showerror("Error", "Invalid room type selected.")
                        return
                if location not in ["Delhi", "Mumbai", "Chennai", "Kolkata"]:
                        mb.showerror("Error", "Invalid location selected.")
                        return

                # 🔹 Special request validation
                if len(special) > 250:
                        mb.showerror("Error", "Special request must be under 250 characters.")
                        return
                if re.search(r'<script>|</script>|<.*?>', special, re.IGNORECASE):
                        mb.showerror("Error", "Special request contains unsafe text.")
                        return


                # ✅ If everything is valid
                mb.showinfo("Success", "All details are valid!")
                        

        frame2 = tk.LabelFrame(form, text="BOOKING DETAILS", bg="#fdd36e",padx=58, pady=25, font=("Bahnschrift", 10, 'bold', 'underline'),bd=3, relief=tk.SUNKEN)
        frame2.place(x=50, y=180)

        UsernameL = ttk.Label(frame2, text="UserName : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        UsernameL.grid(row=0, column=0, sticky='w')
        UsernameE = ttk.Entry(frame2,width=20,font=('Consolas', 10),background='black')
        UsernameE.grid(row=0, column=1)

        PasswordL = ttk.Label(frame2, text="Password : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        PasswordL.grid(row=1, column=0, sticky='w')
        PasswordE = ttk.Entry(frame2,width=20,font=('Consolas', 10),background='black',show="*")
        PasswordE.grid(row=1, column=1)
        
        PassConfirmL = ttk.Label(frame2, text="Confirmation  : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        PassConfirmL.grid(row=2, column=0, sticky='w')
        PassConfirmE = ttk.Entry(frame2,width=20,font=('Consolas', 10),background='black', show="*")
        PassConfirmE.grid(row=2, column=1)

        def selectsound():
                winsound.PlaySound("select.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        def toggle_password():
                if show_pass.get():
                        PasswordE.config(show='')
                        PassConfirmE.config(show='')
                else:
                        PasswordE.config(show='*')
                        PassConfirmE.config(show='*')
        show_pass = BooleanVar()
        show_passcon = Checkbutton(frame2, text="Show Password", variable=show_pass, command=lambda:[toggle_password(),selectsound()], bg='#fdd36e', fg='black',font=("Bahnschrift", 10, 'bold',))
        show_passcon.place(x=110, y=70)

        

        frame3 = tk.LabelFrame(form, text="ACCOUNT DETAILS", bg="#fdd36e",padx=35, pady=20, font=("Bahnschrift", 10, 'bold', 'underline'),bd=3, relief=tk.SUNKEN)
        frame3.place(x=50, y=330)

        GuestL = ttk.Label(frame3, text="Number of Guests : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        GuestL.grid(row=0, column=0, sticky='w')
        GuestE = ttk.Spinbox(frame3, from_=1, to=10,width=20,font=('Consolas', 10))
        GuestE.grid(row=0, column=1)

        CheckInL = ttk.Label(frame3, text="Check In Date : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        CheckInL.grid(row=1, column=0, sticky='w')
        CheckInE = DateEntry(frame3, date_pattern='dd/mm/yyyy',width=19,font=('Consolas', 10))
        CheckInE.grid(row=1, column=1)

        CheckOutL = ttk.Label(frame3, text="Check Out Date : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        CheckOutL.grid(row=2, column=0, sticky='w')
        CheckOutE = DateEntry(frame3, date_pattern='dd/mm/yyyy',width=19,font=('Consolas', 10))
        CheckOutE.grid(row=2, column=1)

        RoomTypeL = ttk.Label(frame3, text="Room Type : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        RoomTypeL.grid(row=3, column=0, sticky='w')
        RoomType = ttk.Combobox(frame3,values=["Single","Double","Suite"],width=19,state="readonly",font=('Consolas', 10))
        RoomType.current(0)
        RoomType.grid(row=3, column=1)

        LocationL = ttk.Label(frame3, text="Location : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        LocationL.grid(row=4, column=0, sticky='w')
        Location = ttk.Combobox(frame3,values=["Delhi","Mumbai","Bangalore","Hyderabad","Kolkata","Chennai","Ahmedabad","Pune"],width=19,state="readonly",font=('Consolas', 10))
        Location.current(0)
        Location.grid(row=4, column=1)

        SpecialReqL = ttk.Label(frame3, text="Special Request : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        SpecialReqL.grid(row=5, column=0, sticky='w')
        SpecialReq = tk.Text(frame3, width=19, height=4)
        SpecialReq.grid(row=5, column=1)

        def on_enter(e):
                submitBTN['background'] = 'green'  
                submitBTN['foreground'] = 'white'

        def on_leave(e):
                submitBTN['background'] = 'orange'       
                submitBTN['foreground'] = 'black'

        
        submitBTN = tk.Button(form, 
                        text='SUBMIT BOOKING',
                        font=('Bahnschrift SemiBold', 10, 'bold'),
                        bg='orange',  
                        fg='black',
                        activebackground='dark green',
                        activeforeground='white',
                        relief='raised',
                        borderwidth=3,
                        padx=10,
                        pady=5,
                        cursor='hand2',
                        command=validate_form)
        submitBTN.bind("<Enter>", on_enter)
        submitBTN.bind("<Leave>", on_leave)
        submitBTN.place(x=500, y=40)

        def on_enter(e):
                ResetBTN['background'] = 'blue'  
                ResetBTN['foreground'] = 'white'

        def on_leave(e):
                ResetBTN['background'] = 'orange'       
                ResetBTN['foreground'] = 'black'

        ResetBTN = tk.Button(form, 
                        text='CLEAR ALL',
                        font=('Bahnschrift SemiBold', 10, 'bold'),
                        bg='orange',  
                        fg='black',
                        activebackground='dark green',
                        activeforeground='white',
                        relief='raised',
                        borderwidth=3,
                        padx=10,
                        pady=5,
                        cursor='hand2',
                        command=clear_all_fields)
        ResetBTN.bind("<Enter>", on_enter)
        ResetBTN.bind("<Leave>", on_leave)
        ResetBTN.place(x=650, y=40)

        def on_enter(e):
                HomeBTN['background'] = 'red'  
                HomeBTN['foreground'] = 'white'

        def on_leave(e):
                HomeBTN['background'] = 'orange'       
                HomeBTN['foreground'] = 'black'

        HomeBTN = tk.Button(form, 
                        text='HOME',
                        font=('Bahnschrift SemiBold', 10, 'bold'),
                        bg='orange',  
                        fg='black',
                        activebackground='dark green',
                        activeforeground='white',
                        relief='raised',
                        borderwidth=3,
                        padx=10,
                        pady=5,
                        cursor='hand2',
                        command=lambda: [click_sound()])
        HomeBTN.bind("<Enter>", on_enter)
        HomeBTN.bind("<Leave>", on_leave)
        HomeBTN.place(x=765, y=40)
        form.mainloop()    
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
start_button = ttk.Button(entrance, text="START BOOKING",style='TButton',command=open_booking_form)

start_button.place(x=650, y=425)
entrance.mainloop()