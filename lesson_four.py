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
        tk.Button(
            master = win,
            text= f'Btn {1+(i*5)+j}',
            borderwidth=5).grid(row=i, column=j, padx=1, pady=1)


#l1 = tk.Label(text="GUI", bg='yellow')
#l2 = tk.Label(text="GUI", bg = 'red')

#coordinate placement
#l1.grid(row=0, column=0)
#l2.grid(row=1, column=1)

#looping of window
win.mainloop()