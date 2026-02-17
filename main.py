import tkinter as tk

root = tk.Tk()
root.title("Drawing App")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)   

root.mainloop()