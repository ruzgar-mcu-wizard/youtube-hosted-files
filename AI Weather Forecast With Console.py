import tkinter as tk
from tkinter import ttk

def start_check():
    win2 = tk.Toplevel(root)
    win2.title("AI weather forecast")
    win2.geometry("235x110")

    progress = ttk.Progressbar(win2, length=180, mode='determinate')
    progress.pack(side="bottom", pady=10)

    status = tk.Label(win2, text="", font=("Arial", 9))
    status.pack(pady=20)

    def update(p=0):
        progress['value'] = p

        if p <= 25:
            status.config(text="Searching location...")
        elif p <= 50:
            status.config(text="Analyzing the clouds...")
        elif p <= 75:
            status.config(text="Looking outside your window...")
        elif p < 100:
            status.config(text="Gathering last information...")

        if p >= 100:
            win2.destroy()
            win3 = tk.Toplevel(root)
            win3.title("")
            win3.geometry("165x70")

            tk.Label(win3, text="Idk, just look outside.", font=("Arial", 9)).pack(expand=True)
            return

        win2.after(80, lambda: update(p + 1))

    update()


root = tk.Tk()
root.title("AI weather forecast")
root.geometry("300x130")

tk.Label(root, text="Enter your location:").pack(pady=10)

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check weather", command=start_check).pack(pady=20)

root.mainloop()
