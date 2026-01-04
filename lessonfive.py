import tkinter as tk

#create window
win = tk.Tk()

#image upload
p1 = tk.PhotoImage(file="Python_Advanced_Lessons\elements\mario.png")

#setting of window
win.title("Mario Game")
win.iconphoto(False,p1)
win.geometry("300x200")

#main 
def keypressed(event):
    print(event.keysym)
    print(event.keycode)
    print(event.char)
    print(event.x)
    print(event.y)

win.bind("<Return>", keypressed) #Enter
win.bind("<Enter>", keypressed) #When moouse enter the tk screen
win.bind("<Key>", keypressed) #When any key is pressed
win.bind("<KeyRelease>", keypressed) #When any key released

win.bind("<Motion>", keypressed) #when mouse move in tk screen
win.bind("<Leave>", keypressed) #When mouse leave the tk screen
win.bind("<MouseWheel>", keypressed) #When mouse wheel is used
win.bind("<Button-1>", keypressed) #Left Click
win.bind("<Button-2>", keypressed) #wheel Click
win.bind("<Button-3>", keypressed) #Right Click
#looping of window
win.mainloop()