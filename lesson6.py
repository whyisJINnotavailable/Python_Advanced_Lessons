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
score_var = tk.IntVar(value=0)
score_label = tk.Label(win, textvariable=score_var, font=("Arial", 16))
score_label.pack()

lives = 3
game_over = False
# =========================

# =========================
# 5. Helper function (collisions and score)
def is_collision(a, b):
    ax1, ay1, ax2, ay2 = canvas.coords(a)
    bx1, by1, bx2, by2 = canvas.coords(b)

    return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)

def increase_score(points):
    score_var.set(score_var.get() + points)
# =========================

# =========================
# 6. Main GameLoop (update and draw)
def game_loop():
    global game_over, lives
    if game_over:
        return

    canvas.move(enemy, 0, enemy_speed)
    ex1, ey1, ex2, ey2 = canvas.coords(enemy)

    # if enemy leaves the bottom, respawn at top and lose a life or just continue
    if ey2 > 400:
        lives -=1
        if lives <= 0:
            game_over = True
            canvas.create_text(300,200, text="GAME OVER", fill="yellow", font=("Arial", 32))
            return
        
        new_x = random.randint(20, 580)
        canvas.coords(enemy, new_x - 20, 0, new_x + 20, 40)

    # check collision with player
    if is_collision(player, enemy):
        increase_score(1)
        new_x = random.randint(20, 580)
        canvas.coords(enemy, new_x - 20, 0, new_x + 20, 40)

    win.after(30, game_loop)

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