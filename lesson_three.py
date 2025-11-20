import tkinter as tk

#create window
win = tk.Tk()

#image upload
p1 = tk.PhotoImage(file = "elements\download.png")

#setting of window
win.title("Personal details")
win.iconphoto(False,p1)
win.geometry("300x200")

f1 = tk.Frame(width=50, height=40, bg='red')
f2 = tk.Frame(width=80, height=20, bg='green')
f3 = tk.Frame(width=20, height=20, bg='blue')

# "fill = tk.X" - fill the whole space with horizontal
# "fill = tk.Y" - fill the whole space with vertically

# expand = True to expand vertically, space in between them
f1.pack(fill = tk.Y, )
f2.pack(fill = tk.Y, )
f3.pack(fill = tk.Y, )

#looping of window
win.mainloop()