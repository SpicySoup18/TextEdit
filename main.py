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

def change_size():
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
families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria', 'Georgia', 'MS Gothic', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']
font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set('Terminal')
#Set the width so it will fit "times new roman" and remain constant
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)

"""Must build out sections for sizes of font, as well as font options"""

#Set the width so it will fit "times new roman" and remain constant
font_sizes = ['8', '9', '10', '11', '12', '14', '18', '24', '30', '36', '48', '60', '72', '96']
size_family = StringVar()
font_sizes_drop = tkinter.OptionMenu(menu_frame, size_family, *font_sizes, command=change_size())
size_family.set('8')
#Set the width so it will fit "times new roman" and remain constant
font_sizes_drop.config(width=4)
font_sizes_drop.grid(row=0, column=5, padx=5, pady=5)

#Set the width to be constant

#Layout for the text frame

#Create input_text as a scrolledtext so you can scroll through the text field
#Set default width and height to be more than the window size so that on the smallest text size, the text field size is constant




#Run the root main window
root.mainloop()