import tkinter as tk
root = tk.Tk()
root.title('widget')
root.geometry('450x350+350+250')

lb=tk.Label(text='Label1')
bt = tk.Button(text='button1')

lb.pack()
bt.pack()

root.mainloop()