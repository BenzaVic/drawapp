import tkinter as tk
from tkinter import colorchooser

last_x, last_y = None, None
current_color = "black"
brush_size = 2   # default thickness

# -------------------------
# Functions
# -------------------------

def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

def clear_canvas():
    canvas.delete("all")

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line(
        last_x, last_y, event.x, event.y,
        fill=current_color,
        width=brush_size,
        capstyle=tk.ROUND,
        smooth=True
    )
    last_x, last_y = event.x, event.y

def update_brush_size(value):
    global brush_size
    brush_size = int(value)

# -------------------------
# User Interface
# -------------------------

root = tk.Tk()
root.title("Drawing App")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

toolbar = tk.Frame(root)
toolbar.pack()

tk.Button(toolbar, text="Choose Color", command=choose_color).pack(side="left", padx=5)
tk.Button(toolbar, text="Clear", command=clear_canvas).pack(side="left", padx=5 )

# Thickness slider
size_slider = tk.Scale(
    toolbar,
    from_=1,
    to=20,
    orient="horizontal",
    label="Brush Size:",
    command=update_brush_size
)
size_slider.set(2)
size_slider.pack(side="left", padx=5)

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

root.mainloop()