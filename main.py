
from customtkinter import *
import os
from tkinter import Widget
from sys import exit

window = CTk()
frame = CTkFrame(window)

# dictionary for tasks where I can save each task with its key and remove, save, and done 
var_list=[]
# string_var = {}
tasks_list = []
tasks = []


def on_start():
    # append all task to varlist then creat checkbutton and append them to tasklist
    cma  = Variable()
    
    with open(".task", "r") as t:
        vars = t.readlines()
        
        for var in vars:
            var.strip()
            cm = StringVar(window)
            task = CTkCheckBox(scrollable_frame, text=var,offvalue='no', onvalue='yes', variable=cm)
            task.pack(side=TOP)
            tasks_list.append(task)
            var_list.append(cm)

    for task in tasks_list:
        print(task)


def popupError(s):
    popupRoot = CTk()
    popupRoot.after(2000, exit)
    popupButton = CTkButton(popupRoot, text = s, font = ("Verdana", 12), command = exit) # , bg = "yellow"
    popupButton.pack()
    popupRoot.geometry('400x50+700+500')
    popupRoot.mainloop()


def add_task():
    global task_var, taskbtn, tasks_list
    checkboxes = []
    task_var = StringVar(window)
    # place a loop here or a function and create same name variables for checkbutton and chatgpt
    taskbtn = CTkCheckBox(scrollable_frame, text=entry.get("1.0", END),offvalue='no', onvalue='yes', variable=task_var)
    taskbtn.pack(side=TOP)
    tasks_list.append(taskbtn)

    var_list.append(task_var)
    task_string = entry.get("1.0", END)
    tasks.append(task_string.strip())
    entry.delete("1.0", END)



def save_task():
    with open(".task", "w") as t:
        for var in tasks:
            t.write(var +'\n')
        


def done_task():
    pass

def remove_task():
    selected_indices = []
    f = open('.task')
    tt = f.readlines()

    for index, var in enumerate(var_list):
        if var.get() == 'yes':
            selected_indices.append(index)

    # Remove tasks in reverse order to avoid index changes
    for index in reversed(selected_indices):
        task = tasks_list[index]
        task.destroy()
        tasks_list.pop(index)
        var_list.pop(index)
        del tt[index - 1]

        f.write()
        print(tt[index])
        

        

    # Clear the checkboxes
    for var in var_list:
        var.set('no')


    for task in tasks_list:
        print(task)

    


    
    # try:
    #     for vars in task_var:
    # if task_var.get() == True:
    #     if task:
    #         task.destroy()
                    #task_var.trace_add('read')
    # except NameError:
    #     popupError("No Check Buttons Found or selected")

# First Use Labels then learn to work with check boxes
# Instead of StringVar use IntVar
# Use Trace to track the changes
# Might Need list to create multiple instances of checkbuttons
# Track add_btn? for every time called create an instance
# Checkbtn can be Boolean
# Multiple Objects
#.Checkbutton address


scrollable_frame = CTkScrollableFrame(window, width=500, height=200)
entry = CTkTextbox(scrollable_frame, width=400, height=1)
add_btn = CTkButton(frame, text="Add Task", command=add_task)


add_btn.pack(side=LEFT, padx=20)
save_btn = CTkButton(frame, text="Save Tasks", command=save_task).pack(side=LEFT)
remove_btn = CTkButton(frame, text="Remove Task", command=remove_task).pack(side=LEFT, padx=20)
# task_done = CTkButton(frame, text="Task Done").pack(side=LEFT)


"""         Buttons Positioning          """
entry.pack(fill=X)
scrollable_frame.pack()
frame.pack(pady=20)


if __name__ =="__main__":
    on_start()
    window.mainloop()