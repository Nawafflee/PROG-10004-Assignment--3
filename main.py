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