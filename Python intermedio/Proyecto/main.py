from logica import FinanceManager
from persistencia import load_data
from interfaces import run_main_window


def main():
    categories_list, transactions_list = load_data()
    finance_manager = FinanceManager(categories_list, transactions_list)
    run_main_window(finance_manager)
    

if __name__ == '__main__':
    main()

    