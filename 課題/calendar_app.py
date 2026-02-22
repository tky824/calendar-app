import tkinter as tk
from tkcalendar import Calendar

#ウィンドウ作成
root = tk.Tk()
root.title("カレンダーアプリ")

#カレンダー作成
cal = Calendar(root, selectmode='day')
cal.pack(pady=20)
# 目標入力欄
entry = tk.Entry(root, width=30)
entry.pack()

# 表示用ラベル
label = tk.Label(root, text="")
label.pack()
# 目標保存用の辞書
goals = {}

# ボタンが押されたときの処理
def save_goal():
    date = cal.get_date()
    goal = entry.get()
    goals[date] = goal
    label.config(text=f"{date} の目標: {goal}")

# 保存ボタン
button = tk.Button(root, text="目標を保存", command=save_goal)
button.pack(pady=10)

#画面表示
root.mainloop()