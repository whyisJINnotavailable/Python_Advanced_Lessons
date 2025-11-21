# Learned about
# 1. Widget Assignation for user's input
# 2. Adding Widget into the window
# 3. Learned created the script template/format of gui 

import tkinter as tk

#create window
win = tk.Tk()

#variable
name = tk.StringVar()
age = tk.StringVar()
gender = tk.StringVar()

#function
def save():
    print(f'{name.get()} is {age.get()} years old. {name.get()} want be the best young {gender.get()} coder.')
    win.quit()

#image upload
# "(file = "folder_name\picture_name.png)"
p1 = tk.PhotoImage(file = "elements\download.png")

#setting of window (properties of window)
win.title("Personal Details")
win.geometry("300x200")
win.iconphoto(False,p1)

#assign widget (create input box for user to input, examples:name,age,gender)
label1 = tk.Label(
    text = 'Name:',
    font = "Forte 10 italic bold underline",
    fg = 'black',
    bg = 'white',
    width = 15,
    anchor = tk.W,
    pady = 5
    )
input1 = tk.Entry(
    textvariable = name,
    font = "Calibri 10",
    bg = "orange",
    relief = tk.RAISED
    )
label2 = tk.Label(text = 'Age:')
input2 = tk.Entry(textvariable = age)
label3 = tk.Label(text = 'Gender:')
input3 = tk.Entry(textvariable = gender)
btn = tk.Button(
    text = 'Done',
    command = save)

#adding widget into window (put the widgets that created into the window)
label1.pack()
input1.pack()
label2.pack()
input2.pack()
label3.pack()
input3.pack()
btn.pack()

#looping of window (keep your window staying there)
win.mainloop()