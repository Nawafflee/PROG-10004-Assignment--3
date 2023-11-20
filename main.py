
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


#Test Cases to make sure that the account class along with its variables and methods are working properly
s1 = SavingsAccount("SAV001","Hishmat Fardouz",0,7000,5000)
print(s1.withdraw(4000))
print(s1.getCurrentBalance())

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

    
#Test Cases to make sure that the account class along with its variables and methods are working properly
c1 = ChequingAccount("CHQ500","Ali Faris",0,7000,5000)
print(c1.withdraw(2000000))
print(c1.getCurrentBalance())



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