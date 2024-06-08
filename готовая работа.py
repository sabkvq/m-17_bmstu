import tkinter as tk
from tkinter import messagebox, Radiobutton
import csv
import os


def fill_csv():
    file_exists_1 = os.path.isfile("initial_data.csv")
    is_non_empty_1 = os.path.getsize("initial_data.csv") > 0 if file_exists_1 else False
    # -----------------------------------------------------------------------------------------------------------------------
    with open("initial_data.csv", "a", newline="") as file_1:
        wt = csv.writer(file_1, delimiter=';')
        if not is_non_empty_1:
            wt.writerow(['ORG', 'OKUD', 'OKPO', 'DATE', 'SUB'])
        org = organization_entry.get()
        okud = okud_entry.get()
        okpo = okpo_entry.get()
        date = date_entry.get()
        sub = subdivision_entry_1.get()
        wt.writerow([org, okud, okpo, date, sub])
    # -----------------------------------------------------------------------------------------------------------------------
    file_exists_2 = os.path.isfile("fist.csv")
    is_non_empty_2 = os.path.getsize("fist.csv") > 0 if file_exists_2 else False

    with open("fist.csv", "a", newline="") as file_2:
        tw = csv.writer(file_2, delimiter=';')
        if not is_non_empty_2:
            tw.writerow(
                ['ST_DIVISION', 'ACTIVITY', 'WAREHOUS', 'MARK', 'SORT', 'PROFILE', 'SIZE', 'NUM_MUNBER', 'MEASURE',
                 'PRICE', 'EXPIRATION_DATE', 'SUPPLIER', 'MATERIAL'])
        st = subdivision_entry_2.get()
        ac = activity_entry.get()
        wr = warehous_entry.get()
        mr = mark_entry.get()
        s = sort_entry.get()
        pr = profile_entry.get()
        si = size_entry.get()
        num = num_number_entry.get()
        meas = measure_entry.get()
        pri = price_entry.get()
        ex = expiration_date_entry.get()
        sup = supplier_entry.get()
        ma = material_entry.get()
        tw.writerow([st, ac, wr, mr, s, pr, si, num, meas, pri, ex, sup, ma])

    # -----------------------------------------------------------------------------------------------------------------------
    file_exists_3 = os.path.isfile("initial_data.csv")
    is_non_empty = os.path.getsize("initial_data.csv") > 0 if file_exists_3 else False

    with open("metal.csv", "a", newline="") as file:
        q = csv.writer(file, delimiter=';')
        if not is_non_empty:
            q.writerow(['NAME', 'VIEW', 'NUMEN_NUMBER', 'MEASURE1', 'NUMBER', 'NAMEOFPASPORT'])
        n = name_entry.get()
        v = view_entry.get()
        nu = numen_number_entry.get()
        m = measure1_entry.get()
        num = number_entry.get()
        nameof = nameofpasport_entry.get()
        q.writerow([n, v, nu, m, num, nameof])
    # -----------------------------------------------------------------------------------------------------------------------
    file_exists_4 = os.path.isfile("last.csv")
    is_non_empty = os.path.getsize("last.csv") > 0 if file_exists_4 else False

    with open("last.csv", "a", newline="") as file:
        w = csv.writer(file, delimiter=';')
        if not is_non_empty:
            w.writerow(['DATE2', 'NUMERR', 'FROMTO', 'ACOUNTINGUNIT', 'PROFIT', 'SPENT', 'LEFT', 'LASTNAME'])
        d = date2_entry.get()
        nn = numerr_entry.get()
        f = fromto_entry.get()
        acount = acountingunit_entry.get()
        prof = profit_entry.get()
        sp = spent_entry.get()
        lf = left_entry.get()
        ls = lastname_entry.get()
        w.writerow([d, nn, f, acount, prof, sp, lf, ls])


def open_second_window():
    global second_window, entries, storage_var, metal_var

    init_window.pack_forget()

    second_window = tk.Frame(root)
    second_window.pack(fill='both', expand=True)

    # Entries for second window
    fields = [
        "Структурное подразделение", "Вид деятельности", "Склад", "Марка", "Сорт",
        "Профиль", "Размер", "Номенклатурный номер", "Единица измерения (Код, Наименование)",
        "Цена (в рублях, копейках)", "Срок годности", "Поставщик", "Наименование материала"
    ]

    entries = {}
    for i, field in enumerate(fields):
        tk.Label(second_window, text=field + ":").grid(row=i, column=0, padx=5, pady=5)
        entries[field] = tk.Entry(second_window)
        entries[field].grid(row=i, column=1, padx=5, pady=5)

    tk.Label(second_window, text="Место хранения:").grid(row=3, column=0, padx=5, pady=5)
    storage_var = tk.StringVar(value="Стеллаж")
    Radiobutton(second_window, text="Стеллаж", variable=storage_var, value="Стеллаж").grid(row=3, column=1, sticky='w')
    Radiobutton(second_window, text="Ячейка", variable=storage_var, value="Ячейка").grid(row=3, column=2, sticky='w')

    tk.Label(second_window, text="В материале содержится металл?:").grid(row=len(fields), column=0, padx=5, pady=5)
    metal_var = tk.StringVar(value="Нет")
    Radiobutton(second_window, text="Да", variable=metal_var, value="Да").grid(row=len(fields), column=1, sticky='w')
    Radiobutton(second_window, text="Нет", variable=metal_var, value="Нет").grid(row=len(fields), column=2, sticky='w')

    tk.Button(second_window, text="Далее", command=handle_material_choice).grid(row=len(fields) + 1, column=0,
                                                                                columnspan=3, pady=10)


