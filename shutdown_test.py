import os
# from tkinter import*
import tkinter.messagebox
import tkinter as tki

from setuptools import Command

tk = tki.Tk()
tk.geometry("300x200")
tk.title("Shutdown program")
tk.resizable(False, False)

lab1 = tki.Label(tk)
lab1['text'] = "희망하는 시간(Time you want)"
lab1.pack()
limit_text_lab = tki.Label(tk)
limit_text_lab['text'] = "Range : 0-315360000(10y)"
limit_text_lab.pack()

lab2 = tki.Label(tk)
ent1 = tki.Entry(tk)
ent1.pack()

def print_result() :
    lab2.configure(text = "shutdown a " + ent1.get() + "m after")
# ent1.bind("<Return>", print_result())
lab2.pack()

def error_box() :
    tkinter.messagebox.showerror("Limit Error!", "Range : 0-315360000(10y)")

class main_funtion : 
    def shutdown_time(self) : 
        print_result()
        return os.system("shutdown -s -t " + ent1.get())
    def restart(self) :
        print_result()
        return os.system("shutdown -r -t")
    def cancel(self) :
        return os.system("shutdown -a")

Activity_tool = main_funtion()

button1 = tki.Button(tk, text = "shutdown time", command = Activity_tool.shutdown_time).place(x = 105, y = 90)
button2 = tki.Button(tk, text = "restart", command = Activity_tool.restart).place(x = 125, y = 120)
button3 = tki.Button(tk, text = "cancel", command = Activity_tool.cancel).place(x = 125, y = 150)

# if ent1.get() > "315360000":
#     print(len(ent1.get()))
#     error_box()

# if ent1.get() <= "315360000" and ent1.get() >= "0" :
#     Activity_tool = main_funtion()
#     tki.Button(tk, text = "shutdown time", command = Activity_tool.shutdown_time).place(x = 105, y = 90)
#     tki.Button(tk, text = "restart", command = Activity_tool.restart).place(x = 125, y = 120)
#     tki.Button(tk, text = "cancel", command = Activity_tool.cancel).place(x = 125, y = 150)
    
# else :
#     tki.Button(tk, text = "shutdown time", command = error_box()).place(x = 105, y = 90)
#     tki.Button(tk, text = "restart", command = error_box()).place(x = 125, y = 120)
#     tki.Button(tk, text = "cancel", command = error_box()).place(x = 125, y = 150)
#     print(ent1.get())

    # error_box()
    

# if ent1.get() <= "315360000" and ent1.get() >= "0" :
#     button1['state'] = tki.ACTIVE
#     button2['state'] = tki.ACTIVE
#     button3['state'] = tki.ACTIVE
# else :
#     button1['state'] = tki.DISABLED
#     button2['state'] = tki.DISABLED
#     button3['state'] = tki.DISABLED    

tk.mainloop()