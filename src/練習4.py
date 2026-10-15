import tkinter as tk

root = tk. Tk()
root.title("grid関数")
root.geometry('400x200')

# ウィジェットの数
WIDGET_MAX = 8

# Labelウィジェットのリストを生成
labels = [
    tk.Label(
        root,
        text="NO_"+str(num),
        relief=tk.SOLID
    )
    for num in range(WIDGET_MAX)
]

for i in range(4):
    root.columnconfigure(i, weight=1, uniform="columns")
for i in range(2):
    root.rowconfigure(i, weight=1, uniform="rows")

# grid関数で配置
# デフォルトでは、ウィジェットは左端に配置される
for num in range(WIDGET_MAX):
    if num < 4:
        labels[num].grid(column=num, row=0, padx=5, pady=5, sticky="nsew")
    else:
        labels[num].grid(column=num - 4, row=1, padx=5, pady=5, sticky="nsew")


root.mainloop()