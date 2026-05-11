import webbrowser
import re
import random
import tkinter as tk

def calculate():
    try:
        raw_input = entry.get().strip().replace(" ", "").replace(".", "*").replace(":", "/")
        
        if not raw_input:
            status_label.config(text="Error: Your math is too ugly to process.\nType more beautiful math or get out", fg="orange")
            return

        if "/0" in raw_input:
            status_label.config(text="DIVIDING BY ZERO? REALLY?", fg="red")
            result_label.config(text=f"Result: -1")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            return

        if not re.fullmatch(r"[0-9\+\-\*\/\(\)\s]+", raw_input):
            status_label.config(text="Nice try, Hacker. No system commands!", fg="red")
            return

        real_answer = eval(raw_input)
        offset = random.choice([random.randint(1, 5), -random.randint(2, 6), 0.69])
        fake_answer = round(real_answer + offset, 2)
        
        result_label.config(text=f"Result: {fake_answer}")
        status_label.config(text="Confidence: 0.00069% - trust me bro.")
        
    except Exception:
        status_label.config(text="Error: Your math is too ugly to process. Type more beautiful math or get out.", fg="orange")

root = tk.Tk()
root.title("CircuitBuddy Gaslight Calc")
root.geometry("300x180")

tk.Label(root, text="Enter Math (e.g. 2+2):").pack()
entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Calculate Truth*", command=calculate)
btn.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"))
result_label.pack()

status_label = tk.Label(root, text="Waiting for your inevitable mistake...", fg="red")
status_label.pack(side="bottom", pady=15)

root.mainloop()
