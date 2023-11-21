
"""
 Github Repository: https://github.com/Nawafflee/PROG-10004-Assignment--3

"""

class Account:
    
    #Constructor to initialize Account and declare its properties

    def __init__(self,accountNumber,accountHolderName,rateOfInterest,currentBalance):
        self.__accountNumber = accountNumber
        self.__accountHolderName = accountHolderName
        self.__rateOfInterest = rateOfInterest
        self.__currentBalance = currentBalance

    #getAccountNumber method for Account class
    def getAccountNumber(self):
        return self.__accountNumber

    #getAccountHolderName method for Account class
    def getAccountHolderName(self):
        return self.__accountHolderName
    
    #getRateOfInterest method for Account class
    def getRateOfInterest(self):
        return self.__rateOfInterest
    
    #getCurrentBalance method for Account class
    def getCurrentBalance(self):
        return self.__currentBalance 
    
    #setAccountHolderName method for Account class
    def setAccountHolderName(self,name):
        self.__accountHolderName = name

    #setRateOfInterest method for Account class
    def setRateOfInterest(self,rate):
        self.__rateOfInterest = rate

    #deposit method for Account class
    def deposit(self,amount):
        self.__currentBalance += amount
        return "${} CAD has been successfully deposited!".format(amount)
     
    #withdraw method for Account class 
    def withdraw(self,amount):
        self.__currentBalance -= amount
        return "${} CAD has been successfully withdrawn!".format(amount)

"""
#Test Cases to make sure that the account class along with its variables and methods are working properly
account1 = Account("CHQ200","Mike Hern",0.0,5000.0)
print(account1.deposit(3000.0))
print(account1.getCurrentBalance())
print(account1.getAccountNumber())
print(account1.getRateOfInterest())
print(account1.setAccountHolderName("fsd"))
print(account1.withdraw(50000.0))
print(account1.getCurrentBalance())   
print(account1.getAccountHolderName())
"""


class SavingsAccount(Account):
    
    #Initializer to initialize Saving account with parameters which some inherit from Account Class
    def __init__(self,accountNumber,accountHolderName,rateOfInterest,currentBalance,minimumBalance):
        self.__minimumBalance = minimumBalance
        super().__init__(accountNumber,accountHolderName,rateOfInterest,currentBalance)

    #Withdrawal method that adds the minimum balance requirement to a new withdraw method on the SavingsAccount Class
    def withdraw(self,amount):
        #self._Account__currentBalance is used this way to call from the Account Class since the currentBalance property is a private attribute with 2 underscores
        if self._Account__currentBalance - amount < self.__minimumBalance:
            print("Withdrawal of ${} CAD from Savings Account has been rejected : BELOW MINIMUM BALANCE!".format(amount))

        #calls Account Class withdrawal method using super function
        else:
            super().withdraw(amount)
            print("Withdrawal of ${} CAD from Savings Account has been successful!".format(amount))

"""
#Test Cases to make sure that the account class along with its variables and methods are working properly
s1 = SavingsAccount("SAV001","Hishmat Fardouz",0,7000,5000)
print(s1.withdraw(4000))
print(s1.getCurrentBalance())
"""
class ChequingAccount(Account):
    def __init__(self,accountNumber,accountHolderName, rateOfInterest, currentBalance ,overdraftLimit):
        super().__init__(accountNumber,accountHolderName,rateOfInterest,currentBalance)
        self.__overdraftLimit = overdraftLimit

    #Withdrawal method that adds the overdraft limit requirement to a new withdraw method on the ChequingAccount Class
    def withdraw(self, amount):
        if self._Account__currentBalance + self.__overdraftLimit < amount:
            print("Withdrawal of ${} CAD from Chequing Account has been rejected : ABOVE OVERDRAFT LIMIT!".format(amount))

            #calls Account Class withdrawal method using super function
        else:
            super().withdraw(amount)
            print("Withdrawal of ${} CAD from Chequing Account has been successful!".format(amount))

