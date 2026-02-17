import tkinter as tk
from tkinter import colorchooser

# -------------------------
# Global State Variables
# -------------------------
last_x, last_y = None, None      # Track previous mouse position
current_color = "black"          # Default drawing color
brush_size = 2                   # Default brush thickness


# -------------------------
# Drawing Functions
# -------------------------

def choose_color():
    """
    Open a color picker dialog and update the current brush color.
    """
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color


def clear_canvas():
    """
    Remove all drawings from the canvas.
    """
    canvas.delete("all")


def start_draw(event):
    """
    Record the starting mouse position when the user begins drawing.
    """
    global last_x, last_y
    last_x, last_y = event.x, event.y


def draw(event):
    """
    Draw a smooth line from the previous mouse position to the current one.
    This function is called continuously while the mouse is dragged.
    """
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
    """
    Update the global brush size based on the slider value.
    """
    global brush_size
    brush_size = int(value)


# -------------------------
# User Interface Setup
# -------------------------

root = tk.Tk()
root.title("Drawing App")

# Main drawing area
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Toolbar for controls
toolbar = tk.Frame(root)
toolbar.pack(pady=5)

# Color and clear buttons
tk.Button(toolbar, text="Choose Color", command=choose_color).pack(side="left", padx=5)
tk.Button(toolbar, text="Clear", command=clear_canvas).pack(side="left", padx=5)

# Brush size slider
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

# Bind mouse events to drawing functions
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

root.mainloop()