def handle_material_choice():
    global filename
    date = date_entry.get()
    filename = f"{date}.csv"

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        data = [entries[field].get() for field in entries]
        data.insert(3, storage_var.get())
        writer.writerow(data)

    if metal_var.get() == "Да":
        open_metal_window()
    else:
        open_non_metal_window()


def open_metal_window():
    global metal_window, metal_entries

    second_window.pack_forget()

    metal_window = tk.Frame(root)
    metal_window.pack(fill='both', expand=True)

    fields = [
        "Наименование", "Вид", "Номенклатурный номер",
        "Единица измерения (Код, Наименование)", "Количество", "Номер паспорта"
    ]

    metal_entries = {}
    for i, field in enumerate(fields):
        tk.Label(metal_window, text=field + ":").grid(row=i, column=0, padx=5, pady=5)
        metal_entries[field] = tk.Entry(metal_window)
        metal_entries[field].grid(row=i, column=1, padx=5, pady=5)

    tk.Button(metal_window, text="Далее", command=open_common_window).grid(row=len(fields), column=0, columnspan=2,
                                                                           pady=10)


def open_non_metal_window():
    second_window.pack_forget()
    open_common_window()


def open_common_window():
    global common_window, common_entries

    if 'metal_window' in globals():
        metal_window.pack_forget()

    common_window = tk.Frame(root)
    common_window.pack(fill='both', expand=True)

    fields = [
        "Дата записи", "Номер документа", "От кого получено или кому отпущено",
        "Учетная единица выпуска продукции", "Приход", "расход", "остаток", "Фамилия, дата"
    ]

    common_entries = {}
    for i, field in enumerate(fields):
        tk.Label(common_window, text=field + ":").grid(row=i, column=0, padx=5, pady=5)
        common_entries[field] = tk.Entry(common_window)
        common_entries[field].grid(row=i, column=1, padx=5, pady=5)

    tk.Button(common_window, text="Сохранить", command=save_common_data).grid(row=len(fields), column=0, columnspan=2,
                                                                              pady=10)


def save_common_data():
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        data = [common_entries[field].get() for field in common_entries]
        writer.writerow(data)

    messagebox.showinfo("Сохранено", "Данные успешно сохранены.")
    root.quit()


root = tk.Tk()
root.title("Карточка учета материалов форма М-17")

init_window = tk.Frame(root)
init_window.pack(fill='both', expand=True)

tk.Label(init_window, text="Организация:").grid(row=0, column=0, padx=5, pady=5)
organization_entry = tk.Entry(init_window)
organization_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(init_window, text="Форма по ОКУД:").grid(row=1, column=0, padx=5, pady=5)
okud_entry = tk.Entry(init_window)
okud_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(init_window, text="По ОКПО:").grid(row=2, column=0, padx=5, pady=5)
okpo_entry = tk.Entry(init_window)
okpo_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(init_window, text="Дата составления:").grid(row=3, column=0, padx=5, pady=5)
date_entry = tk.Entry(init_window)
date_entry.grid(row=3, column=1, padx=5, pady=5)

# tk.Label(init_window, text="Структурное подразделение:").grid(row=4, column=0, padx=5, pady=5)
# subdivision_entry_1 = tk.Entry(init_window)
# subdivision_entry_1.grid(row=4, column=1, padx=5, pady=5)

# -----------------------------------------------------------------------------------------------------------------------

tk.Label(init_window, text="Структурное подразделение:").grid(row=0, column=0, padx=5, pady=5)
subdivision_entry_2 = tk.Entry(init_window)
subdivision_entry_2.grid(row=0, column=1, padx=5, pady=5)

tk.Label(init_window, text="Вид деятельности:").grid(row=1, column=0, padx=5, pady=5)
activity_entry = tk.Entry(init_window)
activity_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(init_window, text="Склад:").grid(row=2, column=0, padx=5, pady=5)
warehous_entry = tk.Entry(init_window)
warehous_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(init_window, text="Марка:").grid(row=3, column=0, padx=5, pady=5)
mark_entry = tk.Entry(init_window)
mark_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(init_window, text="Сорт:").grid(row=4, column=0, padx=5, pady=5)
sort_entry = tk.Entry(init_window)
sort_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(init_window, text="Профиль:").grid(row=5, column=0, padx=5, pady=5)
profile_entry = tk.Entry(init_window)
profile_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(init_window, text="Размер:").grid(row=6, column=0, padx=5, pady=5)
size_entry = tk.Entry(init_window)
size_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Label(init_window, text="Номенклатурный номер:").grid(row=7, column=0, padx=5, pady=5)
num_number_entry = tk.Entry(init_window)
num_number_entry.grid(row=7, column=1, padx=5, pady=5)

