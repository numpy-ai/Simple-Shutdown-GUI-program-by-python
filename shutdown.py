import os
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
ent1 = tki.Entry(tk, textvariable=tki.IntVar())
ent1.pack()

def print_result() :
    lab2.configure(text = "shutdown a " + ent1.get() + "s after")
lab2.pack()

def error_box() :
    tkinter.messagebox.showerror("Limit Error!", "Range : 0-315360000(10y)")

class Main_funtion : 
    def shutdown_time(self) : 
        print_result()
        return os.system("shutdown -s -t " + ent1.get())
    def restart(self) :
        print_result()
        return os.system("shutdown -r -t " + ent1.get())
    def cancel(self) :
        return os.system("shutdown -a")

Activity_tool = Main_funtion()

button1 = tki.Button(tk, text = "shutdown time", command = Activity_tool.shutdown_time).place(x = 105, y = 90)
button2 = tki.Button(tk, text = "restart", command = Activity_tool.restart).place(x = 125, y = 120)
button3 = tki.Button(tk, text = "cancel", command = Activity_tool.cancel).place(x = 125, y = 150)

tk.mainloop()