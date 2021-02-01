import tkinter as tk
root = tk.Tk()
root.title('.config()')

root.geometry('350x150')
lb = tk.Label()
lb['text'] = 'Lebel'

print(lb.config())
root.mainloop()