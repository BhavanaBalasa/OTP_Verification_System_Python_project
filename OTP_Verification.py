import random # used to generate the random value/values
import tkinter as tk # GUI Library
from PIL import Image,ImageTk # install the pillow library
import yagmail # install the yagmail--pip install yagmail
from tkinter import messagebox # To show the popup box


# function to send otp 
def send_otp():
     global otp # Declare `otp` as a global variable
     email=email_input.get() # to store the email entered
     otp=str(random.randrange(100000,999999))  # random otp generation
     
     # code to send an otp
     try:
        yag=yagmail.SMTP("bhavanamalli117@gmail.com","pwxi loco huhs chrf") # Initialize SMTP client with email and password
        yag.send(to=email, subject="OTP Verification Code",contents=otp+" is the OTP.") #sending an OTP via email
        messagebox.showinfo("Sent","OTP has sent successfully to "+email) #clear the user data in text box
        email_input.delete(0,tk.END) # it clear user entered email 
        window.destroy() #to close the application window
        verify_otp_window() #function call

     # any error/exception noticed it will execute the below code.
     except Exception as e :
        email_input.delete(0,tk.END) #clear the user data in text box
        messagebox.showwarning("Error","Check your email and retry.") # show the pop up message



# code to create a window to enter otp recieved by user
def verify_otp_window():
   # create a new window
   window_otp=tk.Tk()   
   window_otp.geometry("800x500+400+150") # set window size and position (widthxheight+x_position+y_position).
   window_otp.configure(bg="#E0F7FA") # used to change the back ground color using hexa code or name of colour.
   window_otp.resizable(False,False) # used to disable to change the window size in any case.

   image = Image.open("email.png") # Load an image using pillow in pillow compatible image
   resize_image=image.resize((80,80)) #resize the image
   photo=ImageTk.PhotoImage(resize_image) # it convert pillow compatible image into tkinter compatible image

   image_label=tk.Label(window_otp,image=photo) # create a image label and insert in a window.
   image_label.place(x=350, y=50)

   text_label=tk.Label(window_otp,text=" OTP Verification....",font=("Arial",14)) # create a text label in window
   text_label.place(x=310,y=150) # where to position the label in the window

   otp_label=tk.Label(window_otp,text="Enter OTP ",font=("Arial",14),bg="#E0F7FA")# user email input label
   otp_label.place(x=250,y=200)  # where to position the label in the window
   otp_input=tk.Entry(window_otp,width=25) # it create a text box where user can enter the email id
   otp_input.place(x=350,y=205) # where to position the entry box in the window

   # Button to verify otp and use lambda to pass the value dynamically when the button is clicked
   button_verify=tk.Button(window_otp,text="Submit",font=("Arial",13),bg="#00008B",fg="#FFFFFF",command=lambda: otp_verify(otp_input.get(),window_otp,otp_input)) 
   button_verify.place(x=340,y=250)  # where to position the button in the window
   # run the application
   window_otp.mainloop()


attempts=5
# function to verify the otp and show the no of attempts.
def otp_verify(user_otp,window_otp,otp_input):
   global attempts # reassigning the variable requires global within a function.
   if str(user_otp): # used to check whether the user entered the otp
     
     if attempts>1: # check the attempts 
         if user_otp==otp: # checks whether the user entered otp is equal to generated otp
            messagebox.showinfo("Success","Access is granted.") # Show the pop up window 
            otp_input.delete(0,tk.END)  #clearing the user input in textbox
            window_otp.destroy() #to close the application window
      
         else: # below code executes if the user entered otp is not equal to generated otp
            attempts-=1 # decrement the attempts count.
            messagebox.showwarning("Wrong",f"You have {attempts} more attempts retry") # showing attempts count
            otp_input.delete(0,tk.END) #clearing the user input in textbox
            
      
     else: # it executes when given attemptes is used by user i.e., attempts becomes zero
         messagebox.showwarning("Incorrect","Access is denied") # Showing the information access denied after completing given attempts
         window_otp.destroy() # closes the window

   else: # if user did not enter the input
       messagebox.showwarning("Invalid","Please enter the OTP") # it pop up the warning window with text

    
# Create a window and start code
window=tk.Tk()   
window.geometry("800x500+400+150") # set window size and position (widthxheight+x_position+y_position).
window.configure(bg="#E0F7FA") # used to change the back ground color using hexa code or name of colour.
window.resizable(False,False) # used to disable to change the window size in any case.

image = Image.open("email.png")# Load an image using pillow in pillow compatible image
resize_image=image.resize((80,80)) #resize the image 
photo=ImageTk.PhotoImage(resize_image) # it convert pillow compatible image into tkinter compatible image

image_label=tk.Label(window,image=photo) # created a image label and inserted in a window.
image_label.place(x=350, y=50) # where to position the image in the window

text_label=tk.Label(window,text=" Email Id Verification....",font=("Arial",14)) # creating a text label in window
text_label.place(x=310,y=150) # where to position the label text in the window

email_label=tk.Label(window,text="Email Id ",font=("Arial",14),bg="#E0F7FA") # email label to inform to user to enter email id
email_label.place(x=240,y=200) # where to position the label in the window
email_input=tk.Entry(window,width=35) # it create a text box where user can enter the email id
email_input.place(x=325,y=205) # where to position the entry in the window

# Button for otp generation
button_otp=tk.Button(window,text="Send OTP",font=("Arial",13),bg="#00008B",fg="#FFFFFF",command=send_otp)
button_otp.place(x=345,y=250) # where to position the button in the window

# Run the application
window.mainloop()

