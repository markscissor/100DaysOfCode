import tkinter as tk


def calculate():
    if input_mile.get().isdigit():
        mile = float(input_mile.get())
        km = mile * 1.60934
        result_label.config(text=f"{km:.2f}")
    else:
        result_label.config(text="ERROR", font=("Arial", 10))


window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

input_mile = tk.Entry(width=10)
input_mile.focus()
input_mile.grid(column=1, row=0)

mile_label = tk.Label(text="Miles", font=("Arial", 12))
mile_label.grid(column=2, row=0)
mile_label.config(padx=10)

is_equal_to_label = tk.Label(text="is equal to", font=("Arial", 12))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10)

result_label = tk.Label(text="", font=("Arial", 12))
result_label.grid(column=1, row=1)

km_label = tk.Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)
km_label.config(padx=10)

calculate_button = tk.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()
