"""Text Edit"""

import tkinter
from PIL import ImageTk, Image
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog

"""Create Window"""

root = tkinter.Tk()
root.title("Text Edit")
root.geometry('600x800')
root.resizable(100, 100)

"""Define Fonts and Colors"""

text_color = "#fffacd"
menu_color = "#dbd9db"
root_color = "#6c809a"
root.config(bg=root_color)

"""Functions"""
def change_font():
    """Change the given font based off the dropdown options"""
    if mods_family.get() == "None":
        used_font = (font_family.get(), size_family.get())
    else:
        used_font = (font_family.get(), size_family.get(), mods_family.get())

    # Change the font styles
    input_text.config(font=used_font)

def new_note():
    pass

def close_note():
    pass

def save_note():
    pass

def open_note():
    pass



"""Menu and Text Frames"""

menu_frame = tkinter.Frame(root, bg=menu_color)
text_frame = tkinter.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

"""Buttons and Positions"""

new_image = ImageTk.PhotoImage(Image.open("new.png"))
new_button = tkinter.Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)


"""Fonts"""

families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria', 'Georgia', 'MS Gothic', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']
font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command=change_font)
font_family.set('Terminal')

"""Fonts Positions"""

font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)


"""Font Sizes"""

font_sizes = ['8', '9', '10', '11', '12', '14', '18', '24', '30', '36', '48', '60', '72', '96']
size_family = StringVar()
font_sizes_drop = tkinter.OptionMenu(menu_frame, size_family, *font_sizes, command=change_font())
size_family.set('24')

"""Font Size Positions"""

font_sizes_drop.config(width=4)
font_sizes_drop.grid(row=0, column=5, padx=5, pady=5)


"""Character Modifications"""
mods = ['None', 'Bold', 'Italics']
mods_family = StringVar()
mods_drop = tkinter.OptionMenu(menu_frame, mods_family, *mods, command=change_font)
mods_family.set('None')

"""Character Modification Positions"""
mods_drop.config(width=4)
mods_drop.grid(row=0, column=6, padx=5, pady=5)

used_font = (font_family.get(), size_family.get())

input_text = tkinter.scrolledtext.ScrolledText(text_frame, width=1000, height=100, bg=text_color, font=used_font)
input_text.pack()

root.mainloop()