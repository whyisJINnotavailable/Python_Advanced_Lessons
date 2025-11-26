import tkinter as tk

#MAKE SURE YOU HAVE THE TEMPLATE BEFORE START.
#---------------------------------------------
#create window
#win = tk.Tk()

#image upload
#p1 = tk.PhotoImage(file="folder_name\picture_name.format(png, jpg, jpeg,...)")

#setting of window
#win.title("Title_Name")
#win.iconphoto(False,p1)
#win.geometry("300x200")

#looping of window
#win.mainloop()
#---------------------------------------------

# LESSON THREE: FRAME()
# - FRAME() is for organize the layout and separate the compartment of widgets.
# - helps on adjust the size of compartment to fir the other widget include the other frame.
# - same like a picture frame, we can adjust and construct the structure we want.

# SIMPLE FRAME() WIDGET
#f1 = tk.Frame(width=50, height=40, bg='red')
#f2 = tk.Frame(width=80, height=20, bg='green')
#f3 = tk.Frame(width=20, height=20, bg='blue')

# CHOOSE EITHER ONE TO FILL EITHER X(HORIZONTALLY) OR Y(VERTICALLY)
#---------------------------------------------
# IT WILL FILL THE FRAME TO THE X (HORIZONTAL FILLED ONLY)
#f1.pack(fill = tk.X)
#f2.pack(fill = tk.X)
#f3.pack(fill = tk.X)

# IT WILL FILL THE FRAME TO THE Y (VERTICALLY FILLED ONLY)
#f1.pack(fill = tk.Y)
#f2.pack(fill = tk.Y)
#f3.pack(fill = tk.Y)
#---------------------------------------------

# IT WILL FILL, EVEN IF YOU INCREASE THE SIZE OF WINDOW, IT WILL STICK AND FILL
#f1.pack(fill = tk.Y, expand = True)
#f2.pack(fill = tk.Y, expand = True)
#f3.pack(fill = tk.Y, expand = True)

# IT WILL FILL THE WHOLE WINDOW, BUT BASED ON THE WIDTH & HEIGHT PRESET IN THE FRAME()
#f1.pack(fill = tk.BOTH, expand = True)
#f2.pack(fill = tk.BOTH, expand = True)
#f3.pack(fill = tk.BOTH, expand = True)


#create window
win = tk.Tk()

#image upload
p1 = tk.PhotoImage(file = "Python_Advanced_Lessons\elements\download.png")

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