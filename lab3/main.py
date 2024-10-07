from Until import TwoDimensionalArray
import customtkinter as ctk

from lab1 import Lab1
from lab2 import Lab2
from lab3 import Lab3


def main():
    root = ctk.CTk()
    root.geometry("2400x2400")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    main_frame = ctk.CTkFrame(root)
    main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=0)
    main_frame.grid_rowconfigure(2, weight=0)
    main_frame.grid_columnconfigure(0, weight=1)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    tabview = ctk.CTkTabview(main_frame)
    tabview.pack(expand=True, fill="both", padx=10, pady=10)

    Lab1(tabview, "Лабораторна 1")
    Lab2(tabview, "Лабораторна 2")
    Lab3(tabview, "Лабораторна 3")

    rows, cols = 5, 5
    array_obj = TwoDimensionalArray(rows, cols)

    array_obj.fill_random()

    root.mainloop()

if __name__ == "__main__":
    main()
