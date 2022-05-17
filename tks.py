import tkinter as tk

def circle(canvas,x,y, r):
   id = canvas.create_oval(x-r,y-r,x+r,y+r)
   return id

root = tk.Tk()

canvas_width = 190
canvas_height =150
python_green = "#476042"
w = tk.Canvas(root, 
           width=canvas_width, 
           height=canvas_height)
w.pack()
c = circle(w,75,75,50)
w.create_oval(50,50,100,100, outline=python_green, fill='red', width=3)

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [("Python", 101),
        ("Perl", 102),
            ("Java", 103),
            ("C++", 104),
            ("C", 105)]

def ShowChoice():
    print(v.get())
tk.Label(root, 
        text="Choose your favourite programming language:",
        justify = tk.LEFT,
        padx = 20).pack()

for language, val in languages:
    tk.Radiobutton(root, 
                text=language,
                padx = 20, 
                variable=v, 
                command=ShowChoice,
                value=val).pack(anchor=tk.W)

root.mainloop()