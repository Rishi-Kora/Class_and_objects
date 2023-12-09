import tkinter as tk
window  = tk.Tk()
tk.Label(window, text = "Name").grid(row = 0)
tk.Label(window, text = "Job Title").grid(row = 1)
tk.Entry(window).grid(row = 0, column = 1)
tk.Entry(window).grid(row = 1, column = 1)
window.mainloop()
