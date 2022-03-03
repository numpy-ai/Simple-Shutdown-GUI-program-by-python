import os
from tkinter import*

tk = Tk()
tk.geometry("250x250")
tk.title("시간 지정 셧다운(여러 가지 추가 예정)")

lab1 = Label(tk)
lab1['text'] = "희망하는 n초 후의 종료 시간"
lab1.pack()

lab2 = Label(tk)
def result(n) :
    lab2.config(text = ent1.get() + "초 후에 종료됩니다.")

def shutdown_time() : 
    return os.system("shutdown -s -t " + ent1.get())
def shutdown_cancel() :
    return os.system("shutdown -a")

ent1 = Entry(tk)
ent1.bind("<Return>", result)
ent1.pack()
lab2.pack()

Button(tk, text = "shutdown_time", command = shutdown_time).place(x = 80, y = 100)
Button(tk, text = "shutdown_cancel", command = shutdown_cancel).place(x = 75, y = 150)

tk.mainloop()