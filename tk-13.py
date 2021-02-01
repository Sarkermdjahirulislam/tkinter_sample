import tkinter as  tk
root = tk.Tk()
root.geometry('400x200')
lb = tk.Label(text='This is a Label\n This is a Label name of the Button,  and is called a Label')
ms = tk.Message(text='This is a Message\nThis is a Message for you. This is a Message where write something.')
[widget.pack() for widget in (lb,ms)]
root.mainloop()