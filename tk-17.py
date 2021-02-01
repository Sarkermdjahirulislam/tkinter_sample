import tkinter as tk
root = tk.Tk()
root.geometry('250x280')
bt_dict = {}
for bitmap_val in ['info','error','gray12','gray25','gray50','gray75','hourglass','questhead','question','warning']:
    bt_dict[bitmap_val] = tk.Button(bitmap=bitmap_val,width=100)
    bt_dict[bitmap_val].pack()
root.mainloop()