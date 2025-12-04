import tkinter as tk

#create window
win = tk.Tk()

#image upload
#p1 = tk.PhotoImage(file="address")

#setting of window
win.title("Window Title")
#win.iconphoto(False,p1)
win.geometry("300x200")

#main
for i in range(5):
    for j in range(5):
        tk.Button(text='text').grid(row=i, column=j)

l1 = tk.Label(text="GUI", bg='yellow')
l2 = tk.Label(text="GUI", bg = 'red')

l1.grid(row=0, column=0)
l2.grid(row=1, column=1)

#looping of window
win.mainloop()