import pandas as pd
import tkinter as tk
from tkinter import messagebox
import csv
import os
from tkinter import filedialog
import datetime
from tkinter import ttk
from dotenv import load_dotenv

root = tk.Tk()
root.title("Карточка учета материалов")
pd.options.display.float_format = '{:.0f}'.format
load_dotenv()

sub = os.getenv("sub")
org = os.getenv("org")
worktype = os.getenv("worktype")
warehouse = os.getenv("warehouse")
rack = os.getenv("rack")
cell = os.getenv("cell")
brand = os.getenv("brand")
sort = os.getenv("sort")
profile = os.getenv("profile")
size = os.getenv("size")
nomenclature = os.getenv("nomenclature")
code = os.getenv("code")
name = os.getenv("name")
price = os.getenv("price")
norm = os.getenv("norm")
expire = os.getenv("expire")
supplier = os.getenv("supplier")
from_to = os.getenv("from_to")
unit = os.getenv("unit")
debit = os.getenv("debit")
credit = os.getenv("credit")
remainder = os.getenv("remainder")

df_warehouse = pd.DataFrame(
    columns=[sub, worktype, warehouse, rack, cell, brand, sort, profile, size, nomenclature, code, name, price, norm,
             expire, supplier])
df_movement = pd.DataFrame(columns=[from_to, unit, debit, credit, remainder])


def import_organization(structural_combo, organization_combo):
    """
    Imports organization data from a CSV file, creates a DataFrame, and updates values for combo boxes.

    Parameters:
        structural_combo (tkinter Combobox): The Combobox for structural data selection.
        organization_combo (tkinter Combobox): The Combobox for organization data selection.

    Returns:
        None
    """
    global df_organization
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )
    table_path = filedialog.askopenfile(mode="r", filetypes=filetypes)
    with open(table_path.name, encoding="utf-8-sig") as file:
        data = csv.reader(file)
        header = next(data)
        data = list(data)
        df_organization = pd.DataFrame(data, columns=header)
        messagebox.showinfo("Импорт данных", "Данные успешно импортированы")
    structural_combo['values'] = list(df_organization[sub].unique())
    organization_combo['values'] = list(df_organization[org].unique())


def import_defaults():
    global df_defaults
    """
    Imports default data from a CSV file and updates the global DataFrame `df_defaults`.

    This function prompts the user to select a CSV file using a file dialog. The selected file is read using the 
    `csv.reader` function and its contents are stored in the `data` variable. The first row of the `data` is used as 
    the header for the DataFrame. The remaining rows are converted to a list and stored in the `data` variable.

    The imported data is then used to create a new DataFrame `df_defaults` using the `pd.DataFrame` constructor. The 
    `data` is passed as the data for the DataFrame and the `header` is used as the column names.

    After the DataFrame is created, a message box is displayed using `messagebox.showinfo` to inform the user that 
    the data has been successfully imported.

    Parameters:
    - None

    Returns:
    - None
    """
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )
    table_path = filedialog.askopenfile(mode="r", filetypes=filetypes)
    with open(table_path.name, encoding="utf-8-sig") as file:
        data = csv.reader(file)
        header = next(data)
        data = list(data)
        df_defaults = pd.DataFrame(data, columns=header)
        messagebox.showinfo("Импорт данных", "Данные успешно импортированы")


def first_window_func():
    """
    A function that sets up the first window interface by creating frames, buttons, comboboxes, and labels.
    """
    global first_window

    first_window = tk.Frame(root)
    first_window.pack(fill='both', expand=True)

    frame_data = tk.Frame(first_window)
    frame_data.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    frame_import = tk.Frame(first_window)
    frame_import.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    tk.Button(frame_import, text="Импорт данных по умолчанию", command=import_defaults).grid(row=0, column=1, padx=5,
                                                                                             pady=5)
    tk.Button(frame_import, text="Импорт организации",
              command=lambda: import_organization(structural_combo, organization_combo)).grid(row=0, column=0, padx=5,
                                                                                              pady=5)

    organization_combo = ttk.Combobox(frame_data)
    organization_combo.grid(row=0, column=1, padx=5, pady=5)
    tk.Label(frame_data, text="Организация:").grid(row=0, column=0, padx=5, pady=5)

    structural_combo = ttk.Combobox(frame_data)
    structural_combo.grid(row=1, column=1, padx=5, pady=5)
    tk.Label(frame_data, text="Структурное подразделение:").grid(row=1, column=0, padx=5, pady=5)

    material_entry = tk.Entry(frame_data)
    material_entry.grid(row=2, column=1, padx=5, pady=5)
    tk.Label(frame_data, text="Материал:").grid(row=2, column=0, padx=5, pady=5)

    tk.Button(first_window, text="Далее", command=second_window_func).grid(row=10, column=0, columnspan=2, pady=10)


