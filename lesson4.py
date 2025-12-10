# =========================
# 1. Modules imports
import tkinter as tk
# =========================

# =========================
# 2. Game window setup
win = tk.Tk()
win.title("Tkinter Game - Canvas Intro")
win.geometry("600x400")
#p1 = tk.PhotoImage(file="address")
#win.iconphoto(False,p1)
# =========================

# =========================
# 3. Game canvas and objects
canvas = tk.Canvas(win, width=600, height=400, bg="black")
canvas.pack()

player = canvas.create_rectangle(200,180,320,220, fill="white")

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
def move_left():
    canvas.move(player, -10, 0)

def move_right():
    canvas.move(player, 10, 0)

btn_left = tk.Button(win, text="Left", command=move_left)
btn_left.pack(side="left")

btn_right = tk.Button(win, text="Right", command=move_right)
btn_right.pack(side="right")

# =========================

# =========================
# 8. Start game

win.mainloop()
# =========================