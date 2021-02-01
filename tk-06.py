import tkinter as tk

def action_btn_press():
    print('Azuma Senmon College')
root = tk.Tk()
root.title('Widget creation')
root.geometry('350x150')
lb = tk.Label(text='LB')
bt = tk.Button(text='BUTTON-1',command=action_btn_press)
lb.pack()
bt.pack()
root.mainloop()