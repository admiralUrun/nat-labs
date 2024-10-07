import customtkinter as ctk
from customtkinter import CTkTabview, CTkLabel

from Until import create_entries, auto_generate


class Lab1:
    def __init__(self, root: CTkTabview, name: str):
        tab = root
        self.frame = tab.add(name)
        frame = self.frame
        max_label=ctk.CTkLabel(frame, text= "Максимум: 0")
        max_label.grid(row=1, column=3, sticky="nsew", columnspan=4)

        self.entry_list = create_entries(10, frame)

        generate_value_button = ctk.CTkButton(frame, text="Автозаповнення", command=lambda: auto_generate(self.entry_list))
        generate_value_button.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew", padx=10)

        find_max_button = ctk.CTkButton(frame, text="Знайти максимум", command= lambda: self.find_max(self.entry_list, max_label))
        find_max_button.grid(row=2, column=8, columnspan=2, pady=20, sticky="ew", padx=10)


    @staticmethod
    def find_max(entry_list, max_label: CTkLabel):
        int_list = [int(entry.get()) for _, entry in enumerate(entry_list) if entry.get().isdigit() or (entry.get().startswith('-') and entry.get()[1:].isdigit())]

        if int_list:
            max_label.configure(text=f"Максимум: {max(int_list)}")