tk.Label(init_window, text="Единица измерения (Код, Наименование):").grid(row=8, column=0, padx=5, pady=5)
measure_entry = tk.Entry(init_window)
measure_entry.grid(row=8, column=1, padx=5, pady=5)

tk.Label(init_window, text="Цена (в рублях, копейках):").grid(row=9, column=0, padx=5, pady=5)
price_entry = tk.Entry(init_window)
price_entry.grid(row=9, column=1, padx=5, pady=5)

tk.Label(init_window, text="Срок годности:").grid(row=10, column=0, padx=5, pady=5)
expiration_date_entry = tk.Entry(init_window)
expiration_date_entry.grid(row=10, column=1, padx=5, pady=5)

tk.Label(init_window, text="Поставщик:").grid(row=11, column=0, padx=5, pady=5)
supplier_entry = tk.Entry(init_window)
supplier_entry.grid(row=11, column=1, padx=5, pady=5)

# tk.Label(init_window, text="Наименование материала:").grid(row=12, column=0, padx=5, pady=5)
# material_entry = tk.Entry(init_window)
# material_entry.grid(row=12, column=1, padx=5, pady=5)
# -----------------------------------------------------------------------------------------------------------------------

# tk.Label(init_window, text="Наименование:").grid(row=12, column=0, padx=5, pady=5)
# name_entry = tk.Entry(init_window)
# name_entry.grid(row=12, column=1, padx=5, pady=5)

# tk.Label(init_window, text="Вид:").grid(row=12, column=0, padx=5, pady=5)
# view_entry = tk.Entry(init_window)
# view_entry.grid(row=12, column=1, padx=5, pady=5)

# tk.Label(init_window, text="Номенклатурный номер:").grid(row=12, column=0, padx=5, pady=5)
# numen_number_entry = tk.Entry(init_window)
# numen_number_entry.grid(row=12, column=1, padx=5, pady=5)

# tk.Label(init_window, text="Единица измерения (Код, Наименование):").grid(row=12, column=0, padx=5, pady=5)
# measure1_entry = tk.Entry(init_window)
# measure1_entry.grid(row=12, column=1, padx=5, pady=5)

# tk.Label(init_window, text="Количество:").grid(row=12, column=0, padx=5, pady=5)
# number_entry = tk.Entry(init_window)
# number_entry.grid(row=12, column=1, padx=5, pady=5)

# tk.Label(init_window, text="Номер паспорта:").grid(row=12, column=0, padx=5, pady=5)
# nameofpasport_entry = tk.Entry(init_window)
# nameofpasport_entry.grid(row=12, column=1, padx=5, pady=5)

# -----------------------------------------------------------------------------------------------------------------------
# tk.Label(init_window, text="Дата записи:").grid(row=0, column=0, padx=5, pady=5)
# date2_entry = tk.Entry(init_window)
# date2_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(init_window, text="Номер документа:").grid(row=1, column=0, padx=5, pady=5)
numerr_entry = tk.Entry(init_window)
numerr_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(init_window, text="От кого получено или кому отпущено:").grid(row=2, column=0, padx=5, pady=5)
fromto_entry = tk.Entry(init_window)
fromto_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(init_window, text="Учетная единица выпуска продукции:").grid(row=3, column=0, padx=5, pady=5)
acountingunit_entry = tk.Entry(init_window)
acountingunit_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(init_window, text="Приход:").grid(row=4, column=0, padx=5, pady=5)
profit_entry = tk.Entry(init_window)
profit_entry.grid(row=4, column=1, padx=5, pady=5)

# tk.Label(init_window, text="Расход:").grid(row=5, column=0, padx=5, pady=5)
# spent_entry = tk.Entry(init_window)
# spent_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(init_window, text="Остаток:").grid(row=6, column=0, padx=5, pady=5)
left_entry = tk.Entry(init_window)
left_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Label(init_window, text="Фамилия, дата:").grid(row=7, column=0, padx=5, pady=5)
lastname_entry = tk.Entry(init_window)
lastname_entry.grid(row=7, column=1, padx=5, pady=5)
# -----------------------------------------------------------------------------------------------------------------------


# Next Button
tk.Button(init_window, text="Сохранить данные", command=fill_csv).grid(row=40, column=0, columnspan=2, pady=10)
tk.Button(init_window, text="Далее", command=open_second_window).grid(row=40, column=1, columnspan=2, pady=10)

root.mainloop()
