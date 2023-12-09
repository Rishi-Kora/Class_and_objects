def button_click(name_str, job_str):
    print(name_str + ' is a ' + job_str)
 
import tkinter as tk
window = tk.Tk()
tk.Label(window, text='Name').grid(row=0)
tk.Label(window, text='Job Title').grid(row=1)
name = tk.Entry(window)
name.grid(row=0,column=1)
job = tk.Entry(window)
job.grid(row=1,column=1)
tk.Button(window, text='Cancel', command=window.destroy).grid(row=2, column=3)
#Notice there are no () in destroy (above). If there were, the function would
#be called instantly – and not when clicked
tk.Button(window, text='Ok', command=lambda:button_click(name.get(), 
job.get())).grid(row=2, column=1)
window.mainloop()
