import datetime
from datetime import datetime  
import os
from stat import filemode
import time
import tkinter as tk
from tkinter import END, BooleanVar, Checkbutton, ttk
from tkinter import filedialog
import PIL 
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import winsound
from tkinter import messagebox as mb
import re
import first
import threading
from tkinter import Toplevel, PhotoImage
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import textwrap
import random
from reportlab.lib.units import inch
import qrcode


payment_done = False
booking_id = f"WY{random.randint(100000, 999999)}"


def Form():
        def click_sound():
                winsound.PlaySound("click.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        click_sound()
        form = tk.Tk()
        form.title("WOYO BOOKING FORM")
        form.geometry("1100x800+50+20")
        form.resizable(0,0)
        form.configure(background='#fdd36e')

        def backtohome():
                click_sound()
                orm.destroy()
                first.Entrance()

        imgf = Image.open("form.png")
        imgf = imgf.resize((650,800))
        logo = ImageTk.PhotoImage(imgf)
        logo_label = tk.Label(form, image=logo, border=0)
        logo_label.place(x=470, y=-1)



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

                CardNumE.delete(0, tk.END)
                ExpiryDateE.delete(0, tk.END)
                CvvE.delete(0, tk.END)
        def validate_payment():
                card = CardNumE.get().strip()
                expiry = ExpiryDateE.get().strip()
                cvv = CvvE.get().strip()
                method = payment_method.get()

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
        def handle_payment():
                 if validate_payment():
                        # Simulated payment success action
                        qr_window = Toplevel()
                        qr_window.title("Scan to Pay")
                        qr_window.geometry("400x550")
                        qr_window.resizable(0,0)
                        qr_window.configure(bg="black")

                        # Add label
                        tk.Label(qr_window, text="Scan this QR to Pay", font=("Bahnschrift SemiBold", 14), fg="white",bg="black").pack(pady=10)

                        # Load and display QR image
                        qr_img = PhotoImage(file="qr.png")  # Make sure 'qr.png' is in the same folder
                        qr_label = tk.Label(qr_window, image=qr_img, bg="black")
                        qr_label.image = qr_img  # Keep a reference to avoid garbage collection
                        qr_label.pack(pady=5)

                        # Add a fake payment complete button
                        def close_after_payment():
                                global  payment_done
                                payment_done = True
                                mb.showinfo("Payment Confirmed", "You may now submit your booking.")
                                qr_window.destroy()

                        tk.Button(qr_window, text="I Have Paid", command=close_after_payment, bg="green", fg="white", font=("Bahnschrift", 10, "bold")).pack(pady=15)
                        winsound.MessageBeep()

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
                                return
                        elif checkout_date <= checkin_date:
                                mb.showerror("Invalid Date", "Check-out date must be after check-in date.")
                                return
                except ValueError:
                        mb.showerror("Format Error", "Dates must be in DD/MM/YYYY format.")
                        return

                # 🔹 Room and location validation
                if room_type not in ["Single", "Double", "Suite"]:
                        mb.showerror("Error", "Invalid room type selected.")
                        return
                

                # 🔹 Special request validation
                if len(special) > 250:
                        mb.showerror("Error", "Special request must be under 250 characters.")
                        return
                if re.search(r'<script>|</script>|<.*?>', special, re.IGNORECASE):
                        mb.showerror("Error", "Special request contains unsafe text.")
                        return
                global payment_done
                # 🔹 Payment check
                if not payment_done:
                        mb.showwarning("Payment Required", "Please complete the payment before submitting the booking.")
                        return

                # ✅ If everything is valid and payment is done
                mb.showinfo("Success", "All details are valid and payment is completed!")
                mb.showinfo("Booking Confirmed", f"Booking ID: {booking_id}\nSaved Successfully!")


                # 👉 Show booking summary window
                show_booking_summary()

                        

        frame2 = tk.LabelFrame(form, text="BOOKING DETAILS", bg="#fdd36e",padx=58, pady=25, font=("Bahnschrift", 10, 'bold', 'underline'),bd=3, relief=tk.SUNKEN)
        frame2.place(x=50, y=150)

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
        frame3.place(x=50, y=290)

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

        def generate_qr_code(data):
                import qrcode
                from PIL import Image
                qr = qrcode.QRCode(version=1, box_size=8, border=2)
                qr.add_data(data)
                qr.make(fit=True)
                img = qr.make_image(fill_color='black', back_color='white')
                return img



        def show_booking_summary():
                # 1. Gather data & ID
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
                booking_id = f"BK{random.randint(10000,99999)}"

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

                # 2. Create window
                summaryWin = tk.Toplevel()
                summaryWin.title("Booking Summary")
                summaryWin.geometry("500x650+600+20")
                summaryWin.configure(bg="grey")

                # 3. Content frame
                content = tk.Frame(summaryWin, bg="grey", padx=20, pady=20, relief=tk.SUNKEN)
                content.pack(fill="both", expand=True)

                # Title
                tk.Label(content,
                        text="Your Booking Details",
                        font=("Consolas",20,"bold","underline"),
                        fg="white", bg="grey")\
                .pack(pady=(0,20))

                # Summary text
                txt = tk.Text(content, wrap="word", font=("Consolas",10,"bold"),
                                bg="white", height=15)
                txt.insert("1.0", data)
                txt.config(state="disabled")
                txt.pack(fill="both", expand=False)

                lines = [line.strip() for line in data.splitlines() if line.strip()]
                clean_data = "\n".join(lines)

                    # 1) Build a compact payload with all key details + your new lines
                payload_lines = [
                        f"Booking ID: {booking_id}",
                        f"Name: {full_name}",
                        f"Phone: {phone}",
                        f"Email: {email}",
                        f"Username: {username}",
                        f"Room: {room_type}",
                        f"Check-in: {check_in}",
                        f"Check-out: {check_out}",
                        f"Guests: {guests}",
                        f"Location: {location}",                         # added
                        f"Request: {special_req}",                       # added
                        "Thank you for choosing WOYO!",                  # added
                        "We look forward to welcoming you soon.",        # added
                        "Have a wonderful day!"                          # added
                ]
                qr_payload = "\n".join(payload_lines)

                # 2) Generate a small, high-error-resilience QR
                qr = qrcode.QRCode(
                        version=None,
                        error_correction=qrcode.constants.ERROR_CORRECT_M,
                        box_size=8,
                        border=4,
                )
                qr.add_data(qr_payload)
                qr.make(fit=True)
                qr_img = qr.make_image(fill_color="black", back_color="white")

                # 3) Resize it for display clarity
                qr_img = qr_img.resize((180, 180), Image.LANCZOS)
                qr_photo = ImageTk.PhotoImage(qr_img)

                # 4) Show it in your summary window
                qr_label = tk.Label(summaryWin, image=qr_photo, bg="grey")
                qr_label.image = qr_photo   # keep reference alive
                qr_label.pack(pady=10)

                tk.Label(summaryWin,
                        text="Scan for key booking details",
                        font=("Consolas", 9),
                        bg="grey", fg="white"
                ).pack()


                # 5. Button frame
                btn_frame = tk.Frame(summaryWin, bg="grey", pady=20)
                btn_frame.pack(fill="x")

                tk.Button(btn_frame, text="Save to PDF", bg="green", fg="white",
                        font=("Consolas",10,"bold"),
                        command=lambda: saveToPdf(data, booking_id))\
                .pack(side="left", padx=10, expand=True)

                tk.Button(btn_frame, text="Save to Text File", bg="blue", fg="white",
                        font=("Consolas",10,"bold"),
                        command=lambda: save_to_text(data, booking_id))\
                .pack(side="right", padx=10, expand=True)

        def saveToPdf(data, booking_id):
                try:
                        # Ask user where to save the PDF file
                        file_path = filedialog.asksaveasfilename(
                                defaultextension=".pdf",
                                filetypes=[("PDF files", "*.pdf")],
                                initialfile=f"Booking_{booking_id}.pdf",
                                title="Save Booking as PDF"
                        )

                        if not file_path:  # If user cancels the save dialog
                                return

                        # Create PDF
                        c = canvas.Canvas(file_path, pagesize=A4)
                        c.setFont("Courier", 12)

                        # Define margins
                        left_margin = 1 * inch
                        y = 750  # Start from top of page

                        # Add a title
                        c.setFont("Helvetica-Bold", 16)
                        c.drawString(left_margin, y, "Booking Summary")
                        y -= 30

                        # Reset to regular font
                        c.setFont("Courier", 12)

                        # Process each line
                        for line in data.split('\n'):
                                if not line.strip():
                                        y -= 15
                                        continue

                        # Check if this is a special request line
                                if "Special Req" in line:
                                        parts = line.split(":", 1)
                                        if len(parts) == 2:
                                                label = parts[0].strip() + ":"
                                                content = parts[1].strip()

                                # Draw label
                                        c.drawString(left_margin, y, label)
                                        y -= 15

                                # Wrap and draw content with indentation
                                        wrapped_lines = textwrap.wrap(content, width=80)
                                        for wrap_line in wrapped_lines:
                                                c.drawString(left_margin + 20, y, wrap_line)
                                                y -= 15
                                else:
                                        c.drawString(left_margin, y, line)
                                        y -= 15
                        else:
                                c.drawString(left_margin, y, line)
                                y -= 15

                        # Page break if near bottom
                        if y < 50:
                                c.showPage()
                                c.setFont("Courier", 12)
                                y = 750

                        c.save()
                        mb.showinfo("Success", "Booking saved to PDF successfully!")

                except Exception as e:
                        mb.showerror("PDF Error", f"Could not save to PDF:\n{e}")

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
                        
                                mb.showinfo("Success", "Booking saved to text file successfully!")
                        
                except Exception as e:
                        mb.showerror("Text File Error", f"Could not save to text file:\n{e}")
        
        frame4 = tk.LabelFrame(form, text="PAYMENT DETAILS", bg="#fdd36e",padx=41, pady=10, font=("Bahnschrift", 10, 'bold', 'underline'),bd=3, relief=tk.SUNKEN)
        frame4.place(x=50, y=535)
        
        
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
        
        CardNumL = tk.Label(frame4, text="Card/UPI Number:", bg="#fdd36e", font=("Consolas", 10, 'bold'))
        CardNumL.grid(row=3, column=0, sticky="w")
        CardNumE = tk.Entry(frame4, width=15)
        CardNumE.grid(row=3, column=1, padx=5)

        ExpiryDateL = tk.Label(frame4, text="Expiry Date (MM/YY):", bg="#fdd36e", font=("Consolas", 10, 'bold'))
        ExpiryDateL.grid(row=4, column=0, sticky="w")
        ExpiryDateE = tk.Entry(frame4, width=15)
        ExpiryDateE.grid(row=4, column=1,sticky="w", padx=5)

        CvvL = tk.Label(frame4, text="CVV:", bg="#fdd36e", font=("Consolas", 10, 'bold'))
        CvvL.grid(row=5, column=0, sticky="w")
        CvvE = tk.Entry(frame4, width=15, show="*")
        CvvE.grid(row=5, column=1,sticky="w", padx=5)

        
                
                        
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
                        command=backtohome)
        HomeBTN.bind("<Enter>", on_enter)
        HomeBTN.bind("<Leave>", on_leave)
        HomeBTN.place(x=765, y=40)
        
        form.mainloop()

        if __name__ == "__entrance__":
                entrance()