import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()  # Створення головного вікна
app.geometry("800x300")
app.title("Моя програма")

def button_function():
    print("Кнопка натиснута")


# Create an array (list) to store the CTkEntry widgets
entry_list = []

def create_entries(num_entries):
    for i in range(num_entries):
        entry = ctk.CTkEntry(app, placeholder_text=f"Entry {i+1}")
        entry.grid(row=0, column=i, padx=10, pady=10)  # Place each entry in a single row
        entry_list.append(entry)  # Store each entry widget in the list

# Create 5 CTkEntry widgets in one line
create_entries(5)

button1 = ctk.CTkButton(master=app, text="Натисни мене", command=button_function)
button2 = ctk.CTkButton(master=app, text="Натисни мене", command=button_function)


button1.grid(row=1, column=0, columnspan=30, pady=20)
button2.grid(row=1, column=1, pady=20)

app.mainloop()