def second_window_func():
    """
    Creates and displays the second window of the GUI application.

    This function initializes the second window and hides the first window. It then creates two frames within the
    second window: `second_window_data` and `second_window_navigation`. The `second_window_data` frame is used to
    display input fields for each column in the `df_warehouse` DataFrame. The `second_window_navigation` frame is
    used to display navigation buttons.

    The function iterates over each column in the `df_warehouse` DataFrame and creates a corresponding input field
    and label within the `second_window_data` frame. The input field is bound to the corresponding cell in the
    `df_warehouse` DataFrame. The label displays the column name.

    The function also creates two buttons within the `second_window_navigation` frame. The "Назад" button is used to
    navigate back to the first window and the "Далее" button is used to save the input data and navigate to the third
    window.

    Parameters:
    None

    Returns:
    None
    """
    global second_window, df_warehouse
    second_window = tk.Frame(root)
    first_window.pack_forget()
    second_window.pack(fill='both', expand=True)

    second_window_data = tk.Frame(second_window)
    second_window_data.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    second_window_navigation = tk.Frame(second_window)
    second_window_navigation.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    for i, field in enumerate(df_warehouse.columns.tolist()):
        df_warehouse.at[0, field] = tk.Entry(second_window_data)
        df_warehouse.at[0, field].grid(row=i, column=1, padx=5, pady=5)
        tk.Label(second_window_data, text=field).grid(row=i, column=0, padx=5, pady=5)

    tk.Button(second_window_navigation, text="Назад",
              command=lambda: [second_window.pack_forget(), first_window_func()]).grid(
        row=0,
        column=0,
        padx=5,
        pady=5)
    tk.Button(second_window_navigation, text="Далее", command=lambda: [save_second(), third_window_func()]).grid(
        row=0,
        column=1,
        padx=5,
        pady=5)


def third_window_func():
    """
    A function to handle the third window of the GUI application.
    Sets up the third window layout, populates a Treeview widget, and creates input fields based on DataFrame columns.
    Manages navigation buttons for saving data and transitioning to other windows.
    """
    global third_window
    third_window = tk.Frame(root)
    tree_window = tk.Frame(third_window)
    tree_window.grid(row=0, column=0, padx=5, pady=5)
    second_window.pack_forget()
    third_window.pack(fill='both', expand=True)
    tree = ttk.Treeview(tree_window)
    tree.grid(row=0, column=0, padx=5, pady=5)
    df_movement_col = tuple(df_movement.columns.values)
    tree['columns'] = df_movement_col
    tree_create(tree, df_movement_col)
    third_window_data = tk.Frame(third_window)
    third_window_data.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    for i, j in enumerate(df_movement.columns.tolist()[:-1]):
        df_movement.at[0, j] = tk.Entry(third_window_data)
        df_movement.at[0, j].grid(row=i, column=1, padx=5, pady=5)
        tk.Label(third_window_data, text=j).grid(row=i, column=0, padx=5, pady=5)

    third_window_navigation = tk.Frame(third_window)
    third_window_navigation.grid(row=10, column=0, columnspan=2, padx=5, pady=5)
    tk.Button(third_window_navigation, text="Назад",
              command=lambda: [third_window.pack_forget(), second_window_func()]).grid(
        row=0,
        column=0,
        padx=5,
        pady=5)
    tk.Button(third_window_navigation, text="Сохранить", command=lambda: save_third(tree, df_movement_col)).grid(
        row=0,
        column=1,
        padx=5,
        pady=5)
    tk.Button(third_window_navigation, text="Удалить последний",
              command=lambda: delete_last(tree, df_movement_col)).grid(
        row=0,
        column=2,
        padx=5,
        pady=5)
    tk.Button(third_window_navigation, text="Сохранить в Excel", command=save_excel).grid(
        row=0,
        column=3,
        padx=5,
        pady=5)
    tk.Button(third_window_navigation, text="Сохранить в текстовый файл", command=save_text).grid(
        row=0,
        column=4,
        padx=5,
        pady=5)


def tree_create(tree, df_movement_col):
    """
    Creates a Treeview widget with columns and rows based on the given DataFrame.

    Parameters:
    - tree (ttk.Treeview): The Treeview widget to be populated.
    - df_movement_col (list): A list of column names for the DataFrame.

    Returns:
    None
    """
    for i in range(len(df_movement_col)):
        tree.column(i, width=100, anchor='center')
        tree.heading(i, text=df_movement_col[i])
    for i in tree.get_children():
        tree.delete(i)
    for i in range(len(df_movement)):
        if i == 0:
            continue
        tree.insert('', 'end', text=i, values=tuple(df_movement.iloc[i].values))
    tree.pack()


