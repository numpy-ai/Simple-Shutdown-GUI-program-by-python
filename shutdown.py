import os
from tkinter import*

tk = Tk()
tk.geometry("300x200")
tk.title("Shutdown program")
tk.resizable(False, False)

lab1 = Label(tk)
lab1['text'] = "희망하는 시간(Time you want)"
lab1.pack()
lab3 = Label(tk)
lab3['text'] = "Range : 0-315360000(10y)"
lab3.pack()

lab2 = Label(tk)
ent1 = Entry(tk)

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

# if ent1.get() <= "315360000" and ent1.get() >= "0" :
#     pass
# else :
#     lab2.configure(text = "Range : 0-315360000")


ent1.bind("<Return>", print_result())
ent1.pack()
lab2.pack()

Button(tk, text = "shutdown time", command = shutdown_time).place(x = 105, y = 90)
Button(tk, text = "restart", command = restart).place(x = 125, y = 120)
Button(tk, text = "cancel", command = cancel).place(x = 125, y = 150)

tk.mainloop()