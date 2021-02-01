import tkinter as  tk
root = tk.Tk()
root.geometry('400x250')
ms_dict = {}

for relief_var in ['flat','raised','sunken','groove','ridge']:
    ms_dict[relief_var] = tk.Message(text=relief_var,relief=relief_var, bd=10,width=500)
    ms_dict[relief_var].pack()

root.mainloop()