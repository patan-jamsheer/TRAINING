class BankAccount:
    def __init__(self,Acc_holder_name:str,Acc_number:int,Balance:int):
        self.Acc_number:str=Acc_number
        self.Acc_holder_name:int=Acc_holder_name
        self._Balance:str=Balance
    def deposit(self,amount:int):
        self.__Balance+=amount
        print(f"successfully deposited {amount}\nTotal Balance={self.__Balance}")
        print("-"*50)
    def withdraw(self,amount:int):
        if self.__Balance < amount:
            print("Low balance\n")
            print("-"*50)
        else:
            self.__Balance-=amount
            print(f"successfully withdrawn amount of {amount}\nTotal Balance={self.__Balance}")
            print("-"*50)
    def check_balance(self):
        print(f"current Balance is ={self.__Balance}\n")
        print("-"*50)
    def display_account_details(self):
        print(f"ACcount Holder Name={self.Acc_holder_name}\n Account_number={self.Acc_number}\nTotal Balance={self.__Balance}")
        print("-"*50)

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__("jamsheer",246913342,2000)

    def show_balance(self):
        print(self._balance)

SA=SavingsAccount()
SA.show_balance()