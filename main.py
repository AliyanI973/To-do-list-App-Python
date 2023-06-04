
from customtkinter import *
import os


window = CTk()
frame = CTkFrame(window)


from sys import exit
def popupError(s):
    popupRoot = CTk()
    popupRoot.after(2000, exit)
    popupButton = CTkButton(popupRoot, text = s, font = ("Verdana", 12), command = exit) # , bg = "yellow"
    popupButton.pack()
    popupRoot.geometry('400x50+700+500')
    popupRoot.mainloop()

# dictionary for tasks where I can save each task with its key and remove, save, and done 

def add_task():
    global task_var, task
    task_var = StringVar()
    task = CTkCheckBox(scrollable_frame, text=entry.get("1.0", END), onvalue="yes", offvalue="no", variable=task_var)
    task.pack(side=TOP)
    entry.delete("1.0", END)

def save_task():
    with open(".task", "w") as t:
        t.writelines()

def done_task():
    pass

def remove_task():
    # try:
    #     for vars in task_var:
            if task_var.get() == "yes":
                if task:
                    task.pack_forget()
    # except NameError:
    #     popupError("No Check Buttons Found or selected")

    





scrollable_frame = CTkScrollableFrame(window, width=500, height=200)
entry = CTkTextbox(scrollable_frame, width=400, height=1)
add_btn = CTkButton(frame, text="Add Task", command=add_task)


add_btn.pack(side=LEFT, padx=20)
save_btn = CTkButton(frame, text="Save Tasks").pack(side=LEFT)
remove_btn = CTkButton(frame, text="Remove Task", command=remove_task).pack(side=LEFT, padx=20)
task_done = CTkButton(frame, text="Task Done").pack(side=LEFT)


"""         Buttons Positioning          """
entry.pack(fill=X)
scrollable_frame.pack()
frame.pack(pady=20)


window.mainloop()