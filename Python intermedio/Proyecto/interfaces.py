import FreeSimpleGUI as sg
import re
from persistencia import *
from logica import FinanceManager
from datetime import datetime


def build_main_layout():
    headings = ['Fecha', 'Titulo', 'Categoria', 'Monto', 'Tipo']
    layout = [
    [sg.Text("Gestor de Finanzas Personales", key="-APP_TITLE-",
        font=("Helvetica", 22, "bold"), text_color="white",
        justification="center", expand_x=True, pad=(0, (12, 0)))],
    [sg.Text("Registra tus ingresos y gastos", key="-APP_SUBTITLE-",
        font=("Helvetica", 11), text_color="#C9D3DF",
        justification="center", expand_x=True, pad=(0, (0, 12)))],
    [sg.HorizontalSeparator()],
    [sg.Text(" ")],
    [sg.Button("Agregar Categoria", key="-ADD_CATEGORY-",
        font=("Helvetica", 12, "bold"),
        button_color=("white", "#2F80C8"),        
        mouseover_colors=("white", "#256BA8"),    
        border_width=1,
        size=(20, 2),                           
        pad=(10, 10)), 
        sg.Button("Agregar Gasto/Ingreso", key="-ADD_EXPENSE_INCOME-",
        font=("Helvetica", 12, "bold"),
        button_color=("white", "#1F9D6B"),        
        mouseover_colors=("white", "#188159"),
        border_width=1,
        size=(22, 2),
        pad=(10, 10)), 
        sg.Push(), 
        sg.Button("Exportar CSV", key="-EXPORT_CSV-")],
    [sg.CalendarButton("Desde", target="-INPUT_DATE_FROM-", format="%d/%m/%Y", close_when_date_chosen=True, no_titlebar=False, title=""), sg.Input(key="-INPUT_DATE_FROM-", size=(21,1), default_text= "", disabled=True), 
    sg.CalendarButton("Hasta", target="-INPUT_DATE_TO-", format="%d/%m/%Y", close_when_date_chosen=True, no_titlebar=False, title=""), sg.Input(key="-INPUT_DATE_TO-", size=(21,1), default_text= "", disabled=True), 
    sg.Button("Filtrar", key="-FILTER_DATE-",
        font=("Helvetica", 12, "bold"),
        button_color=("black", "#EDF1F5"), 
        mouseover_colors=("black", "#C1CFCF"),    
        border_width=1,
        size=(8, 1)),
    sg.Button("Limpiar", key="-CLEAN_FILTER-",
            font=("Helvetica", 12, "bold"),
            button_color=("black", "#EDF1F5"), 
            mouseover_colors=("black", "#C1CFCF"),    
            border_width=1,
            size=(8, 1))],
    [sg.Text(" ")],
    [sg.Table(
        values = [], 
        headings = headings, 
        col_widths = [12, 25, 15, 12, 10],
        auto_size_columns = False,
        display_row_numbers = False,
        justification = 'left',
        num_rows = 10,
        background_color = "#88A1C0",
        row_height = 26,
        text_color = '#1B2733', 
        header_background_color = '#2B3647',
        header_text_color = 'white',
        selected_row_colors = ('white', '#1F6FB2'),
        key = '-TABLE-',
        enable_events = True ,
        expand_x = True,
        expand_y = True,
    )],
    [sg.Text("Ingreso:", font=("Helvetica", 13, "bold"), text_color="white"),
    sg.Text("0", key="-TOTAL_INCOME-", size=(12, 1), font=("Helvetica", 13, "bold"), text_color="white"),
    sg.Text("Gasto:", font=("Helvetica", 13, "bold"), text_color="white"),
    sg.Text("0", key="-TOTAL_EXPENSES-", size=(12, 1), font=("Helvetica", 13, "bold"), text_color="white"),
    sg.Text("Total:", font=("Helvetica", 13, "bold"), text_color="white"), 
    sg.Text("0", key="-TOTAL_BALANCE-", size=(12, 1), font=("Helvetica", 13, "bold"), text_color="white"), ],
    [sg.Text(" ")]
    ]
    return layout


