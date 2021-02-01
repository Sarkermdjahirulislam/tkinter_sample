import tkinter as  tk
root = tk.Tk()
root.geometry('400x250')
ms_dict = {}

for bw_int in range (1,6):
    bw_str = str(bw_int)
    ms_dict[bw_str] = tk.Message(text='borderwidge='+bw_str,relief='ridge',bd=bw_int,width=85)
    ms_dict[bw_str].pack()

root.mainloop()