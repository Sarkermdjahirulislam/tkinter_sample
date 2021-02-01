import tkinter as tk
def get_selpoint():
    sel_start = txt.index('sel.first')
    sel_end = txt.index('sel.last')
    lb['text']= 'start:{} end:{}'.format(sel_start, sel_end)

root = tk.Tk()
lb = tk.Label()
txt = tk.Text(width=30, height=10)
bt = tk.Button(text='Selected Area', command=get_selpoint)
[w.pack() for w in (lb, txt, bt)]

root.mainloop()