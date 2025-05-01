# import Statements
import tkinter
from tkinter import *
from tkinter import messagebox

FONT = 'Georgia'

# add function
def add_task():
    task = entry_box.get()

    if task:
        # check if the user letter is less than 3
        if  len(task) < 3:
            messagebox.showerror(message="Warning, you can't add less than three letters.")

        else:
            items_box.insert(END,'\u2022' + task)
            entry_box.delete(0, END)

    # tell the use they can't add an empty task.
    else:
        messagebox.showerror(message="You can't add an empty task name.")


# delete function
def delete_task():
    
    delete_task = items_box.curselection()

    if delete_task:
        items_box.delete(delete_task[0])

    else:
        messagebox.showerror(message="Select an item you want to delete.")


# store the task in txt file
file_name = "task_store.txt"
def save_tasks():
    with open(file_name, 'w') as task_file:
        to_do_tasks = items_box.get(0, END)
        for task in to_do_tasks:
            task_file.write(f'{task}\n')

        # update_items = items_box.delete(0, END)
        # for task in to_do_tasks:
        #     items_box.insert(END, task)
        
            


##--------------------------------UI---------------------------------------##
window = tkinter.Tk()
window.title("To Do App")
window.geometry('400x500')
window.resizable(False, False)

# app heading
heading = Label(text="To Do List", font=(FONT, 24, 'bold'))
heading.pack(pady=10)

# list of the task that will be showen as defualt to do.
items_box = Listbox(window, background='lightblue', width=20, height=10, font=(FONT, 16, 'italic'))
items_box.pack(pady=10, padx=10)


    
# list of items
list_items =[
    "Practice Coding",
    "Exercise", "Reading Book", "Typing",
    ]

bullet_point = "\u2022" # unicode character

# add list to the list box
for list_item in list_items:
    print(list_item)
    items_box.insert(END, f"{bullet_point} {list_item}\n")

# entry box
entry_box = Entry(font=(FONT, 16, 'italic'), fg='blue')
entry_box.pack()

# add button
add_btn = Button(text='Add Task', background='green', font=(FONT, 12, 'bold'), fg='white', command=add_task)
add_btn.pack(pady=5, padx=5)

# delete button
delete_btn = Button(text='Delete Task', background='red', font=(FONT, 12, 'bold'), fg='white', command=delete_task)
delete_btn.pack(pady=5, padx=5)

# call save function
# save_tasks()
save_btn = Button(text="Save", bg='yellow', command=save_tasks)
save_btn.pack()

window.mainloop()
