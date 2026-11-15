from logica import Category, Transaction
import csv, json, os

BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, "finanzas.json")
CSV_FILE_PATH = os.path.join(BASE_DIR, "finanzas.csv")

def load_data():
    categories_list = [] #will hold the Category objects rebuilt from the JSON file
    transactions_list = [] #will hold the Transaction objects rebuilt from the JSON file
    try:
        with open(FILE_PATH, "r", encoding='utf-8') as file:
            data = json.load(file)
        for category_dict in data["categories"]: #rebuild each category dictionary into a Category object
            category = Category.from_dict(category_dict)
            categories_list.append(category)
        for transaction_dict in data["transactions"]: #rebuild each transaction dictionary into a Transaction object
            transaction = Transaction.from_dict(transaction_dict)
            transactions_list.append(transaction)
    #if FileNotFoundError or JSONDecodeError found (first time running the app) the except keeps the lists empty
    except FileNotFoundError:
        pass
    except json.JSONDecodeError as ex:
        pass
    return categories_list, transactions_list


def save_data(categories_list, transactions_list):
    category_dicts = [] #will hold each category converted to a dictionary, ready for the JSON file
    transaction_dicts = [] #will hold each transaction converted to a dictionary, ready for the JSON file
    dictionary_to_save = {} #final structure to save: {"categories": [...], "transactions": [...]}
    for category in categories_list: #convert each Category object into a dictionary
        dict_category = category.to_dict()
        category_dicts.append(dict_category)
    for transaction in transactions_list: #convert each Transaction object into a dictionary
        dict_transaction = transaction.to_dict()
        transaction_dicts.append(dict_transaction)
    dictionary_to_save["categories"] = category_dicts
    dictionary_to_save["transactions"] = transaction_dicts
    with open(FILE_PATH, "w", encoding="utf-8") as file: #write the final structure to the JSON file
        json.dump(dictionary_to_save, file, indent=4, ensure_ascii=False)


def export_csv(file_path, transactions_list, total_income, total_expense, total_balance):
    transactions = []
    for transaction in transactions_list:
        if transaction.type_transaction == "expense":
            translated_type_transaction = "Gasto"
        else: 
            translated_type_transaction = "Ingreso"
        rows = [transaction.date, transaction.title, transaction.amount, transaction.category, translated_type_transaction]
        transactions.append(rows)
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha", "Titulo", "Monto", "Categoria", "Tipo"])
        writer.writerows(transactions)
        writer.writerow(["",])
        writer.writerow(["TOTALES:",])
        writer.writerow(["Total ingresos: ", total_income])
        writer.writerow(["Total egresos: ", total_expense])
        writer.writerow(["Balance: ", total_balance])

