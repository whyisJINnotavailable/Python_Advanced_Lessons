import tkinter as tk


#create window
win = tk.Tk()

#image upload
p1 = tk.PhotoImage(file="Python_Advanced_Lessons\elements\mario.png")

#setting of window
win.title("Mario Game")
win.iconphoto(False,p1)
win.geometry("300x200")
win.resizable(False, False)

temp = 27
#main
def redinvade(event):
    global temp
    f1['width'] += 5
    f2['width'] -= 5
    temp += 1
    l1['text'] = f'{temp}°C'
    if f1['width'] > f2['width']:
        l1['bg'] = 'red'
        l1['fg'] = 'blue'
    elif f1['width'] == f2['width']:
        l1['bg'] = 'white'
        l1['fg'] = 'black'

def blueinvade(event):
    global temp
    f1['width'] -= 5
    f2['width'] += 5
    temp -= 1
    l1['text'] = f'{temp}°C'
    if f2['width'] > f1['width']:
        l1['bg'] = 'blue'
        l1['fg'] = 'red'
    elif f1['width'] == f2['width']:
        l1['bg'] = 'white'
        l1['fg'] = 'black'

f1 = tk.Frame(master = win, width=150,bg='red')
f2 = tk.Frame(master=win, width=150,bg='blue')
l1 = tk.Label(
    master=win, 
    text=f'{temp}°C', 
    width=5, 
    height=1, 
    font='Arial 15 bold')

f1.pack(fill=tk.Y,side=tk.LEFT)
f2.pack(fill=tk.Y,side=tk.RIGHT)
l1.place(x=120,y=40)

f1.bind('<Button-1>', redinvade)
f2.bind('<Button-1>', blueinvade)

#loop the screen
win.mainloop()