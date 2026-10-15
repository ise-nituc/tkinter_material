from tkinter import messagebox
import tkinter as tk


def show_message():
    messagebox.showinfo("Message", "Button clicked!")

def enter_message(event):
    messagebox.showinfo("Message", "Enter pressed!")

def close_program(event):
    if messagebox.askyesno("Warning", "Close the program?"):
        root.destroy()

root = tk.Tk()
root.title("Bind demo")
root.geometry("250x150")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

button = tk.Button(root, text="Click Me", command=show_message)
button.grid(row=0, column=0, padx=20, pady=20)

root.bind("<Escape>", close_program)
root.bind("<Return>", enter_message)

root.mainloop()