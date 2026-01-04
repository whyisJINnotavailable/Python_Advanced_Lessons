# Lesson 5: Real GameLoop + smooth movement using key states

# =========================
# 1. Modules imports
import tkinter as tk
# =========================

# =========================
# 2. Game window setup
win = tk.Tk()
win.title("Tkinter Game - Canvas Intro")
win.geometry("600x200")
try:
    p1 = tk.PhotoImage(file="C:/Users/User/Desktop/Python_Advance_Lesson/Python_Advanced_Lessons/elements/mario.png")
    win.iconphoto(False,p1)
except:
    pass
# =========================

# =========================
# 3. Game canvas and objects
W = 600
H = 200
canvas = tk.Canvas(win, width=W, height=H, bg="black")
canvas.pack()

player = canvas.create_rectangle(200,180,320,220, fill="white")

# =========================

# =========================
# 4. Game variables (score, lives, state)
speed = 6
keys = {"Left": False, "Right": False, "Up": False, "Down": False}
running = True
# =========================

# =========================
# 5. Helper function (collisions and score)
def clamp_item(item_id):
    x1, y1, x2, y2 = canvas.coords(item_id)
    dx = 0
    dy = 0
    if x1 < 0: dx = -x1
    if x2 > W: dx = W - x2
    if y1 < 0: dy = -y1
    if y2 > H: dy = H - y2
    if dx or dy:
        canvas.move(item_id, dx, dy)
# =========================

# =========================
# 6. Main GameLoop (update and draw)
def game_loop():
    if not running:
        return

    dx = 0
    dy = 0

    if keys["Left"]:  dx -= speed
    if keys["Right"]: dx += speed
    if keys["Up"]:    dy -= speed
    if keys["Down"]:  dy += speed

    canvas.move(player, dx, dy)
    clamp_item(player)

    win.after(16, game_loop)
# =========================

# =========================
# 7. Player input (buttons and keyboard)
def on_key_press(event):
    if event.keysym in keys:
        keys[event.keysym] = True

def on_key_release(event):
    if event.keysym in keys:
        keys[event.keysym] = False

win.bind("<KeyPress>", on_key_press)
win.bind("<KeyRelease>", on_key_release)
# =========================

# =========================
# 8. Start game
game_loop()
win.mainloop()
# =========================