def delete_last(tree, df_movement_col):
    """
    Deletes the last row from the global DataFrame `df_movement` and updates the Treeview widget `tree` accordingly.

    Parameters:
    - tree (ttk.Treeview): The Treeview widget to be updated after deleting the last row.
    - df_movement_col (list): A list of column names for the DataFrame.

    Returns:
    None
    """
    global df_movement
    df_movement = df_movement.iloc[:-1]
    tree_create(tree, df_movement_col)


def save_text():
    """
    Save the contents of the global DataFrame `df_movement` and `df_defaults` to a text file named 'export.txt'.

    This function opens the file 'export.txt' in write mode and writes the contents of the DataFrames `df_defaults`
    and `df_warehouse` to the file. The DataFrame `df_defaults` is written using the `to_markdown` method with the
    `index` parameter set to `False`. The DataFrame `df_warehouse` is written in a similar manner. After writing the
    contents of `df_defaults` and `df_warehouse`, the function creates a copy of `df_movement` excluding the first
    row and writes it to the file.

    Parameters:
    None

    Returns:
    None
    """
    global df_movement
    with open('export.txt', 'w') as f:
        f.write(df_defaults.to_markdown(index=False))
        f.write("\n\n\n\n")
        f.write(df_warehouse.to_markdown(index=False))
        f.write("\n\n\n\n")
        df_mov_export = df_movement.iloc[1:].copy()
        f.write(df_mov_export.to_markdown(index=False))


def save_excel():
    """
    Save the contents of the global DataFrame `df_movement` to Excel files.

    This function creates a copy of the `df_movement` DataFrame excluding the first row and saves it to an Excel file
    named 'movement.xlsx'. It also saves the contents of the global DataFrame `df_warehouse` to an Excel file named
    'warehouse.xlsx', without including the index.

    Parameters:
    None

    Returns:
    None
    """
    global df_movement
    df_mov_export = df_movement.iloc[1:].copy()
    df_warehouse.to_excel('warehouse.xlsx', index=False)
    df_mov_export.to_excel('movement.xlsx', index=False)


def save_third(tree, df_movement_col):
    """
    Save data from the Treeview widget and global DataFrame `df_movement` to the global DataFrame `df_movement`.

    Parameters:
    - tree (ttk.Treeview): The Treeview widget from which to extract data.
    - df_movement_col (list): A list of column names for the DataFrame.

    Returns:
    None

    This function appends a new row to the global DataFrame `df_movement` with `None` values for all columns. It then
    iterates over the columns in `df_movement_col` except for the last one. If the column is either `debit` or
    `credit`, it checks if the corresponding entry in the first row of `df_movement` is empty. If it is, it sets the
    corresponding value in the last row of `df_movement` to 0 and continues to the next iteration. Otherwise,
    it tries to convert the value to a float and sets it in the last row of `df_movement`. If the conversion fails,
    it displays an error message and removes the last row from `df_movement`. If the column is not `debit` or
    `credit`, it sets the corresponding value in the last row of `df_movement` to the value in the first row of
    `df_movement`. After iterating over all columns, if no error occurred, it calculates the remainder by subtracting
    `credit` from `debit` and sets it in the last row of `df_movement`. Finally, it calls the `tree_create` function
    to update the Treeview widget with the new data.
    """
    global df_movement
    df_movement.loc[len(df_movement)] = [None] * len(df_movement_col)
    error_occured = False
    for i, j in enumerate(df_movement_col[:-1]):
        if j in [debit, credit]:
            if df_movement.iloc[0, i].get() == "":
                df_movement.iloc[-1, i] = 0
                continue
            try:
                df_movement.iloc[-1, i] = float(df_movement.iloc[0, i].get())
                continue
            except:
                messagebox.showerror("Ошибка", "Некорректные данные")
                df_movement = df_movement.iloc[:-1]
                break
        df_movement.iloc[-1, i] = df_movement.iloc[0, i].get()
    if not error_occured:
        df_movement[remainder].iloc[-1] = df_movement[debit].iloc[-1] - df_movement[credit].iloc[-1]
        tree_create(tree, df_movement_col)


def save_second():
    """
    Save the contents of the global DataFrame `df_warehouse` after converting specific fields to float.
    """
    global df_warehouse
    pass
    error_occured = False
    for i, field in enumerate(df_warehouse.columns.tolist()):
        if error_occured:
            break
        if field in [worktype, warehouse, rack, size, nomenclature]:
            try:
                df_warehouse.at[0, field] = float(df_warehouse.at[0, field])
            except:
                error_occured = True
                messagebox.showerror("Ошибка", "Некорректные данные")
                break
        else:
            df_warehouse.at[0, field] = df_warehouse.at[0, field].get()


first_window_func()

root.mainloop()
