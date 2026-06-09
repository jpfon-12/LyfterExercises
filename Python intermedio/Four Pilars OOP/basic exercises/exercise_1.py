# Cree una clase de BankAccount que:
# Tenga un atributo de balance.
# Tenga un método para ingresar dinero.
# Tengo un método para retirar dinero.
# Cree otra clase que herede de esta llamada SavingsAccount que:
# Tenga un atributo de min_balance que se pueda asignar al crearla.
# Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.


class BankAccount:

    def __init__(self):
        self.balance = 0


    def deposit_money(self, money_to_deposit):
        self.balance += money_to_deposit


    def withdraw_money(self, money_to_withdraw):
        self.balance -= money_to_withdraw



class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.min_balance = 25 #sets the min_balance to 25


    def withdraw_money(self, money_to_withdraw):
        self.money_to_withdraw = money_to_withdraw
        self.checking_min_balance = self.balance - self.money_to_withdraw #checks if the min_balance is under the min amount

        if self.checking_min_balance < self.min_balance:
            print("Transaction declined: minimum balance must be maintained. (US$25)")
        else:
            super().withdraw_money(self.money_to_withdraw)



my_savings_account = SavingsAccount()
while True:
    try:
        print("\n\t *** Savings Account *** \n")
        print("\n1. Deposit money")
        print("2. Withdraw money")
        print("3. See balance")
        print("0. Exit")
        print("="*15)
        option = int(input("Select an option: "))
        print("-"*20)
        print("\n")
        
        match option:
            case 1:
                try:
                    money_to_deposit = int(input("How much money do you want to deposit? "))
                    my_savings_account.deposit_money(money_to_deposit)
                except:
                    raise ValueError("Invalid input. Please enter a numeric value")
            case 2: 
                try:  
                    money_to_withdraw = int(input("How much money do you want to withdraw? "))
                    my_savings_account.withdraw_money(money_to_withdraw)
                except:
                    raise ValueError("Invalid input. Please enter a numeric value")
            case 3:
                print(f"Balance: {my_savings_account.balance}")
            case 0:
                break
            case _:
                    print("\n --> Invalid option. Please select a valid option from the menu.")
    except ValueError as ex:
        print(f"Error: {ex}")