"""
#Test Cases to make sure that the account class along with its variables and methods are working properly
c1 = ChequingAccount("CHQ500","Ali Faris",0.0,7000.0,5000.0)
print(c1.withdraw(2000000))
print(c1.getCurrentBalance())
"""


class Bank:
    
    def __init__(self,bankName):
        self.__bankName = bankName
        
        self.accountList = [
            ChequingAccount("CHQ001","Mike",0.0,1000.0,5000.0),
            ChequingAccount("CHQ002","Sam",0.0,2000.0,3000.0),
            ChequingAccount("CHQ003","Marcel",0.0,3000.0,2000.0),
            SavingsAccount("SAV001","Ali",5.0,5000.0,1000.0),
            SavingsAccount("SAV002","Hishmat",5.0,6000.0,1500.0),
            SavingsAccount("SAV003","Sara",5.0,7000.0,2000.0),
        ]
        
    def searchAccount(self,account_number):
        for account in self.accountList:
            if account._Account__accountNumber == account_number:
                #return "Account {} found".format(account)
                return account
        #return "Cannot find account {}".format(account_number)
        return None
    
    
    def openAccount(self,account_type,account_number,account_holder_name,rate_of_interest,current_balance,account_feature):
        if account_type == "Savings" or account_type == "savings" or account_type == "SAVINGS":
            establish_account = SavingsAccount(account_number,account_holder_name,rate_of_interest,current_balance,account_feature)
            self.accountList.append(establish_account)
            return "Account Type {} | Account Number {} | Holder Name '{}' | Rate of Interest {}% | Balance ${} CAD was successfully created".format(account_type,account_number,account_holder_name,rate_of_interest,current_balance)
            #return "{} Account Type | Account Number {} | Minimum Balance {}".format(account_type,account_number,account_feature) 
        elif account_type == "Chequing" or account_type == "chequing" or account_type == "CHEQUING":
            establish_account = ChequingAccount(account_number,account_holder_name,rate_of_interest,current_balance,account_feature)
            self.accountList.append(establish_account)
            #return "{} Account Type | Account Number {} | Overdraft Limit {}".format(account_type,account_number,account_feature) 
            return "Account Type {} | Account Number {} | Holder Name '{}' | Rate of Interest {}% | Balance ${} CAD was successfully created".format(account_type,account_number,account_holder_name,rate_of_interest,current_balance)
        else:
            return "Account Type is Invalid : Must be 'Chequing' 'chequing' 'CHEQUING' or 'Savings' or 'savings' or 'SAVINGS' Account"
      
"""
#Code so far can only work when interest is added onto Chequing Account which is true in the real world as there are Chequing accounts
#offering an annual interest rate
bank1 = Bank("Test Bank")
print(bank1.searchAccount("CHQ001"))
print(bank1.openAccount("hi","SAV101","Ali",5.0,5000.0,3000.0))
print(bank1.searchAccount("SAV101"))
print(bank1.openAccount("Savings","SAV1301","Ali",5.0,5000.0,3000.0))
print(bank1.searchAccount("SAV1301"))
"""

