import tkinter as tk

root = tk.Tk()
root.title("Grid Layout Example")
root.geometry("500x300")

# Main grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)
root.rowconfigure(0, weight=1)

# Left frame
left_frame = tk.Frame(root, bd=1, relief="solid")
left_frame.grid(
    row=0, column=0,
    sticky="nsew",
    padx=10, pady=10
)

# Right frame
right_frame = tk.Frame(root, bd=1, relief="solid")
right_frame.grid(
    row=0, column=1,
    sticky="nsew",
    padx=10, pady=10
)

# Right frame grid
right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(0, weight=1)

# Large upper area
main_frame = tk.Frame(right_frame, bd=1, relief="solid")
main_frame.grid(
    row=0, column=0,
    sticky="nsew",
    padx=10, pady=10
)

# Frame for buttons
button_frame = tk.Frame(right_frame)
button_frame.grid(
    row=1, column=0,
    sticky="e",
    padx=5, pady=10
)

button1 = tk.Button(button_frame, text="Button 1")
button1.grid(row=0, column=0, padx=5)

button2 = tk.Button(button_frame, text="Button 2")
button2.grid(row=0, column=1, padx=5)

root.mainloop()