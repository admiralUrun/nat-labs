import customtkinter as ctk
from customtkinter import CTkTabview, CTkLabel, CTkEntry

from Until import create_entries, auto_generate


class Lab2:
    def __init__(self, root: CTkTabview, name: str):
        tab = root
        self.frame = tab.add(name)
        frame = self.frame
        max_label = ctk.CTkLabel(frame, text="Середньоарифметичне між min & max: 0")
        max_label.grid(row=1, column=0, sticky="nsew", columnspan=10)

        self.entry_list = create_entries(0, 10, frame)

        generate_value_button = ctk.CTkButton(frame, text="Автозаповнення", command=lambda : auto_generate(self.entry_list))
        generate_value_button.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew", padx=10)

        find_max_button = ctk.CTkButton(frame, text="Знайти середньоарифметичне", command= lambda : find_average_between_max_min(self, max_label))
        find_max_button.grid(row=2, column=8, columnspan=2, pady=20, sticky="ew", padx=10)




def find_average_between_max_min(self, max_label: CTkLabel):
    int_list = [int(entry.get()) for _, entry in enumerate(self.entry_list) if entry.get().isdigit() or (entry.get().startswith('-') and entry.get()[1:].isdigit())]

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


