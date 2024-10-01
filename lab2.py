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

max_label=ctk.CTkLabel(frame, text= "Середньоарифметичне між min & max: 0")
max_label.grid(row=1, column=0, sticky="nsew", columnspan=10)

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

def find_average_between_max_min():
    int_list = [int(entry.get()) for _, entry in enumerate(entry_list) if entry.get().isdigit() or (entry.get().startswith('-') and entry.get()[1:].isdigit())]

    if int_list:
        max_i=0
        min_i=0
        for i, val in enumerate(int_list):
            if val > int_list[max_i]:
                max_i = i

            if val < int_list[min_i]:
                min_i = i

        if min_i < max_i:
            subarray = int_list[min_i:max_i + 1]
        else:
            subarray = int_list[max_i:min_i + 1]

        max_label.configure(text=f"Середньоарифметичне між {int_list[min_i]} та {int_list[max_i]}: {sum(subarray) / len(subarray)}")


generate_value_button = ctk.CTkButton(frame, text="Автозаповнення", command=auto_generate)
generate_value_button.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew", padx=10)


find_max_button = ctk.CTkButton(frame, text="Знайти середньоарифметичне", command=find_average_between_max_min)
find_max_button.grid(row=2, column=6, columnspan=4, pady=20, sticky="ew", padx=10)


app.mainloop()