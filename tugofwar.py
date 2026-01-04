import tkinter as tk


#create window
win = tk.Tk()

#image upload
p1 = tk.PhotoImage(file="Python_Advanced_Lessons\elements\mario.png")

#setting of window
win.title("Energy Tug-of-War")
win.iconphoto(False, p1)
win.geometry("500x250")
win.resizable(False, False)

# starting values
energy = 50
game_over = False

#main
def redinvade(event):
    global energy, game_over

    if game_over:
        return

    # ROBOTS (LEFT) steal 10 width each click
    f1['width'] += 10
    f2['width'] -= 10

    # update energy
    energy += 2
    if energy > 100:
        energy = 100

    l1['text'] = f'Energy: {energy}%'

    # win condition
    if f1['width'] >= 250:
        l1['text'] = "Robots Win!"
        l1['bg'] = 'green'
        l1['fg'] = 'white'
        game_over = True
        return

    # color switching logic
    if f1['width'] > f2['width']:
        l1['bg'] = 'green'
        l1['fg'] = 'white'
    elif f1['width'] < f2['width']:
        l1['bg'] = 'purple'
        l1['fg'] = 'yellow'
    else:
        l1['bg'] = 'gray'
        l1['fg'] = 'black'


def blueinvade(event):
    global energy, game_over

    if game_over:
        return

    # ALIENS (RIGHT) steal 15 width each click
    f1['width'] -= 15
    f2['width'] += 15

    # update energy
    energy -= 3
    if energy < 0:
        energy = 0

    l1['text'] = f'Energy: {energy}%'

    # win condition
    if f2['width'] >= 250:
        l1['text'] = "Aliens Win!"
        l1['bg'] = 'purple'
        l1['fg'] = 'yellow'
        game_over = True
        return

    # color switching logic
    if f1['width'] > f2['width']:
        l1['bg'] = 'green'
        l1['fg'] = 'white'
    elif f1['width'] < f2['width']:
        l1['bg'] = 'purple'
        l1['fg'] = 'yellow'
    else:
        l1['bg'] = 'gray'
        l1['fg'] = 'black'


# NOTE: Keep same widgets (2 frames + 1 label), only change values/colors/text
f1 = tk.Frame(master=win, width=180, bg='green')   # Robots
f2 = tk.Frame(master=win, width=120, bg='purple')  # Aliens

l1 = tk.Label(
    master=win,
    text=f'Energy: {energy}%',
    width=12,
    height=1,
    font='Arial 20 bold',
    bg='gray',
    fg='black'
)

f1.pack(fill=tk.Y, side=tk.LEFT)
f2.pack(fill=tk.Y, side=tk.RIGHT)

# reposition label (center-ish)
l1.place(x=160, y=40)

# bind clicks (keep same binding idea)
f1.bind('<Button-1>', redinvade)
f2.bind('<Button-1>', blueinvade)

#loop the screen
win.mainloop()