def open_category_window():
    category_data = None #stays None if the user cancels or closes the window
    layout = [
        [sg.Text("Nombre", key="-NAME_CATEGORY-")],
        [sg.Input(key="-INPUT_CATEGORY-")],
        [sg.ColorChooserButton("Elegir Color", target="-COLOR_HEX-"), sg.Text("", size=(2, 1), key="-PREV-", background_color="white"), sg.Input(key="-COLOR_HEX-", size=(10, 1), enable_events=True, visible=False)],
        [sg.Text(" ")],
        [sg.Button("Cancelar", key= "-CANCEL_CATEGORY-"), sg.Button("Guardar", key="-SAVE_CATEGORY-")],
    ]
    window = sg.Window("Nueva Categoria", layout)
    while True:
        event, values = window.read()
        if event == "-COLOR_HEX-":
            color_chosen = values["-COLOR_HEX-"]
            if color_chosen:
                window['-PREV-'].update(background_color=values["-COLOR_HEX-"])
        elif event == sg.WIN_CLOSED or event == "-CANCEL_CATEGORY-":
            break    
        elif event == "-SAVE_CATEGORY-":   
            category_data = {
                    "name": values["-INPUT_CATEGORY-"] ,
                    "color": values["-COLOR_HEX-"]
                    }
            break
    window.close() 
    return category_data


def open_transaction_window(category_names):   
    CURRENCY_REGEX = r'^\d*\.?\d{0,2}$'
    layout = [
            [sg.Text("Titulo", key="-TITLE_TRANSACTION-")],
            [sg.Input(key="-INPUT_TRANSACTION-", size=(38,1))],
            [sg.Text("Monto", size=(13,1), key="-AMOUNT-"), sg.CalendarButton("Fecha", target="-TRANSACTION_INPUT_DATE-", format="%d/%m/%Y", close_when_date_chosen=True, no_titlebar=False, title="")], #sg.Text("Fecha", size=(13,1), key="-DATE-")],
            [sg.Input(key="-INPUT_AMOUNT-",size=(15,1),  enable_events=True), sg.Input(key="-TRANSACTION_INPUT_DATE-", size=(21,1), default_text=datetime.now().strftime("%d/%m/%Y"), disabled=True)],
            [sg.Text("Categoria", key="-CATEGORY-")],
            [sg.Combo(values=category_names, default_value=category_names[0], key="-COMBO_CATEGORIES-", readonly=True)],
            [sg.Text("Tipo", key="-TYPE_TRANSACTION-")],
            [sg.Radio("Gasto", group_id=1, key="-EXPENSE_OPTION-"), sg.Radio("Ingreso", group_id=1, key="-INCOME_OPTION-")],
            [sg.Text()],
            [sg.Button("Cancelar", key= "-CANCEL_TRANSACTION-"), sg.Button("Guardar", key="-SAVE_TRANSACTION-")],
    ]
    window = sg.Window("Nuevo Gasto/Ingreso", layout)
    transaction_data = None #in case end user cancels the transaction or close the window, the window returns None
    last_valid_amount = ""
    while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "-CANCEL_TRANSACTION-":
                break    
            elif event == "-INPUT_AMOUNT-":#validates numbers and 2 decimals in the amount input 
                if re.fullmatch(CURRENCY_REGEX, values["-INPUT_AMOUNT-"]):
                    last_valid_amount = values["-INPUT_AMOUNT-"]
                else:
                    window["-INPUT_AMOUNT-"].update(last_valid_amount)
            elif event == "-SAVE_TRANSACTION-":   
                if values["-EXPENSE_OPTION-"]:
                    type_transaction = "expense"
                elif values["-INCOME_OPTION-"]:
                    type_transaction = "income"
                else:
                    sg.popup("Debe seleccionar el tipo de transaccion: Gasto o Ingreso")
                    continue
                transaction_data = {
                    "title": values["-INPUT_TRANSACTION-"],
                    "type_transaction": type_transaction,
                    "amount": values["-INPUT_AMOUNT-"],
                    "category": values["-COMBO_CATEGORIES-"],
                    "date": values["-TRANSACTION_INPUT_DATE-"],
                }
                break
    window.close() 
    return transaction_data


