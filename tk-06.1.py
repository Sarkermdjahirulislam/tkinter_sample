import tkinter as tk

def action_btn_press():
    print('Azuma Senmon College')
def action_btn_press1():
    print('Happy Birthday')
def action_btn_press2():
    print('おめでとうございます。')
def action_btn_press3():
    print('シリヤ')
def action_btn_press4():
    print('ウィン')


root = tk.Tk()
root.title('Widget creation')
root.geometry('350x180')
lb = tk.Label(text='Level')
bt1 = tk.Button(text='BUTTON-1',command=action_btn_press)
bt2 = tk.Button(text='BUTTON-2',command=action_btn_press1)
bt3 = tk.Button(text='BUTTON-3',command=action_btn_press2)
bt4 = tk.Button(text='BUTTON-4',command=action_btn_press3)
bt5 = tk.Button(text='BUTTON-5',command=action_btn_press4)


lb.pack()
bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()
bt5.pack()
root.mainloop()