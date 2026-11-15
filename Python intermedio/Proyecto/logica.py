
from datetime import datetime
DATE_FORMAT="%d/%m/%Y"

class Category:

    def __init__(self, name, color=None):
        self.name = name.strip().capitalize()#removes empty spaces from the name and capitalizes the first letter of the string
        self.color = color
        self.validate_name() #validates right away, so an invalid category can never be created

    def __str__(self):
        return self.name

    def validate_name(self):#validates the category name is not empty
        if self.name == "":
            raise ValueError("El nombre de la categoria no puede estar vacio")

    def __eq__(self, category):#compares if a category already exists 
        if not isinstance(category, Category):#returns false if category is not a Category object
            return False
        if self.name == category.name:
            return True
        else:
            return False
        
    def to_dict(self):#converts from object to dict, so can save it to the JSON file
        dict_category = {"name": self.name,
                        "color": self.color,}
        return dict_category

    @classmethod
    def from_dict(cls, dict_category): #converts from dict to object to load data back from the JSON file
        category = Category(**dict_category)
        return category


class Transaction:

    def __init__(self, title, type_transaction, amount, category, date):
        self.title = title.strip()
        self.type_transaction = type_transaction.lower()
        self.amount = amount
        self.category = category
        self.date = date
        #validates attributes 
        self.validate_title() 
        self.validate_type_transaction()
        self.validate_amount()
        self.validate_positive_negative_amount()
        self.validate_date()

    def __str__(self):
        return f"Date: {self.date} | Title: {self.title} | Category: {self.category} | Amount: {self.amount} | Transaction {self.type_transaction}"

    def __eq__(self, transaction):#compares if 2 transactions have same data
            if not isinstance(transaction, Transaction):#returns false if transaction is not a Transaction object
                        return False
            if self.title == transaction.title and self.type_transaction == transaction.type_transaction and self.amount == transaction.amount and self.category == transaction.category and self.date == transaction.date:
                return True
            else:
                return False
            
    def validate_title(self):#validates the title is not empty
            if self.title == "":
                raise ValueError("El titulo no puede estar vacio")

    def validate_type_transaction(self):#validates the type transaction is either expense or income
        if self.type_transaction != "expense" and self.type_transaction != "income":
            raise ValueError("Tipo de transaccion invalido. Seleccione Ingreso o Gasto")

    def validate_amount(self):#validates the amount is a valid number 
        try:
            float_amount = float(self.amount)
            self.amount = float_amount
        except ValueError:
            raise ValueError("Error. Monto invalido")

    def validate_positive_negative_amount(self):#validates if the category is expense so modifies the amount to negative value and positive value if an income
        if self.type_transaction == "expense":
            negative_amount = -abs(self.amount)
            self.amount = negative_amount
        elif self.type_transaction == "income":
                    positive_amount = abs(self.amount)
                    self.amount = positive_amount

    def validate_date(self):
        todays_date = datetime.today().date()
        try:
            date = datetime.strptime(self.date, DATE_FORMAT).date()
        except ValueError:
            raise ValueError("Formato de fecha inválido (use dd/mm/yyyy)")
        if date > todays_date:
            raise ValueError("La fecha no puede ser en el futuro")


    def to_dict(self):#converts from object to dict, so can save it to the JSON file
            dict_transaction = {"title": self.title,
                            "type_transaction": self.type_transaction,
                            "amount": self.amount,
                            "category": self.category,
                            "date": self.date,}
            return dict_transaction

    @classmethod
    def from_dict(cls, dict_transaction): #converts from dict to object to load data back from the JSON file
        transaction = Transaction(**dict_transaction)
        return transaction


class FinanceManager:

    def __init__(self, categories_list=None, transactions_list=None): #receives the transactions and categories lists with data if provided, otherwise starts with empty lists
        self.categories_list = categories_list if categories_list is not None else []
        self.transactions_list = transactions_list if transactions_list is not None else []

    def add_category(self, name, color):
        try:
            category = Category(name, color)
        except ValueError:
            raise
        if category in self.categories_list:#internally calling the __eq__ method from Category class to check if there are duplicate categories in the list
            raise ValueError("Esta categoria ya existe")
        else:
            self.categories_list.append(category)

    def add_new_transaction(self, title, type_transaction, amount, category, date):
        category_exist = False
        for category_in_list in self.categories_list:
            if category_in_list.name == category:
                category_exist = True
        if not category_exist:
            raise ValueError("La categoría no existe. Registre la categoría primero para poder continuar.") 
        else:
            transaction = Transaction(title, type_transaction, amount, category, date)
            self.transactions_list.append(transaction)


    def calculate_total_incomes(self, filtered_list=None): #returns the sum of all incomes; uses filtered_list if provided, otherwise all transactions
        total_income = 0
        if filtered_list is None: #no filter applied, sum over every transaction
            for transaction in self.transactions_list:
                if transaction.type_transaction == "income":
                    total_income += transaction.amount
        else:  # sum only over the filtered transactions
            for transaction in filtered_list:
                if transaction.type_transaction == "income":
                    total_income += transaction.amount
        return total_income


    def calculate_total_expenses(self, filtered_list=None): #returns the sum of all expenses as a positive number. uses filtered_list if provided
        total_expense = 0
        if filtered_list is None: #no filter applied, sum over every transaction
            for transaction in self.transactions_list:
                if transaction.type_transaction == "expense":
                    total_expense += transaction.amount
        else: # sum only over the filtered transactions
            for transaction in filtered_list:
                if transaction.type_transaction == "expense":
                    total_expense += transaction.amount
        convert_total_expense = abs(total_expense)#converts the negative number into positive to show it to the end user
        return convert_total_expense


    def calculate_balance(self, filtered_list=None): #returns income minus expenses by summing every amount (expenses are already negative). uses filtered_list if provided
        balance = 0
        if filtered_list is None: #no filter applied, sum over every transaction
            for transaction in self.transactions_list:
                balance += transaction.amount
        else: # sum only over the filtered transactions
            for transaction in filtered_list:
                balance += transaction.amount
        return balance


    def filter_transactions_per_date(self, date_from, date_to):
        filtered_list = []
        try:
            object_date_from = datetime.strptime(date_from, DATE_FORMAT).date()
            object_date_to = datetime.strptime(date_to, DATE_FORMAT).date()
        except ValueError:
            raise ValueError("Formato de fecha inválido (use dd/mm/yyyy)")
        for transaction in self.transactions_list:
            transaction_date = datetime.strptime(transaction.date, DATE_FORMAT).date() 
            if transaction_date >= object_date_from and transaction_date <= object_date_to:
                filtered_list.append(transaction)
        return filtered_list

