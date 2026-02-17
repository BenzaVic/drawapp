import tkinter as tk

last_x, last_y = None, None

#Function
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, fill="black", width=2)
    last_x, last_y = event.x, event.y


#User Interface
root = tk.Tk()
root.title("Drawing App")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)   

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

root.mainloop()