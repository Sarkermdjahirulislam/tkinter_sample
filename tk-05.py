import tkinter as tk
root = tk.Tk()
root.title('Widget creation')
root.geometry('350x150')
lb = tk.Label(text='LB')
bt = tk.Button(text='BUTTON-1')
lb.pack()
bt.pack()
root.mainloop()