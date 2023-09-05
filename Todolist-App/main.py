"""

"""
from customtkinter import CTk, CTkButton, CTkScrollableFrame, CTkTextbox, CTkFrame, X, LEFT, RIGHT,TOP, END, Variable, StringVar, CTkCheckBox
from tasksdb import SqDB
from utils import validate_entry_input


class ToDoApp:
    tkvar_list=[]
    tasks_list = []
    tasks = []


    def __init__(self, master):
        self.master =master
        self.master.title = "Todo App"
        self.frame = CTkFrame(self.master)

        self.scrollable_frame = CTkScrollableFrame(master, width=500, height=200)
        self.entry = CTkTextbox(self.scrollable_frame, width=400, height=1)
        self.add_btn = CTkButton(self.frame, text="Add Task", command=self.add_task)

        self.add_btn.pack(side=LEFT, padx=20)
        self.save_btn = CTkButton(self.frame, text="Save Tasks", command=self.save_task).pack(side=LEFT)
        self.remove_btn = CTkButton(self.frame, text="Remove Task", command=self.remove_task).pack(side=LEFT, padx=20)

        self.entry.pack(fill=X)
        self.scrollable_frame.pack()
        self.frame.pack(pady=20)


    def on_start(self):
        # append all task to varlist then creat checkbutton and append them to tasklist
        taskdb = SqDB()
        cm  = Variable()

        tupled_list = taskdb.retrieve_tasks()

        for tups in tupled_list:
            cm = StringVar(self.master)
            task = CTkCheckBox(self.scrollable_frame, text=tups[1],offvalue='no', onvalue='yes', variable=cm)
            task.pack(side=TOP)
            ToDoApp.tasks_list.append(task)
            ToDoApp.tkvar_list.append(cm)

        for task in ToDoApp.tasks_list:
            print(task)

    def add_task(self):
        global string_var, taskbtn, tasks_list
        checkboxes = []
        string_var = StringVar(self.master)
        
        taskbtn = CTkCheckBox(self.scrollable_frame, text=self.entry.get("1.0", END),offvalue='no', onvalue='yes', variable=string_var)
        taskbtn.pack(side=TOP)
        ToDoApp.tasks_list.append(taskbtn)

        ToDoApp.tkvar_list.append(string_var)
        task_string = self.entry.get("1.0", END)
        # print(ToDoApp.tasks)
        ToDoApp.tasks.append(tuple(task_string.strip()))
        self.entry.delete("1.0", END)


    def save_task(self):
        taskdb = SqDB()
        taskdb.rearrange_id()
        tupled_tasks = []
        for characters_tuple in ToDoApp.tasks:
            word = (lambda characters: ''.join(characters))(characters_tuple)
            tupled_tasks.append((word,))
        taskdb.add_task_db(tupled_tasks)

            
    def done_task():
        pass

    def remove_task(self):
        selected_indices = []

        taskdb = SqDB()
        
        for index, var in enumerate(ToDoApp.tkvar_list):
            if var.get() == 'yes':
                selected_indices.append(index)
                print(var)

        # Remove tasks in reverse order to avoid index changes
        for index in reversed(selected_indices):
            task = ToDoApp.tasks_list[index]
            task.destroy()
            taskdb.remove_task([(index+1,)])
            ToDoApp.tasks_list.pop(index)
            ToDoApp.tkvar_list.pop(index)
            
        
            
        # Clear the checkboxes
        for var in ToDoApp.tkvar_list:
            var.set('no')

        # for task in ToDoApp.tasks_list:
        #     print(task)

if __name__=='__main__':
    root = CTk()
    obj = ToDoApp(root)
    obj.on_start()
    root.mainloop()