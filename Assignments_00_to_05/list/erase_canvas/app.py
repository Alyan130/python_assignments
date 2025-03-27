import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    left_x, top_y = mouse_x, mouse_y
    right_x, bottom_y = left_x + ERASER_SIZE, top_y + ERASER_SIZE
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

def main():
    root = tk.Tk()
    root.title("Eraser Grid")
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    num_rows, num_cols = CANVAS_HEIGHT // CELL_SIZE, CANVAS_WIDTH // CELL_SIZE
    for row in range(num_rows):
        for col in range(num_cols):
            left_x, top_y = col * CELL_SIZE, row * CELL_SIZE
            right_x, bottom_y = left_x + CELL_SIZE, top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue', outline='black')
    
    def on_click(event):
        global eraser
        eraser = canvas.create_rectangle(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill='pink')
        root.after(10, move_eraser)
    
    def move_eraser():
        if 'eraser' in globals():
            mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
            mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
            canvas.coords(eraser, mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)
            erase_objects(canvas, eraser)
            root.after(50, move_eraser)
    
    canvas.bind("<Button-1>", on_click)
    root.mainloop()

if __name__ == '__main__':
    main()
