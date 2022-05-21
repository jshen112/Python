# samples of tk goodies
import tkinter as tk
import os

def circle(canvas,x,y, r):
   id = canvas.create_oval(x-r,y-r,x+r,y+r)
   return id

root = tk.Tk()
CURR_DIR = os.getcwd()
canvas_width = 190
canvas_height =100
python_green = "#476042"
w = tk.Canvas(root, width=canvas_width, height=canvas_height)
w.pack()
c = circle(w,75,50,30)

v = tk.IntVar()
v.set(0)  # initializing the choice, i.e. Python

my_imgs = []
my_imgs.append(tk.PhotoImage(file = CURR_DIR + "/python/Python.png") )
my_imgs.append(tk.PhotoImage(file = CURR_DIR + "/python/Perl.png") )
my_imgs.append(tk.PhotoImage(file = CURR_DIR + "/python/Java.png") )
l2 = tk.Label(root, image=my_imgs[0] )
l2.pack()

languages = [("Python", 0), ("Perl", 1), ("Java", 2), ("C++", 3), ("C", 4)]

def ShowChoice():
    l2.config(image=my_imgs[v.get()])
    
tk.Label(root, text="Choose your favourite language:",justify = tk.LEFT, padx = 20).pack()
f = tk.Frame (root)
f.pack()
for i in range (4):
    tk.Label(f, text="Year " + str (i+1), justify = tk.LEFT, padx = 20).grid(row=i, column=0)
    for language, val in languages:
        tk.Radiobutton(f, text=language, padx = 20, variable=v, command=ShowChoice,
                    value=val).grid(row = i, column=val)

root.mainloop()