class Application:

    def __init__(self,bank):
        self.bank = bank
        self.currentAccount = None

    def showMainMenu(self):
        print("Welcome to the Bank")
        while True:
            print("\nMain Menu, Please Select the Following Options:")
            print("1. Search Account")
            print("2. Open Account (Bonus Question)")
            print("3. Exit")
            try:
                choice_selection = int(input("Enter your choice: "))

                if choice_selection == 1:
                    self.search_account() 
                elif choice_selection == 2:
                    self.open_account()
                elif choice_selection == 3:
                    print("Exiting the Application...")
                    quit()
            except ValueError as err:
                print(err)
            

    def showAccountMenu(self):
        print("Welcome to the Account Menu:")
        while True:
            print("\nOptions: ")
            print("1. Check Balance")
            print("2. Deposit Amount")
            print("3. Withdraw Amount")
            print("4. Exit Accounts Menu")
            try:
                choice_selection = int(input("Enter your choice: "))

                if choice_selection == 1:
                    self.checkBalance()
                elif choice_selection == 2:
                    self.deposit()
                elif choice_selection == 3:
                    self.withdraw()
                elif choice_selection == 4:
                    print("Exiting the Accounts Menu...")
                    break
            except ValueError as err:
                print(err)

    def search_account(self):
        account_number = str(input("Enter account number: "))
        account = self.bank.searchAccount(account_number)

        #search account success
        if account:
            print("{} Account has been selected".format(account_number))
            self.currentAccount = account
            self.showAccountMenu()
        #account can not be found
        else:
            print("{} Account can not be found".format(account_number))


    def open_account(self):
        print("Account Opening Procedure: ")
    
        account_type = str(input("Enter Account Type (Savings or Chequing): "))
        print("You have selected {} as the Account Type".format(account_type))

        account_number = str(input("Enter Account Number: "))
        print("You have selected '{}' as the Account Number".format(account_number))

        account_holder_name = str(input("Enter Account Holder name: "))
        print("You have selected '{}' as the Account Holder's name".format(account_holder_name))

        rate_of_interest = float(input("Enter Rate of Interest: "))
        print("You have selected '{} %' as the Rate of Interest".format(rate_of_interest))

        current_balance = float(input("Enter Current Balance: "))
        print("You have deposited ${} CAD into the Account's Balance".format(current_balance))
        
        
        if account_type == "Savings" or account_type == "savings" or account_type == "SAVINGS":
            minimum_balance = float(input("Enter Minimum Balance for Savings account: "))
            print("You have set up the Saving Account's Minimum Balance as ${} CAD".format(minimum_balance))
            self.bank.openAccount(account_type,account_number,account_holder_name,rate_of_interest,current_balance,account_feature = minimum_balance)
            print("Account Type {} | Account Number {} | Holder Name '{}' | Rate of Interest {}% | Balance ${} CAD was successfully created".format(account_type,account_number,account_holder_name,rate_of_interest,current_balance))
        elif account_type == "Chequing" or account_type == "chequing" or "CHEQUING":
            overdraft_limit = float(input("Enter Overdraft Limit for Chequing Account: "))
            print("You have set up the Chequing Account's Overdraft Limit as ${} CAD".format(overdraft_limit))
            self.bank.openAccount(account_type,account_number,account_holder_name,rate_of_interest,current_balance,account_feature = overdraft_limit)
            print("Account Type {} | Account Number {} | Holder Name '{}' | Rate of Interest {}% | Balance ${} CAD was successfully created".format(account_type,account_number,account_holder_name,rate_of_interest,current_balance))
        else:
            print("Account Type is Invalid : Must be 'Chequing' 'chequing' or 'Savings' or 'savings Account.")
        
        print("\n Going Back to the Main Menu...")


    def checkBalance(self):
        #check for current balance using getCurrentBalance method
        if self.currentAccount:
            print("Balance ${} CAD".format(self.currentAccount.getCurrentBalance()))

            #good coding practice
        else:
            print("No account selected.")
    
    def deposit(self):
        if self.currentAccount:
            try:
                #amount less than zero condition 
                amount = float(input("Enter amount to deposit: "))
                if amount < 0:
                    print("Invalid amount. Please enter a positive value.")
                else:
                    self.currentAccount.deposit(amount)
                    print("Deposit of ${} CAD has been successful.".format(amount))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        #good coding practice
        else:
            print("No account has been selected.")

    def withdraw(self):
        if self.currentAccount:
            try:
                #amount less than zero condition 
                amount = float(input("Enter amount to withdraw: "))
                if amount < 0:
                    print("Invalid amount. Please enter a positive value.")
                else:
                    self.currentAccount.withdraw(amount)
                    #print("Withdrawal of ${} CAD has been successful.".format(amount))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("No account has been selected.")

    def run(self):
        self.showMainMenu()

# Main
bank = Bank("Nawaf")
app = Application(bank)
app.run()