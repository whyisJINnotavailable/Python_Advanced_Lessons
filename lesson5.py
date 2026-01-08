# Lesson 5: Real GameLoop + smooth movement using key states

# =========================
# 1. Modules imports
# - Import the libraries we need (tkinter, random, time)
# =========================
import tkinter as tk

# =========================
# 2. Game window setup
# - Create main window
# - Set settings of window (title, size, icon)
# - 
# =========================
win = tk.Tk()
win.title("Tkinter Game - Canvas Intro")
win.geometry("600x200")
try:
    p1 = tk.PhotoImage(file="C:/Users/User/Desktop/Python_Advance_Lesson/Python_Advanced_Lessons/elements/mario.png") # find where's the picture
    win.iconphoto(False,p1) # put picture as icon in window
except:
    pass

# =========================
# 3. Game canvas and objects
# - Create the canvas & pack them into the window
# - Create player, enemies, items, buttons, text,...
# - Store object IDs returned by canvas.create
# =========================
W = 600
H = 200
canvas = tk.Canvas(win, width=W, height=H, bg="black")
canvas.pack()

player = canvas.create_rectangle(200,180,320,160, fill="white")


# =========================
# 4. Game variables (score, lives, state)
# - Create variables that control the game (speed, game_state, running,...)
# - Create key dictionary
# =========================
speed = 10
keys = {"Left": False, "Right": False, "Up": False, "Down": False}
running = True

# =========================
# 5. Helper function (player movement)
# - Functions that help the game run smoothly (move player, check collisions,...)
# =========================

# =========================
# 6. Main GameLoop (update and draw)
# ========================
def game_loop():
    if not running:
        return
    move_player()
    win.after(16, game_loop)

# =========================
# 7. Player input (buttons and keyboard)
def on_key_press(event):
    if event.keysym in keys:
        keys[event.keysym] = True

def on_key_release(event):
    if event.keysym in keys:
        keys[event.keysym] = False

def move_player():
    # dx = 0
    # dy = 0
    dx = dy = 0

    if keys["Left"]:
        dx -= speed
    if keys["Right"]:
        dx += speed
    if keys["Up"]:
        dy -= speed
    if keys["Down"]:
        dy += speed
    
    canvas.move(player, dx, dy)

win.bind("<KeyPress>", on_key_press)
win.bind("<KeyRelease>", on_key_release)
# =========================

# =========================
# 8. Start game
game_loop()
win.mainloop()
# =========================