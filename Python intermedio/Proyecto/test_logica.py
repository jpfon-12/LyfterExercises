import pytest
from logica import Category, Transaction, FinanceManager

def test_create_new_category_with_empty_name():
    #Arrange
    finance_manager = FinanceManager()
    name = ""
    #Act/Assert
    with pytest.raises(ValueError):
        finance_manager.add_category(name, None)


def test_create_new_category_with_duplicate_name():
    #Arrange
    finance_manager = FinanceManager()
    name = "Comida"
    finance_manager.add_category(name, None)
    #Act/Assert
    with pytest.raises(ValueError):
        finance_manager.add_category(name, None)


def test_compare_category_name():
    #Arrange
    category_1 = Category("Transporte", None)
    category_2 = Category("Transporte", None)
    #Act
    result = category_1 == category_2
    #Assert
    assert result == True


def test_create_valid_transaction():
    #Arrange
    title = "  Almuerzo  " 
    type_transaction = "EXPENSE"
    amount = "5000.5"
    category = "Comida"
    date = "21/10/2025"
    #Act
    transaction = Transaction(title, type_transaction, amount, category, date)
    #Assert
    assert transaction.title == "Almuerzo"
    assert transaction.type_transaction == "expense"
    assert transaction.amount == -5000.5
    assert transaction.category == "Comida"
    assert transaction.date == "21/10/2025"


def test_create_transaction_with_empty_title():
    #Arrange
    title = "" 
    type_transaction = "expense"
    amount = "5000.5"
    category = "Comida"
    date = "21/10/2025"
    #Act/Assert
    with pytest.raises(ValueError):
        Transaction(title, type_transaction, amount, category, date)


def test_create_transaction_with_future_date():
    #Arrange
    title = "Almuerzo" 
    type_transaction = "expense"
    amount = "5000.5"
    category = "Comida"
    date = "21/10/2100"
    #Act/Assert
    with pytest.raises(ValueError):
        Transaction(title, type_transaction, amount, category, date)


def test_create_transaction_with_non_numeric_amount():
    #Arrange
    title = "Almuerzo" 
    type_transaction = "expense"
    amount = "abc"
    category = "Comida"
    date = "21/10/2025"
    #Act/Assert
    with pytest.raises(ValueError, match="Monto"):
        Transaction(title, type_transaction, amount, category, date)


def test_calculate_totals_with_known_transactions():
    #Arrange
    finance_manager = FinanceManager()
    finance_manager.add_category("Trabajo", None)
    finance_manager.add_category("Comida", None)
    finance_manager.add_new_transaction("Salario", "income", "1000", "Trabajo", "01/07/2025")
    finance_manager.add_new_transaction("Almuerzo", "expense", "300", "Comida", "01/07/2025")
    finance_manager.add_new_transaction("Cena", "expense", "200", "Comida", "01/07/2025")
    #Act
    total_income = finance_manager.calculate_total_incomes()
    total_expenses = finance_manager.calculate_total_expenses()
    balance = finance_manager.calculate_balance()
    #Assert
    assert total_income == 1000
    assert total_expenses == 500
    assert balance == 500