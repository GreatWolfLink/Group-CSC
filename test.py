import tkinter as tk
from PIL import ImageTk,Image


window = tk.Tk()


img = ImageTk.PhotoImage(file="Background.png")
        
Background = tk.Label(window,image=img)
Background.pack()


window.mainloop()
