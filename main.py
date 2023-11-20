
"""
 Github Repository: https://github.com/Nawafflee/PROG-10004-Assignment--3

"""

class Account:
    
    #Constructor to initialize Account and declare its properties

    #Must make attributes private
    def __init__(self,accountNumber,accountHolderName,rateOfInterest,currentBalance):
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance

    #getAccountNumber method for Account class
    def getAccountNumber(self):
        return self._accountNumber

    #getAccountHolderName method for Account class
    def getAccountHolderName(self):
        return self._accountHolderName
    
    #getRateOfInterest method for Account class
    def getRateOfInterest(self):
        return self._rateOfInterest
    
    #getCurrentBalance method for Account class
    def getCurrentBalance(self):
        return self._currentBalance 
    
    #setAccountHolderName method for Account class
    def setAccountHolderName(self,name):
        self._accountHolderName = name

    #setRateOfInterest method for Account class
    def setRateOfInterest(self,rate):
        self._rateOfInterest = rate

    #deposit method for Account class
    def deposit(self,amount):
        self._currentBalance += amount
        return "${} CAD has been successfully deposited".format(amount)
     
    #withdraw method for Account class 
    def withdraw(self,amount):
        self._currentBalance -= amount
        return "${} CAD has been successfully withdrawn".format(amount)

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



#TODO: Application class needs to be worked on at end after all the other classes are created
"""
class Application:

    def showMainMenu(self):
        print("Welcome to the Bank")
        while True:
            print("\tMain Menu, Please Select the Following Options:")
            print("1. Search Account")
            print("2. Open Account (Bonus Question)")
            print("3. Exit")
            try:
                choice_selection = int(input("Enter your choice: "))

                if choice_selection == 1:
                    print("Selected Choice 1") 
                elif choice_selection == 2:
                    print("Selected Choice 2") 
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
                    print("Selected Choice 1") 
                elif choice_selection == 2:
                    print("Selected Choice 2") 
                elif choice_selection == 3:
                    print("Selected Choice 3") 
                elif choice_selection == 4:
                    print("Exiting the Accounts Menu...")
                    break
            except ValueError as err:
                print(err)


App1 = Application()
App1.showAccountMenu()
App1.showMainMenu()
"""