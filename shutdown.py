import os
from tkinter import*

tk = Tk()
tk.geometry("300x200")
tk.title("Enter Shutdown Time")
tk.resizable(False, False)

lab1 = Label(tk)
lab1['text'] = "희망하는 시간(Time you want)"
lab1.pack()

lab2 = Label(tk)
def print_result() :
    lab2.configure(text = "shutdown a " + ent1.get() + "s after")
def shutdown_time() : 
    print_result()
    return os.system("shutdown -s -t " + ent1.get())
def restart() :
    print_result()
    return os.system("shutdown -r -t")
def cancel() :
    return os.system("shutdown -a")

ent1 = Entry(tk)
ent1.bind("<Return>", print_result())

ent1.pack()
lab2.pack()

Button(tk, text = "shutdown_time", command = shutdown_time).place(x = 100, y = 70)
Button(tk, text = "restart", command = restart).place(x = 120, y = 100)
Button(tk, text = "cancel", command = cancel).place(x = 120, y = 130) 

tk.mainloop()
