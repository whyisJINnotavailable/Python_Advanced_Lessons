import tkinter as tk

#create window
win = tk.Tk()

#image upload
p1 = tk.PhotoImage(file = "elements\download.png")

#setting of window
win.title("Personal details")
win.iconphoto(False,p1)
win.geometry("300x200")

f1 = tk.Frame(master=win, width=100, height=40, bg='red', padx=5, pady=5)
f2 = tk.Frame(master=f1, width=30, height=30, bg='green')
f3 = tk.Frame(master=win, width=200, height=20, bg='blue')

# "fill = tk.X" - fill the whole space with horizontal
# "fill = tk.Y" - fill the whole space with vertically

# expand = True to expand vertically, space in between them
f1.pack(fill = tk.BOTH, expand=True, side=tk.LEFT)
f2.place(x =  30, y = 30)
f3.pack(fill = tk.BOTH, expand=True, side=tk.LEFT)

#looping of window
win.mainloop()