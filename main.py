#Freshman Notepad

import tkinter
from PIL import ImageTk, Image
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog

#Define window
root = tkinter.Tk()
root.title("Freshman Notepad")
root.geometry('600x600')
root.resizable(100, 100)

#Define fonts and colors
text_color = "#fffacd"
menu_color = "#dbd9db"
root_color = "#6c809a"
root.config(bg=root_color)

#Define functions
def change_font(event):
    pass

def new_note():
    pass

def close_note():
    pass

def save_note():
    pass

def open_note():
    pass

#Define layout and frames
menu_frame = tkinter.Frame(root, bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

#Layout for menu frame
new_image = ImageTk.PhotoImage(Image.open("new.png"))
new_button = tkinter.Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)


#Create a list of fonts to use

#Set the width so it will fit "times new roman" and remain constant


#Set the width to be constant

#Layout for the text frame

#Create input_text as a scrolledtext so you can scroll through the text field
#Set default width and height to be more than the window size so that on the smallest text size, the text field size is constant




#Run the root main window
root.mainloop()