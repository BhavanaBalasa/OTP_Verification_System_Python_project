import random
import tkinter as tk
from PIL import Image, ImageTk
import yagmail
from tkinter import messagebox
import datetime

class OTPApp:
    def __init__(self):
        # Initialize variables
        self.otp = None
        self.attempts = 3
        self.otp_sent_time = None

        # Main window
        self.window = tk.Tk()
        self.window.geometry("800x500+400+150")
        self.window.configure(bg="#E0F7FA")
        self.window.resizable(False, False)
        self.setup_main_window()

    def setup_main_window(self):
        """Setup the main window UI for email input."""
        try:
            image = Image.open("email.png")
            resize_image = image.resize((80, 80))
            photo = ImageTk.PhotoImage(resize_image)
            image_label = tk.Label(self.window, image=photo)
            image_label.image = photo
            image_label.place(x=350, y=50)
        except FileNotFoundError:
            messagebox.showerror("Error", "Image file 'email.png' not found.")
            return

        text_label = tk.Label(self.window, text="Email ID Verification...", font=("Arial", 14))
        text_label.place(x=310, y=150)

        email_label = tk.Label(self.window, text="Email ID ", font=("Arial", 14), bg="#E0F7FA")
        email_label.place(x=240, y=200)

        self.email_input = tk.Entry(self.window, width=35)
        self.email_input.place(x=325, y=205)

        button_otp = tk.Button(self.window, text="Send OTP", font=("Arial", 13), bg="#00008B", fg="#FFFFFF",
                               command=self.send_otp)
        button_otp.place(x=345, y=250)

        self.window.mainloop()

    def send_otp(self):
        """Generate and send OTP to the entered email address."""
        email = self.email_input.get()
        if not self.validate_email(email):
            messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
            self.email_input.delete(0, tk.END)
            return

        self.otp = str(random.randrange(100000, 999999))
        self.otp_sent_time = datetime.datetime.now()

        try:
            yag = yagmail.SMTP("bhavanamalli117@gmail.com", "pwxi loco huhs chrf")
            yag.send(to=email, subject="OTP Verification Code", contents=f"{self.otp} is the OTP.")
            messagebox.showinfo("Sent", f"OTP has been sent successfully to {email}.")
            self.email_input.delete(0, tk.END)
            self.window.destroy()
            self.verify_otp_window()
        except Exception as e:
            messagebox.showwarning("Error", "Failed to send OTP. Check your email and try again.")
            self.email_input.delete(0, tk.END)

    def verify_otp_window(self):
        """Create a window to verify the OTP."""
        self.window_otp = tk.Tk()
        self.window_otp.geometry("800x500+400+150")
        self.window_otp.configure(bg="#E0F7FA")
        self.window_otp.resizable(False, False)

        try:
            image = Image.open("email.png")
            resize_image = image.resize((80, 80))
            photo = ImageTk.PhotoImage(resize_image)
            image_label = tk.Label(self.window_otp, image=photo)
            image_label.image = photo
            image_label.place(x=350, y=50)
        except FileNotFoundError:
            messagebox.showerror("Error", "Image file 'email.png' not found.")
            return

        text_label = tk.Label(self.window_otp, text="OTP Verification...", font=("Arial", 14))
        text_label.place(x=310, y=150)

        otp_label = tk.Label(self.window_otp, text="Enter OTP ", font=("Arial", 14), bg="#E0F7FA")
        otp_label.place(x=250, y=200)

        self.otp_input = tk.Entry(self.window_otp, width=25)
        self.otp_input.place(x=350, y=205)

        button_verify = tk.Button(self.window_otp, text="Submit", font=("Arial", 13), bg="#00008B", fg="#FFFFFF",
                                  command=self.verify_otp)
        button_verify.place(x=340, y=250)

        self.window_otp.mainloop()

    def verify_otp(self):
        """Verify the entered OTP."""
        user_otp = self.otp_input.get()
        if not user_otp:
            messagebox.showwarning("Invalid", "Please enter the OTP.")
            return

        if self.otp_sent_time:
            elapsed_time = (datetime.datetime.now() - self.otp_sent_time).seconds
            if elapsed_time > 300:
                messagebox.showwarning("Expired", "OTP has expired. Please request a new one.")
                self.window_otp.destroy()
                return

        if self.attempts > 1:
            if user_otp == self.otp:
                messagebox.showinfo("Success", "Access granted.")
                self.window_otp.destroy()
            else:
                self.attempts -= 1
                messagebox.showwarning("Wrong", f"You have {self.attempts} more attempts left. Retry.")
                self.otp_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Failed", "Access denied.")
            self.window_otp.destroy()

    @staticmethod
    def validate_email(email):
        """Validate email format."""
        import re
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_pattern, email)

# Run the application
if __name__ == "__main__":
    OTPApp()
