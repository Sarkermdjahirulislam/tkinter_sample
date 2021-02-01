import tkinter as tk
def print_txtval():
    val_id = en.get()
    val_name = en1.get()
    print('User ID: {} Name: {}'.format(val_id,val_name))
    en.delete(0,tk.END)
    en1.delete(0,tk.END)
    en.focus_set()
    en.insert(0,'AP')



root = tk.Tk()
root.geometry('250x280')
lb = tk.Label(text='User ID')
en = tk.Entry()

lb1 = tk.Label(text='Name')
en1 = tk.Entry()
bt = tk.Button(text='Enter Data', command=print_txtval)
[widget.pack() for widget in (lb,en,lb1,en1,bt)]
en.focus_set()
en.insert(0,'AP')


root.mainloop()