# This is the Form Page where all the main work is done
# Core Python
import datetime 
from datetime import datetime
import io  
from tkcalendar import DateEntry# Date/Time Operations Used For Check-In Check-Out Field
import re # Regular Expression for text Pattern Matching (E-mail Checking)

# GUI development
import tkinter as tk #Main Tkinter module
from tkinter import END,BooleanVar,Checkbutton,filedialog,ttk,Toplevel, PhotoImage # Tkinter components
import tkinter.filedialog as filedialog
from tkcalendar import DateEntry # Calendar widget for Dates

# Image Handling
from PIL import Image, ImageTk  #Image processing and Tkinter integration
import qrcode #QR code generation

# PDF generation
from reportlab.lib.pagesizes import A4 # Standard paper size
from reportlab.pdfgen import canvas # PDF creation
from reportlab.lib.units import inch # Measurement conversion
import textwrap # Text formattin for PDFs

# System/OS specific
import winsound # Windows sound effects

# Application modules
import first # Custom module (GUI entrance screen)
from tkinter import messagebox as mb # Pre-made Dialog boxes

# Misc
import random # Random Number Generation

payment_done = False
booking_id = f"WY{random.randint(100000, 999999)}"

# For Creating Click Sound When Clicked on Buttons
def click_sound():
                winsound.PlaySound("click.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
# For Show Password Click 
def selectsound():
                winsound.PlaySound("select.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

# Main Form Where All the Logic Behind Form's UI and Validation written
def Form():
        # Sound When Clicked 
        click_sound()

        # Starting of Window
        form = tk.Tk()
        form.title("WOYO BOOKING FORM")
        form.geometry("1100x800+50+20")
        form.resizable(0,0)
        form.configure(background='#fdd36e')

        # For Back Button
        def backtohome():
                click_sound()
                form.destroy()
                first.Entrance()
        
        # Image Used For Making Form More Attractive
        imgf = Image.open("form.png")
        imgf = imgf.resize((650,800))
        logo = ImageTk.PhotoImage(imgf)
        logo_label = tk.Label(form, image=logo, border=0)
        logo_label.place(x=470, y=-1)
        
        # Frame Used like a Box that Hold Related Fields
        formFrame = tk.LabelFrame(form, text="PERSONAL DETAILS", bg="#fdd36e",padx=54, pady=20, font=("Bahnschrift", 10, 'bold', 'underline'),bd=3, relief=tk.SUNKEN) 
        formFrame.place(x=50, y=20)

        # Fullname Field and Entry
        FullnameL = ttk.Label(formFrame, text="Full Name : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        FullnameL.grid(row=0, column=0, sticky='w') # w for west(left)
        FullnameE = ttk.Entry(formFrame,width=20,font=('Consolas', 10))
        FullnameE.grid(row=0, column=1) # Using Grid for Precise placement between Label and Entry

        # Phone Field and Entry
        PhoneL = ttk.Label(formFrame, text="Phone Number : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        PhoneL.grid(row=1, column=0, sticky='w')
        PhoneE = ttk.Entry(formFrame,width=20,font=('Consolas', 10))
        PhoneE.grid(row=1, column=1)

        # Email Field and Entry
        EmailL = ttk.Label(formFrame, text="E-Mail : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        EmailL.grid(row=2, column=0, sticky='w')
        EmailE = ttk.Entry(formFrame,width=20,font=('Consolas', 10))
        EmailE.grid(row=2, column=1)

        # This is Second Frame For Acount Details
        frame2 = tk.LabelFrame(form, text="ACOUNT DETAILS", bg="#fdd36e",padx=58, pady=25, font=("Bahnschrift", 10, 'bold', 'underline'),bd=3, relief=tk.SUNKEN)
        frame2.place(x=50, y=150)

        # UserName Field Label and Entry
        UsernameL = ttk.Label(frame2, text="UserName : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        UsernameL.grid(row=0, column=0, sticky='w')
        UsernameE = ttk.Entry(frame2,width=20,font=('Consolas', 10),background='black')
        UsernameE.grid(row=0, column=1)

        # Password Field Label and Entry
        PasswordL = ttk.Label(frame2, text="Password : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        PasswordL.grid(row=1, column=0, sticky='w')
        PasswordE = ttk.Entry(frame2,width=20,font=('Consolas', 10),background='black',show="*")
        PasswordE.grid(row=1, column=1)

        # Confirm Password Field Label and Entry
        PassConfirmL = ttk.Label(frame2, text="Confirmation  : ",font=('Bahnschrift SemiBold',12,'bold'),background='#fdd36e')
        PassConfirmL.grid(row=2, column=0, sticky='w')
        PassConfirmE = ttk.Entry(frame2,width=20,font=('Consolas', 10),background='black', show="*")
        PassConfirmE.grid(row=2, column=1)

        # Checkbox for Showing and Hidding Password 
        def toggle_password():
                if show_pass.get():
                        PasswordE.config(show='')
                        PassConfirmE.config(show='')
                else:
                        PasswordE.config(show='*')
                        PassConfirmE.config(show='*')
        
        # Checkbox of Show Password
        show_pass = BooleanVar()
        show_passE = Checkbutton(frame2, text="Show Password", variable=show_pass, command=lambda:[toggle_password(),selectsound()], bg='#fdd36e', fg='black',font=("Bahnschrift", 10, 'bold',))
        show_passE.place(x=110, y=70)
        
        # This is Third Frame for Hotel Booking Details
        frame3 = tk.LabelFrame(form, text="BOOKING DETAILS", bg="#fdd36e",padx=35, pady=20, font=("Bahnschrift", 10, 'bold', 'underline'),bd=3, relief=tk.SUNKEN)
        frame3.place(x=50, y=290)

        # Guest Field for Entering How many Members Live in Hotel
        GuestL = ttk.Label(frame3, text="Number of Guests : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        GuestL.grid(row=0, column=0, sticky='w')
        GuestE = ttk.Spinbox(frame3, from_=1, to=10,width=20,font=('Consolas', 10)) # Spinbox for Increasing and Decreasing Number
        GuestE.grid(row=0, column=1)

        # Check-In Date Field and Entry By Using DateEntry function That shows Calender for Selecting Calender
        CheckInL = ttk.Label(frame3, text="Check In Date : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        CheckInL.grid(row=1, column=0, sticky='w')
        CheckInE = DateEntry(frame3, date_pattern='dd/mm/yyyy',width=19,font=('Consolas', 10))
        CheckInE.grid(row=1, column=1)

        # Check-In Date Field and Entry By Using DateEntry function That shows Calender for Selecting Calender
        CheckOutL = ttk.Label(frame3, text="Check Out Date : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        CheckOutL.grid(row=2, column=0, sticky='w')
        CheckOutE = DateEntry(frame3, date_pattern='dd/mm/yyyy',width=19,font=('Consolas', 10))
        CheckOutE.grid(row=2, column=1)

        # RoomType Field and Entry Which is Using Combobox for Multiple List of Choices 
        RoomTypeL = ttk.Label(frame3, text="Room Type : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        RoomTypeL.grid(row=3, column=0, sticky='w')
        RoomType = ttk.Combobox(frame3,values=["Single","Double","Suite"],width=19,state="readonly",font=('Consolas', 10)) # Using State that Disable Editing text
        RoomType.current(0) # It will Show Data by using Index which is currently set it to 0(Single)
        RoomType.grid(row=3, column=1)

        # Location Field and Entry Same as RoomType
        LocationL = ttk.Label(frame3, text="Location : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        LocationL.grid(row=4, column=0, sticky='w')
        Location = ttk.Combobox(frame3,values=["Delhi","Mumbai","Bangalore","Hyderabad","Kolkata","Chennai","Ahmedabad","Pune"],width=19,state="readonly",font=('Consolas', 10))
        Location.current(0)
        Location.grid(row=4, column=1)

        # Special Request Field and Entry for User if they wants to Give some Message when ordering a Room
        SpecialReqL = ttk.Label(frame3, text="Special Request : ",font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        SpecialReqL.grid(row=5, column=0, sticky='w')
        SpecialReq = tk.Text(frame3, width=19, height=4) # Using Text field for Taking Input
        SpecialReq.grid(row=5, column=1)

        # These are all the Validation Which is used in Form so that User don't Enter any Wrong Data according to Field and Entry
        def validate_form():
                # All these will Get Values from Entries and Remove any Space for Checking Field is Empty or Not !
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
                special = SpecialReq.get("1.0", END).strip() # Start from line 1, character 0 Until the END of the text         

                # Here Starts the Validation Condition
                try:
                        guests = int(GuestE.get()) # For Checking Guest Field is Integer or not
                except ValueError:
                        mb.showerror("Error", "Number of Guests must be a numeric value.") # Using Messageboxes For Giving ERROR,WARNING and INFO
                        return

                # Full Name Validation
                if not name:
                        mb.showerror("Error", "Full Name is required.")
                        return
                
                # Allow letters, spaces, apostrophes, hyphens
                if not re.match(r"^[A-Za-z\s'-]+$", name): #Using Regular Expression
                        mb.showerror("Error", "Full Name must contain only letters, spaces, hyphens (-), or apostrophes (').")
                        return
                if len(name) < 2:
                        mb.showerror("Error", "Full Name must be at least 2 characters long.")
                        return

                # Phone Number Validation
                if not phone:
                        mb.showerror("Error", "Phone Number is required.")
                        return
                # Accept formats like +911234567890 or 1234567890
                if not re.match(r"^\+?\d{10,15}$", phone):
                        mb.showerror("Error", "Phone Number must be 10-15 digits, optionally starting with '+'.")
                        return

                # Email Validation
                if not email:
                        mb.showerror("Error", "Email is required.")
                        return
                
                # Basic email pattern: something@domain.com
                if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email):
                        mb.showerror("Error", "Enter a valid email address.")
                        return
                
                # Username validation
                if not username:
                        mb.showerror("Error", "Username is required.")
                        return
                if len(username) < 4:
                        mb.showerror("Error", "Username must be at least 4 characters long.")
                        return
                if not re.match(r'^[A-Za-z0-9_]+$', username):
                        mb.showerror("Error", "Username can only contain letters, numbers, and underscores (_). No spaces or symbols.")
                        return

                # Password validation
                if not password:
                        mb.showerror("Error", "Password is required.")
                        return
                if len(password) < 8:
                        mb.showerror("Error", "Password must be at least 8 characters long.")
                        return
                if ' ' in password:
                        mb.showerror("Error", "Password cannot contain spaces.")
                        return
                if not re.search(r'[A-Z]', password): # Using Search 
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

                # Confirm password
                if password != confirm:
                        mb.showerror("Error", "Passwords do not match.")
                        return
                
                # Guests validation
                if guests <= 0:
                        mb.showerror("Error", "Guests must be greater than 0.")
                        return
                if room_type == "Single" and guests > 1:
                        mb.showerror("Error", "Only 1 guest allowed for Single room.")
                        return
                if room_type == "Double" and guests > 2:
                        mb.showerror("Error", "Only 2 guests allowed for Double room.")
                        return

                # Date format and logic validation
                try:    
                        # Convert string dates to datetime objects
                        checkin_date = datetime.strptime(Checkin, "%d/%m/%Y")
                        checkout_date = datetime.strptime(Checkout, "%d/%m/%Y")

                        # Get today's date without time component
                        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

                        # Validate dates
                        if checkin_date < today:
                                mb.showerror("Invalid Date", "Check-in date cannot be in the past.")
                                return
                        elif checkout_date <= checkin_date:
                                mb.showerror("Invalid Date", "Check-out date must be after check-in date.")
                                return
                except ValueError:
                        # Handle format errors
                        mb.showerror("Format Error", "Dates must be in DD/MM/YYYY format.")
                        return

                # Special request validation
                if len(special) > 30:
                        mb.showerror("Error", "Special request must be under 30 characters.")
                        return
                # Check if special requests contain HTML/script tags (potential XSS attack)
                if re.search(r'<script>|</script>|<.*?>', special, re.IGNORECASE):
                        mb.showerror("Error", "Special request contains unsafe text.") # Show security warning
                        return # Exit function to prevent processing
                
                # Payment check
                global payment_done
                if not payment_done:
                        mb.showwarning("Payment Required", "Please complete the payment before submitting the booking.")
                        return

                # If everything is valid and payment is done
                mb.showinfo("Success", "All details are valid and payment is completed!")
                mb.showinfo("Booking Confirmed", f"Booking ID: {booking_id}\nSaved Successfully!")

                # Show booking summary window
                show_booking_summary()
        # For Generating QR of BOOKING SUMMARY when BOOKING is Completed
        def generate_booking_qr(booking_details, display_frame):
        
                # Clear any existing widgets in the frame
                for widget in display_frame.winfo_children():
                        widget.destroy()
                        
                # Create a list containing formatted booking details for QR code payload
                payload_lines = [
                        f"Booking ID: {booking_details['booking_id']}",
                        f"Name: {booking_details['full_name']}",
                        f"Phone: {booking_details['phone']}",
                        f"Email: {booking_details['email']}",
                        f"Username: {booking_details['username']}",
                        f"Room: {booking_details['room_type']}",
                        f"Check-in: {booking_details['check_in']}",
                        f"Check-out: {booking_details['check_out']}",
                        f"Guests: {booking_details['guests']}",
                        f"Location: {booking_details['location']}",
                        f"Request: {booking_details['special_req']}",
                        "Thank you for choosing WOYO!",
                        "We look forward to welcoming you soon.",
                        "Have a wonderful day!"
                ]
                
                # Combine all lines into a single string with newline separators
                qr_payload = "\n".join(payload_lines)
                
                try:
                        # Configure QR code with optimized settings for reliability and scanning
                        qr = qrcode.QRCode(
                        version=None,  # Auto-select version based on data size
                        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction (30% recovery)
                        box_size=12,   # Each QR module = 10 pixels (larger for better scanning)
                        border=4       # 4-module quiet zone (white border)
                        )
                        
                        # Add the formatted booking data to QR code
                        qr.add_data(qr_payload)
                        
                        # Generate the QR pattern (auto-size to fit data)
                        qr.make(fit=True)
                        
                        # Create final image with high contrast colors
                        qr_img = qr.make_image(fill_color="black", back_color="white")
                        
                        # Resize QR code for optimal display (240x240 pixels for better resolution)
                        qr_img = qr_img.resize((240, 240), Image.LANCZOS)
                        
                        # Convert to Tkinter-compatible format
                        # We use a BytesIO buffer to avoid potential reference issues
                        buffer = io.BytesIO()
                        qr_img.save(buffer, format="PNG")
                        buffer.seek(0)
                        
                        # Load from buffer to ensure image data stays in memory
                        pil_img = Image.open(buffer)
                        qr_photo = ImageTk.PhotoImage(pil_img)
                        
                        # Create a label and place QR code in it
                        qr_label = tk.Label(display_frame, image=qr_photo, bg="white")
                        qr_label.image = qr_photo  # Keep a reference to prevent garbage collection
                        qr_label.pack(pady=10)
                        
                        # Text at Bottom of QR code
                        label_text = tk.Label(
                        display_frame,
                        text="Scan for key booking details",
                        font=("Consolas", 10, "bold"),
                        bg=display_frame.cget("bg"), 
                        fg="white"
                        )
                        label_text.pack()
                        
                        return True
                except Exception as e:
                        # Error handling
                        error_label = tk.Label(
                        display_frame,
                        text=f"Error generating QR code: {str(e)}",
                        font=("Consolas", 10),
                        fg="red",
                        bg=display_frame.cget("bg")
                        )
                        error_label.pack(pady=10)
                        return False
        
        # This Will Show All the Data on the New Window in Formatted way 
        def show_booking_summary():

                # 1. Gather data & ID from Entry field
                full_name = FullnameE.get().strip()
                phone = PhoneE.get().strip()
                email = EmailE.get().strip()
                username = UsernameE.get().strip()
                guests = GuestE.get()
                room_type = RoomType.get()
                location = Location.get()
                check_in = CheckInE.get()
                check_out = CheckOutE.get()
                special_req = SpecialReq.get("1.0", tk.END).strip()
                booking_id = f"BK{random.randint(10000,99999)}" # This is for Generating Random Booking ID

                # Create a multi-line formatted string with booking details
                data = f"""
                Booking Summary:
                Name          : {full_name}
                Phone         : {phone}
                Email         : {email}
                UserName      : {username}
                Guests        : {guests}
                Room Type     : {room_type}
                Location      : {location}
                Check-In      : {check_in}
                Check-Out     : {check_out}
                Special Req   : {special_req}
                Booking ID    : {booking_id}
                """

                # Create a new popup window for booking summary
                summaryWin = tk.Toplevel() # Create child window
                summaryWin.title("Booking Summary") 
                summaryWin.geometry("700x750+600+20")
                summaryWin.configure(bg="grey")

                # Create a container frame inside the summary window
                content = tk.Frame(summaryWin, bg="grey", padx=20, pady=20, relief=tk.SUNKEN)
                # Pack the frame to fill and expand in window
                content.pack(fill="both", # Expand to fill both horizontal and vertical space
                             expand=True) # Allow frame to grow if window is resized

                # Title
                tk.Label(content,
                        text="Your Booking Details",
                        font=("Consolas",20,"bold","underline"),
                        fg="white", bg="grey")\
                .pack(pady=(0,20))

                # Create a read-only text widget to display booking summary
                txt = tk.Text(content,
                              wrap="word", # Wrap text at word boundaries
                              font=("Consolas",
                                    10,"bold"),
                                bg="white", height=15)
                # Insert the booking data at the start ("1.0" position)
                txt.insert("1.0", data)
                # Disable editing to make it read-only
                txt.config(state="disabled")
                # Pack the text widget with minimal expansion
                txt.pack(fill="both", expand=False)

                # Process the multi-line booking data to remove empty lines and extra spaces
                lines = [line.strip() for line in data.splitlines() if line.strip()]
                # 1. splitlines() - Splits the string into a list of lines
                # 2. if line.strip() - Filters out empty/whitespace-only lines
                # 3. line.strip() - Removes leading/trailing spaces from each line
                clean_data = "\n".join(lines)
                # Joins the processed lines back together with newline characters
                # Result is clean data with:
                # - No empty lines
                # - No extra whitespace at start/end of lines
                # - Preserved line breaks for formatting

                booking_details = {
                        'booking_id': booking_id,
                        'full_name': full_name,
                        'phone': phone,
                        'email': email,
                        'username': username,
                        'room_type': room_type,
                        'check_in': check_in,
                        'check_out': check_out,
                        'guests': guests,
                        'location': location,
                        'special_req': special_req
                }
                
                # Create a frame for QR code
                qr_frame = tk.Frame(summaryWin, bg="grey", bd=2, relief=tk.GROOVE)
                qr_frame.pack(pady=15, padx=10)
                
                # Generate and display QR code
                generate_booking_qr(booking_details, qr_frame)
                
                # 5. Button frame
                btn_frame = tk.Frame(summaryWin, bg="grey", pady=20)
                btn_frame.pack(fill="x")

                # Button For Save to PDF so that user Save Summary File as PDF in 
                tk.Button(btn_frame, text="Save to PDF", bg="green", fg="white",
                        font=("Consolas",10,"bold"),
                        # Calls save function with current data
                        # lambda : preserves current data when clicked
                        command=lambda: save_to_pdf(data, booking_id))\
                .pack(side="left", padx=10, expand=True) # Allows button to grow if needed

                # Same Button But it's for Saving File as Text format
                tk.Button(btn_frame, text="Save to Text File", bg="blue", fg="white",
                        font=("Consolas",10,"bold"),
                        command=lambda: save_to_text(data, booking_id))\
                .pack(side="right", padx=10, expand=True)

        # This is for Saving all the Booking Summary Data into a PDF file so that user can save that file
        def save_to_pdf(data, booking_id):
                
                try:
                        # Ask user where to save the PDF file
                        file_path = filedialog.asksaveasfilename(
                                defaultextension=".pdf",  # Auto-adds .pdf if not typed
                                filetypes=[("PDF files", "*.pdf")],  # Only shows PDF files in dialog
                                initialfile=f"Booking_{booking_id}.pdf",  # Suggested filename with booking ID
                                title="Save Booking as PDF"
                        )
                        
                        if not file_path:  # If user cancels the save dialog
                                return
                        
                        # Create PDF
                        c = canvas.Canvas(file_path, pagesize=A4)
                        
                        # Define margins and starting position
                        left_margin = 1 * inch
                        y = 750  # Start from top of page
                        
                        # Add a title
                        c.setFont("Helvetica-Bold", 16)
                        c.drawString(left_margin, y, "Booking Summary")
                        y -= 30
                        
                        # Reset to regular font
                        c.setFont("Courier", 12)
                        
                        # Process each line of data
                        for line in data.split('\n'):
                        # Skip empty lines with a smaller space
                                if not line.strip():
                                        y -= 15
                                        continue
                                
                        # Check if we need a new page
                                if y < 50:
                                        c.showPage()
                                        c.setFont("Courier", 12)
                                        y = 750
                        
                        # Special handling for "Special Req" lines
                                if "Special Req" in line:
                                # Split the line at first colon only
                                        parts = line.split(":", 1)
                                
                                        if len(parts) == 2:
                                                label = parts[0].strip() + ":"
                                                content = parts[1].strip()
                                
                                # Draw the label
                                                c.drawString(left_margin, y, label)
                                                y -= 15
                                
                                # Handle text wrapping for long special requests
                                                wrapped_lines = textwrap.wrap(content, width=80)
                                                for wrap_line in wrapped_lines:
                                        # Check if we need a new page within wrapped text
                                                        if y < 50:
                                                                c.showPage()
                                                                c.setFont("Courier", 12)
                                                                y = 750
                                        
                                                        c.drawString(left_margin + 20, y, wrap_line)  # Indent wrapped lines
                                                        y -= 15
                                        else:
                                # Handle case where splitting didn't work as expected
                                                c.drawString(left_margin, y, line)
                                                y -= 15
                                else:
                                # Regular line formatting
                                        c.drawString(left_margin, y, line)
                                        y -= 15
                        
                        # Finalize and save the PDF document
                        c.save()
                        mb.showinfo("Success", "Booking Saved to PDF Successfully!")
                        
                except Exception as e:
                        mb.showerror("PDF Error", f"Could not save to PDF:\n{e}")
        # This is for Saving Booking Summary as Text file
        def save_to_text(data, booking_id):
                try:
                        # Ask user where to save the text file
                        file_path = filedialog.asksaveasfilename(
                        defaultextension=".txt",
                        filetypes=[("Text files", "*.txt")],
                        initialfile=f"Booking_{booking_id}.txt",
                        title="Save Booking as Text"
                        )
                        
                        if not file_path:  # If user cancels the save dialog
                                return
                        
                        # Write data to the file
                        with open(file_path, "w", encoding="utf-8") as f:
                                f.write(data)
                        
                                mb.showinfo("Success", "Booking Saved to Text File Successfully!")
                        
                except Exception as e:
                        mb.showerror("Text File Error", f"Could not save to text file:\n{e}")

        # This is fourth Frame for Payment Details 
        frame4 = tk.LabelFrame(form, text="PAYMENT DETAILS", bg="#fdd36e",padx=41, pady=10, font=("Bahnschrift", 10, 'bold', 'underline'),bd=3, relief=tk.SUNKEN)
        frame4.place(x=50, y=535)
        
        # Selecting Payment method Label
        CreditCardL = ttk.Label(frame4,text="Select Payment Method : ", font=("Bahnschrift SemiBold", 12, "bold"),background='#fdd36e')
        CreditCardL.grid(row=0, column=0, sticky='w')
        
        # Create a single variable for all payment method radio buttons
        payment_method = tk.StringVar(value="Credit Card")

        # All payment methods in a single list
        methods = ["Credit Card", "Debit Card", "UPI", "Net Banking"]
        tk.Radiobutton(frame4, text=methods[0], variable=payment_method, value=methods[0],
               bg="#fdd36e", font=("Consolas", 10, 'bold')).grid(row=1, column=0, sticky="w", padx=(0, 20))

        tk.Radiobutton(frame4, text=methods[1], variable=payment_method, value=methods[1],
                bg="#fdd36e", font=("Consolas", 10, 'bold')).grid(row=1, column=1, sticky="w")

        tk.Radiobutton(frame4, text=methods[2], variable=payment_method, value=methods[2],
                bg="#fdd36e", font=("Consolas", 10, 'bold')).grid(row=2, column=0, sticky="w", padx=(0, 20))

        tk.Radiobutton(frame4, text=methods[3], variable=payment_method, value=methods[3],
                bg="#fdd36e", font=("Consolas", 10, 'bold')).grid(row=2, column=1, sticky="w")
        
        # Card Number Field Label and Entry
        CardNumL = tk.Label(frame4, text="Card/UPI Number:", bg="#fdd36e", font=("Consolas", 10, 'bold'))
        CardNumL.grid(row=3, column=0, sticky="w")
        CardNumE = tk.Entry(frame4, width=15)
        CardNumE.grid(row=3, column=1, padx=5)

        # Expiry Date Field Label and Entry
        ExpiryDateL = tk.Label(frame4, text="Expiry Date (MM/YY):", bg="#fdd36e", font=("Consolas", 10, 'bold'))
        ExpiryDateL.grid(row=4, column=0, sticky="w")
        ExpiryDateE = tk.Entry(frame4, width=15)
        ExpiryDateE.grid(row=4, column=1,sticky="w", padx=5)

        # CVV Field Label and Entry
        CvvL = tk.Label(frame4, text="CVV:", bg="#fdd36e", font=("Consolas", 10, 'bold'))
        CvvL.grid(row=5, column=0, sticky="w")
        CvvE = tk.Entry(frame4, width=15, show="*")
        CvvE.grid(row=5, column=1,sticky="w", padx=5)
        
        # This is for Button That Clear All Entry fields when Clicked on it
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
            
            # Clear Payment Details
            CardNumE.delete(0, tk.END)
            ExpiryDateE.delete(0, tk.END)
            CvvE.delete(0, tk.END)   
                
        # This Will Check Payment Entry Fields Validation
        def validate_payment():
            card = CardNumE.get().strip()
            expiry = ExpiryDateE.get().strip()
            cvv = CvvE.get().strip()

            if not card or not expiry or not cvv:
                    mb.showerror("Validation Error", "All payment fields are required.")
                    return False

            if not card.isdigit() or len(card) < 8 or len(card) > 16:
                    mb.showerror("Validation Error", "Card/UPI number must be 8 to 16 digits.")
                    return False

            if len(cvv) != 3 or not cvv.isdigit():
                    mb.showerror("Validation Error", "CVV must be a 3-digit number.")
                    return False

            if '/' not in expiry or len(expiry) != 5:
                    mb.showerror("Validation Error", "Expiry must be in MM/YY format.")
                    return False
            return True
        # This is the Payment Window it will Open when We will CLick on Make Payment Button then it will show QR code for Payment
        def handle_payment():
                 # It will Check that If all the Validation is Satisfied or not 
                 # If not so it will not procced
                 if validate_payment():
                        # Simulated payment success action
                        qr_window = Toplevel()
                        qr_window.title("Scan to Pay")
                        qr_window.geometry("400x550")
                        qr_window.resizable(0,0)
                        qr_window.configure(bg="black")

                        # Text label
                        tk.Label(qr_window, text="Scan this QR to Pay", font=("Bahnschrift SemiBold", 14), fg="white",bg="black").pack(pady=10)

                        # Load and display QR image
                        qr_img = PhotoImage(file="qr.png")
                        qr_label = tk.Label(qr_window, image=qr_img, bg="black")
                        qr_label.image = qr_img  # Keep a reference to avoid garbage collection
                        qr_label.pack(pady=5)

                        # This is a fake payment complete message show up when clicked on button
                        def close_after_payment():
                                global  payment_done
                                payment_done = True
                                mb.showinfo("Payment Confirmed", "Now You Can Submit Your Booking.")
                                qr_window.destroy()

                        # Button for Completing payment step so that Booking will submit
                        tk.Button(qr_window, text="I Have Paid", command=close_after_payment, bg="green", fg="white", font=("Bahnschrift", 10, "bold")).pack(pady=15)
                        winsound.MessageBeep()
        # Button for Opening QR code and Make the Payment Step Complete     
        MakePaymentBTN = tk.Button(form,
                text="MAKE PAYMENT",
                font=('Bahnschrift SemiBold', 10, 'bold'),
                bg='green',
                fg='white',
                activebackground='dark green',
                activeforeground='white',
                relief='raised',
                borderwidth=3,
                padx=10,
                pady=5,
                cursor='hand2',
                command=lambda: handle_payment())
        MakePaymentBTN.place(x=180, y=720)
        
        # This is Hover Effect
        def on_enter(e):
                submitBTN['background'] = 'green'  
                submitBTN['foreground'] = 'white'

        def on_leave(e):
                submitBTN['background'] = 'orange'       
                submitBTN['foreground'] = 'black'

        # Submit Booking Button When Every Validation Is complete so It will Open Summary Window to show Data
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
        # Button for Clearing All Entries in the form so that User can Enter New Data or it's is just a Easy way to do it
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
        # Button for Returning Home at Entrance Screen 
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
                        command=backtohome)
        HomeBTN.bind("<Enter>", on_enter)
        HomeBTN.bind("<Leave>", on_leave)
        HomeBTN.place(x=765, y=40)
        
        form.mainloop()

        if __name__ == "__entrance__":
                first()