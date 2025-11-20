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
p1 = tk.PhotoImage(file = "elements\download.png")

#setting of window
win.title("Personal Details")
win.geometry("300x200")
win.iconphoto(False,p1)

#assign widget
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

#adding widget into window
label1.pack()
input1.pack()
label2.pack()
input2.pack()
label3.pack()
input3.pack()
btn.pack()

#looping of window
win.mainloop()