def run_main_window(finance_manager):
    layout = build_main_layout()
    window = sg.Window("Gestor Finanzas Personales", layout, finalize=True, resizable=True)
    refresh_table(window, finance_manager)
    while True:
        event, values = window.read()
        if event == "-ADD_CATEGORY-":
            category_data = open_category_window()
            if category_data is not None:
                try:
                    finance_manager.add_category(**category_data)
                except ValueError as ex:
                    sg.popup(str(ex))
                else:
                    save_data(finance_manager.categories_list, finance_manager.transactions_list)          
        elif event == "-ADD_EXPENSE_INCOME-":
            if not finance_manager.categories_list:
                sg.popup("La lista de categorias esta vacia. Registre una categoria primero para poder continuar")
            else:
                category_names = get_category_names(finance_manager.categories_list)#calls auxiliary function 
                transaction_data = open_transaction_window(category_names) 
                if transaction_data is not None:
                    try:
                        finance_manager.add_new_transaction(**transaction_data)
                    except ValueError as ex:
                        sg.popup(str(ex))
                    else:
                        save_data(finance_manager.categories_list, finance_manager.transactions_list)
                        refresh_table(window, finance_manager)
        elif event == "-FILTER_DATE-":
            try:
                filtered_list = finance_manager.filter_transactions_per_date(values["-INPUT_DATE_FROM-"], values["-INPUT_DATE_TO-"])
            except ValueError as ex:
                sg.popup(str(ex))
            else:
                refresh_table(window, finance_manager, filtered_list)
        elif event == "-CLEAN_FILTER-":
            window["-INPUT_DATE_FROM-"].update("")
            window["-INPUT_DATE_TO-"].update("")
            refresh_table(window, finance_manager)
        elif event == "-EXPORT_CSV-":
            if not finance_manager.transactions_list:#prevents overwriting the csv file with empty data
                    sg.popup("La lista de transacciones esta vacia. Agregue primero una transaccion")
            else:
                file_path = sg.popup_get_file("Guardar archivo CSV",           
                                                title="Exportar a CSV",
                                                save_as=True,                      
                                                no_window=True,                   
                                                default_extension=".csv",           
                                                file_types=(("Archivos CSV", "*.csv"),))
                if file_path:
                    total_income = finance_manager.calculate_total_incomes()
                    total_expense = finance_manager.calculate_total_expenses()
                    total_balance = finance_manager.calculate_balance()
                    try:
                        export_csv(file_path, finance_manager.transactions_list, total_income, total_expense, total_balance)
                    except OSError as ex:
                        sg.popup(str(ex))
                    else:
                        sg.popup("Archivo CSV guardado con exito")
        elif event == sg.WIN_CLOSED:
            break
    window.close()


def refresh_table(window, finance_manager, filtered_list=None):
    if filtered_list is None:
        transactions_to_show = finance_manager.transactions_list
        total_income = finance_manager.calculate_total_incomes()
        total_expenses = finance_manager.calculate_total_expenses()
        total_balance = finance_manager.calculate_balance()
    else:
        transactions_to_show = filtered_list
        total_income = finance_manager.calculate_total_incomes(filtered_list)
        total_expenses = finance_manager.calculate_total_expenses(filtered_list)
        total_balance = finance_manager.calculate_balance(filtered_list)
    rows = get_transactions_rows(transactions_to_show)
    category_colors = get_category_color(finance_manager.categories_list)#calls the function to get the color per category
    color_for_row = get_color_rows(finance_manager.transactions_list, category_colors)#calls the function to get the colors of the rows
    window["-TABLE-"].update(values=rows)
    window["-TABLE-"].update(row_colors=color_for_row)
    window["-TOTAL_INCOME-"].update(value=format_currency(total_income))
    window["-TOTAL_EXPENSES-"].update(value=format_currency(total_expenses))
    window["-TOTAL_BALANCE-"].update(value=format_currency(total_balance))


def get_category_names(categories_list):#this auxiliary function returns a list with only the names (text) of each Category object, to fill the combo box
    category_names = []
    for category in categories_list:
        category_names.append(category.name)
    return category_names


def get_category_color(categories_list):#this auxiliary function returns a dictionary with only the name:color of each Category object
    category_name_and_color = {}
    for category in categories_list:
            if category.color is not None:
                category_name_and_color[category.name] = category.color
    return category_name_and_color


def get_color_rows(transactions_list, category_colors):
    color_for_row = []
    counter = 0
    for row in transactions_list:
        for name, color in category_colors.items():
            if row.category == name:
                color_for_row.append((counter, color))
        counter += 1
    return color_for_row

def get_transactions_rows(transactions_list):#the function receives the list of transactions and returns a list of rows (one list per transaction) ready to fill the table
    transactions_rows = []
    for transaction in transactions_list:
        if transaction.type_transaction == "expense":
            translated_type_transaction = "Gasto"
        else: 
            translated_type_transaction = "Ingreso"
        transaction_attributes = [transaction.date, transaction.title, transaction.category, format_currency(transaction.amount), translated_type_transaction]
        transactions_rows.append(transaction_attributes)
    return transactions_rows


def format_currency(amount):#this function returns the amount as text, like ₡5,000.00 or -₡5,000.00
    if amount < 0:
        return f"- ₡{abs(amount):,.2f}"
    else:
        return f" ₡{abs(amount):,.2f}"

