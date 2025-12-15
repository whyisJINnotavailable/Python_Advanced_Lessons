# =========================
# 1. Modules imports
import tkinter as tk
# =========================

# =========================
# 2. Game window setup
win = tk.Tk()
win.title("Crazy Mario")
#win.geometry("width x height")
win.geometry("600x200")
p1 = tk.PhotoImage(file="elements/mario.png")
win.iconphoto(False,p1)
# =========================

# =========================
# 3. Game canvas and objects
canvas = tk.Canvas(win, width=600, height=200, bg="black")
canvas.pack()
# player = canvas.create_rectangle(x1,y1,x2,y2, fill="white")
player = canvas.create_rectangle(275,75,325,125, fill="white")

# =========================

# =========================
# 4. Game variables (score, lives, state)

# =========================

# =========================
# 5. Helper function (collisions and score)

# =========================

# =========================
# 6. Main GameLoop (update and draw)

# =========================

# =========================
# 7. Player input (buttons and keyboard)
def on_key_press(event):
    if event.keysym == "Left":
        canvas.move(player, -10, +0)
    elif event.keysym == "Right":
        canvas.move(player, +10, +0)
    elif event.keysym == "Up":
        canvas.move(player, 0, -10)
    elif event.keysym == "Down":
        canvas.move(player, 0, 10)

win.bind("<KeyPress>", on_key_press)
# =========================

# =========================
# 8. Start game

win.mainloop()
# =========================