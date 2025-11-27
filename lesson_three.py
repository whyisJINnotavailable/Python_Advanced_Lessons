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

# - Frame() is like a box or compartment inside your main window.
# - You will not "see" a frame, unless you give a background color)
# - Use to group widgets together, control layout easily, build complex UIs

# Conclusion: Frame is a container widget that helps you organise the layout
#             and structure of your GUI.

# Creating the frame (Sample) (will not visible, until geometry manager)
#f1 = tk.Frame(width=50, height=40, bg='red')
#f2 = tk.Frame(width=80, height=20, bg='green')
#f3 = tk.Frame(width=20, height=20, bg='blue')

# WARNING: A frame will not appear, until you give it a geometry manager.
# Geometry Manager: "pack()", "grid()", & "place()"

# Difference Between tk.X, tk.Y, tk.BOTH
#---------------------------------------------
# The frame stretches horizontally to fill all the width of the space it is given
#f1.pack(fill = tk.X)
#f2.pack(fill = tk.X)
#f3.pack(fill = tk.X)

# The frame stretches vertically to fill all the height of the space it is given
#f1.pack(fill = tk.Y)
#f2.pack(fill = tk.Y)
#f3.pack(fill = tk.Y)

# The frame stretches both horizontally and vertically
#f1.pack(fill = tk.BOTH)
#f2.pack(fill = tk.BOTH)
#f3.pack(fill = tk.BOTH)
#---------------------------------------------

# "expand = True / False" = 
# “When the window has extra space, which widgets should get that extra space?”

#expand = False
#The widget keeps only the space it needs. Extra space in the window will 
#remain empty (blank) around the widget, usually at the opposite side.

#expand = True
#Tells Tkinter: “When there is extra space, please give some of that space to this widget.”

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

# master - is to defines which container this widget should live insides.

# Structure, based on our current settings
# win
# -  f1
#   -  f2
# -  f3

f1 = tk.Frame(master=win, width=100, height=40, bg='red', padx=5, pady=5)
# padx & pady is to keep settings of internal padding inside
# which means, anything inside of "f1", will be 5 pixel away from x and y
f2 = tk.Frame(master=f1, width=30, height=30, bg='green')
f3 = tk.Frame(master=win, width=200, height=20, bg='blue')

f1.pack(fill = tk.BOTH, expand=True, side=tk.LEFT)
#  will have 30 pixel away from left edge, and top edge of "f1"
f2.place(x =  30, y = 30)
f3.pack(fill = tk.BOTH, expand=True, side=tk.LEFT)

#looping of window
win.mainloop()