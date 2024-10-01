from random import randrange
import customtkinter as ctk

app = ctk.CTk()
app.geometry("800x400")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

frame = ctk.CTkFrame(app)
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")



frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
frame.grid_rowconfigure(0, weight=1)

max_label=ctk.CTkLabel(frame, text= "Максимум: 0")
max_label.grid(row=1, column=3, sticky="nsew", columnspan=4)

entry_list = []

def create_entries(num_entries):
    for i in range(num_entries):
        entry = ctk.CTkEntry(frame, placeholder_text=f"{i}")
        entry.grid(row=0, column=i, padx=10, pady=10, sticky="ew")
        entry_list.append(entry)

create_entries(10)

def auto_generate():
    for i, entry in enumerate(entry_list):
        entry.delete(0, "end")
        entry.insert(0, str(randrange(100)))

def find_max():
    int_list = [int(entry.get()) for _, entry in enumerate(entry_list) if entry.get().isdigit() or (entry.get().startswith('-') and entry.get()[1:].isdigit())]

    if int_list:
        max_label.configure(text=f"Максимум: {max(int_list)}")


generate_value_button = ctk.CTkButton(frame, text="Автозаповнення", command=auto_generate)
generate_value_button.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew", padx=10)


find_max_button = ctk.CTkButton(frame, text="Знайти максимум", command=find_max)
find_max_button.grid(row=2, column=8, columnspan=2, pady=20, sticky="ew", padx=10)


app.mainloop()