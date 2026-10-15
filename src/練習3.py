import tkinter as tk

root = tk. Tk()
root.title("grid関数")
root.geometry('400x200')

# ウィジェットの数
WIDGET_MAX = 9

# Labelウィジェットのリストを生成
labels = [
    tk.Label(
        root,
        text="NO_"+str(num),
        relief=tk.SOLID
    )
    for num in range(WIDGET_MAX)
]

# grid関数で配置
# デフォルトでは、ウィジェットは左端に配置される
for num in range(WIDGET_MAX):
    row = num // 3
    col = num % 3
    labels[num].grid(column=col, row=row)

root.mainloop()