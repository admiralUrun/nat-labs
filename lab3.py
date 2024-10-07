import customtkinter as ctk

from Until import create_entries, auto_generate


def find_min_max(all_entries: list[list[ctk.CTkEntry]]) -> (int, int):
    flat_list = [int(entry.get()) for sublist in all_entries for entry in sublist  if entry.get().isdigit() or (entry.get().startswith('-') and entry.get()[1:].isdigit())]
    return min(flat_list), max(flat_list)


def handel_click_min_and_max(max_label:ctk.CTkLabel, min_label:ctk.CTkLabel, all_entries: list[list[ctk.CTkEntry]]):
    min, max = find_min_max(all_entries)

    max_label.configure(text=f"max: {max}")
    min_label.configure(text=f"min: {min}")


class Lab3:
    def __init__(self, root: ctk.CTkTabview, name: str):
        tab = root
        self.frame = tab.add(name)
        frame = self.frame

        all_entries: list[list[ctk.CTkEntry]] = [[]]

        for i in range(5):
            all_entries.append(create_entries(i, 5, frame))

        last_available_row = len(all_entries) + 1

        max_label = ctk.CTkLabel(frame, text="max: 0")
        max_label.grid(row=last_available_row, column=0, sticky="nsew", columnspan=1)

        min_label = ctk.CTkLabel(frame, text="max: 0")
        min_label.grid(row=last_available_row, column=4, sticky="nsew", columnspan=1)

        last_available_row += 1

        def for_each():
            for es in all_entries:
                auto_generate(es)

        generate_value_button = ctk.CTkButton(frame, text="Автозаповнення", command=for_each)
        generate_value_button.grid(row=last_available_row, column=0, columnspan=2, pady=20, sticky="ew", padx=10)

        find_max_button = ctk.CTkButton(frame, text="Знайти max $ min", command=lambda: handel_click_min_and_max(max_label, min_label, all_entries))
        find_max_button.grid(row=last_available_row, column=8, columnspan=2, pady=20, sticky="ew", padx=10)





