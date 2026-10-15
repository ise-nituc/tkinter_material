import tkinter as tk

root = tk. Tk()
root.title("grid関数")
root.geometry('400x200')

# Setup window's columns and rows
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=5)

# Label
text = tk.Label(root, text="abc")
text.grid(row=0, column=0, columnspan=3, pady=1)

# bottom frame
bottom_frame = tk.Frame(root)
bottom_frame.grid(
    row=1, column=0,
    sticky="nsew",
    padx=1, pady=1
)

# ウィジェットの数
WIDGET_MAX = 9

# Labelウィジェットのリストを生成
labels = [
    tk.Label(
        bottom_frame,
        text="NO_"+str(num),
        relief=tk.SOLID
    )
    for num in range(WIDGET_MAX)
]

for i in range(3):
    bottom_frame.columnconfigure(i, weight=1, uniform="columns")
    bottom_frame.rowconfigure(i, weight=1, uniform="rows")

# grid関数で配置
# デフォルトでは、ウィジェットは左端に配置される
for num in range(WIDGET_MAX):
    column = num % 3
    row = num // 3
    labels[num].grid(column=column, row=row, padx=5, pady=5, sticky="nsew")

root.mainloop()