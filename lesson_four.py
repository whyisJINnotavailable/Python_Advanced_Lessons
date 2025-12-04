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
#for i in range(5):
#    tk.Button(text="BTN").grid(row=i, column=0)

#for j in range(5):
#    tk.Button(text="BTN").grid(row=0, column=j)

#stk = ['e','w','n','s']
stk = ['ne','ew','ns','nsew']
for i in range(2):
    win.rowconfigure(index=i, weight=1, minsize=200/5)
    for j in range(2):
        win.columnconfigure(index=i, weight=1, minsize=300/5)
        tk.Button(
            master = win,
            #this will make each button have numbers name on it
            text= f'Btn {1+(i*5)+j}',
            borderwidth=5).grid(row=i, column=j, padx=1, pady=1, sticky= stk[(i*2)+j])


#l1 = tk.Label(text="GUI", bg='yellow')
#l2 = tk.Label(text="GUI", bg = 'red')

#coordinate placement
#l1.grid(row=0, column=0)
#l2.grid(row=1, column=1)

#looping of window
win.mainloop()