import os
import tkinter.messagebox
import tkinter as tki
import random

from setuptools import Command

tk = tki.Tk()
tk.geometry("450x250")
tk.title("Shutdown program")
tk.resizable(False, False)

top_text = tki.Label(tk)
top_text['text'] = "희망하는 시간(Time you want)"
top_text.pack()
limit_text_lab = tki.Label(tk)
limit_text_lab['text'] = "Range : 0-315360000(10y)"
limit_text_lab.pack()

Print_input_time_value = tki.Label(tk)
input_time_value = tki.Entry(tk)
# input_time_value.insert(tki.INSERT, "Enter Time(s)")   
input_time_value.pack()

Enter_text_Announce = tki.Label(tk)
Enter_text_Announce.configure(text = "↑ Enter Time(s) ↑")
Enter_text_Announce.pack()

def print_result() :
    Print_input_time_value.configure(text = "shutdown a " + input_time_value.get() + "s after")
def print_random_result() :
    Print_input_time_value.configure(text = "Ouch!")
Print_input_time_value.pack()


def error_box() :
    tkinter.messagebox.showerror("Limit Error!", "Range : 0-315360000(10y)")
    
# if (input_time_value.get() > "315360000" or input_time_value.get() < "0") and len(input_time_value.get()) != 0 :
#     error_box()

time_value_type = ""

def time_value_number():
    global time_value_type
    try:
        int(input_time_value.get())
        time_value_type = "INT"
    except ValueError:
        time_value_type = "NOT INT"

def verification_input_time() :
    if time_value_type == "NOT INT" :
            if int(input_time_value.get()) > 315360000 :
                error_box()
            if int(input_time_value.get()) < 0 :
                error_box()

class Main_funtion : 
    global time_value_type
    time_value_number()
    def shutdown_time(self) : 
        print_result()
        verification_input_time()
        return os.system("shutdown -s -t " + input_time_value.get())
    def restart(self) :
        print_result()
        verification_input_time()
        return os.system("shutdown -r -t " + input_time_value.get())
    def cancel(self) :
        return os.system("shutdown -a")


def random_print() : # 1/6 확률로 Ouch! 문자만 출력하고 카운트 + 1
        isRandomNum = random.randint(1, 6);
        isRandomOfCnt = 0
        print("randomNum : ", isRandomNum)
        if isRandomNum == 6 :
            tkinter.messagebox.showinfo(message="Oh")
            print_random_result()
            isRandomOfCnt += 1
        return isRandomOfCnt

randomOfCnt = random_print()
print(randomOfCnt)
print_get_six = tki.Label(tk)
print_get_six.configure(text = randomOfCnt)
print_get_six.pack()


            
Activity_tool = Main_funtion()

button1 = tki.Button(tk, text = "shutdown time", command = Activity_tool.shutdown_time).place(x = 120, y = 130)
button2 = tki.Button(tk, text = "random shutdown", command = random_print).place(x = 250, y = 130)
button3 = tki.Button(tk, text = "restart", command = Activity_tool.restart).place(x = 170, y = 170)
button4 = tki.Button(tk, text = "cancel", command = Activity_tool.cancel).place(x = 250, y = 170)

# if input_time_value.get() > "315360000":
#     print(len(input_time_value.get()))
#     error_box()

# if input_time_value.get() <= "315360000" and input_time_value.get() >= "0" :
#     Activity_tool = Main_funtion()
#     tki.Button(tk, text = "shutdown time", command = Activity_tool.shutdown_time).place(x = 105, y = 90)
#     tki.Button(tk, text = "restart", command = Activity_tool.restart).place(x = 125, y = 120)
#     tki.Button(tk, text = "cancel", command = Activity_tool.cancel).place(x = 125, y = 150)
    
# else :
#     tki.Button(tk, text = "shutdown time", command = error_box()).place(x = 105, y = 90)
#     tki.Button(tk, text = "restart", command = error_box()).place(x = 125, y = 120)
#     tki.Button(tk, text = "cancel", command = error_box()).place(x = 125, y = 150)
#     print(input_time_value.get())

    # error_box()
    

# if input_time_value.get() <= "315360000" and input_time_value.get() >= "0" :
#     button1['state'] = tki.ACTIVE
#     button2['state'] = tki.ACTIVE
#     button3['state'] = tki.ACTIVE
# else :
#     button1['state'] = tki.DISABLED
#     button2['state'] = tki.DISABLED
#     button3['state'] = tki.DISABLED    

tk.mainloop()