import tkinter as tk
def btn_press():
    print('Button was pressed')

root = tk.Tk()
root.geometry('250x100')
bt = tk.Button(bitmap='question', command=btn_press)
bt.pack()

root.mainloop()