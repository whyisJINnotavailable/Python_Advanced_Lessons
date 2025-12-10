# =========================
# 1. Modules imports
import tkinter as tk
import random
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
enemy = canvas.create_oval(50, 50, 90, 90, fill="red")
enemy_speed = 3
# =========================

# =========================
# 4. Game variables (score, lives, state)

# =========================

# =========================
# 5. Helper function (collisions and score)

# =========================

# =========================
# 6. Main GameLoop (update and draw)
def game_loop():
    global enemy_speed

    canvas.move(enemy, 0, enemy_speed)
    ex1, ey1, ex2, ey2 = canvas.coords(enemy)

    # if enemy goes out of bottom, move it back to top at random x
    if ey2 > 400:
        new_x = random.randint(20, 580)
        canvas.coords(enemy, new_x - 20, 0, new_x + 20, 40)

    win.after(30, game_loop)
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

def on_key_press(event):
    if event.keysym == "Left":
        canvas.move(player, -10, 0)
    elif event.keysym == "Right":
        canvas.move(player, 10, 0)
    elif event.keysym == "Up":
        canvas.move(player, 0, -10)
    elif event.keysym == "Down":
        canvas.move(player, 0, 10)

win.bind("<KeyPress>", on_key_press)
# =========================

# =========================
# 8. Start game
game_loop()
win.mainloop()
# =========================