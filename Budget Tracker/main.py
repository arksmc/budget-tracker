# TODO: make it scalable, start with an empty dict

import sys

wallets = {}
expenses = {}

def displayWallet():
    if not wallets:
        print("No wallets found.")
        print("Please create a wallet first.")
    for key, value in wallets.items(): 
        print(f"{key}: ₱{value}")
    # for dashboard, prints wallet w balance

def displayExpenses():
    if not expenses:
        print("No expenses found.")
        print("Please create an expense category first.")
    for key, value in expenses.items():
        print(f"{key}: ₱{value}")
    # for dashboard, prints category w expense

def printBudget():
    totalBudget = sum(wallets.values())
    displayWallet()
    print(f"\nTotal Budget: ₱{totalBudget}")
    # just prints the total budget

def printExpenses():
    totalExpenses = sum(expenses.values())
    displayExpenses()
    print(f"\nTotal Expenses: ₱{totalExpenses}")
    # just prints the total expenses i guess

def chooseWallet():
    if not wallets:
        print("No wallets found.")
        print("Please create a wallet first.")
        return
    
    walletNames = list(wallets.keys())
    while True:
        try:
            for index, source in enumerate(walletNames):
                print(f"{index + 1}. {source}")
            choice = int(input("Choose a wallet: "))
        except ValueError:
            print(f"Please input a valid option.")
            continue
        if choice <= 0 or choice > len(walletNames):
            print("Invalid option")
            continue
    
        selectedWallet = walletNames[choice - 1]
        return selectedWallet
    # prints key with number then returns user's selected wallet

def chooseExpense():
    if not expenses:
        print("No expenses found.")
        print("Please create an expense category first.")
        return
    
    expenseNames = list(expenses.keys())
    while True:
        try:
            for index, source in enumerate(expenseNames):
                print(f"{index + 1}. {source}")
            choice = int(input("Choose an expense: "))
        except ValueError:
            print(f"Please input a valid option.")
            continue
        if choice <= 0 or choice > len(expenseNames):
            print("Invalid option")
            continue
    
        selectedExpense = expenseNames[choice - 1]
        return selectedExpense
    # prints key with number then returns user's selected category

def addIncome():
    if not wallets:
        wallet = input("Enter wallet name: ").capitalize()
        amount = float(input("Amount to add: "))
        wallets[wallet] = amount
    else:
        while True:
            choice = int(input("Do you want to add a new wallet?\n[1] Yes\n[2] No\nEnter choice: "))
            if choice == 1:
                wallet = str(input("Enter wallet name: ")).capitalize()
                if wallet in wallets:
                    print("You already have this wallet.")
                    continue
                amount = float(input("Amount to add: "))
                wallets[wallet] = amount
                return
            elif choice == 2:
                selectedWallet = chooseWallet()
                amount = float(input("Amount to add: "))
                wallets[selectedWallet] += amount
                return
            else:
                print("Please choose a valid option.")
                continue

def addExpense():
    if not expenses:
        newExpense()
        return
    
    while True:
        choice = int(input("Do you want to add a new expense category?\n[1] Yes\n[2] No\nEnter choice: "))
        if choice == 1:
            newExpense()
            return
        elif choice == 2:
            category = chooseExpense()
            paidAmt = float(input("Enter amount paid: "))
            expenses[category] = paidAmt

            deductBalance(paidAmt)
            return
        else:
            print("Please choose from one of the options.")
            continue

def deductBalance(paidAmt):
    debt = paidAmt
    while True:
        print("Paid from: ")
        selectedWallet = chooseWallet()
        deduct = float(("Enter amount paid from this wallet: "))

        if deduct > wallets[selectedWallet]:
            print("You don't have enough balance to deduct this amount. Please input a different amount.")
            continue
        else:
            print(f"Deducting ₱{deduct} from {selectedWallet}")
            wallets[selectedWallet] -= deduct
            remaining = debt - deduct

            if remaining > 0:
                print(f"You still have ₱{remaining} left. Please choose another wallet to deduct from.")
                continue
            elif remaining < 0:
                print(f"You have overspent. Though I don't know how you bypassed this lol.")
                continue
            else:
                print(f"You have successfully spent ₱{debt}.")
                return

def newExpense():
    expense = input("Enter expense category: ").capitalize()

    if expense in expenses:
        print("You already have this expense category.")
        return
    
    amount = float(input("Enter expense amount: "))
    expenses[expense] = amount
# you should deduct everytime a new expense is added that is > 0

def transferMoney():
    while True:
        print(f"Transfer from: ")
        selectedWallet = chooseWallet()
        print(f"Transfer to: ")
        receivingWallet = chooseWallet()

        if selectedWallet == receivingWallet:
            print("You cannot transfer money to the same wallet. Please try again.")
            continue

        amount = float(input("Amount to transfer: "))

        if amount <= 0:
            print("Please input an amount greater than 0.")
            continue

        if amount > wallets[selectedWallet]:
            print("You don't have the sufficient funds for this transfer.")
            continue

        wallets[selectedWallet] -= amount
        wallets[receivingWallet] += amount

        print("Transfer Successful. Would you like to make another transfer?")
        choice = int(input("[1] Yes\n[2] No\nEnter choice: "))

        if choice == 1:
            continue
        elif choice == 2:
            return
        else:
            print("Please choose from one of the options.")
            continue

    #edge cases: transferring to same wallet, amount more than balance

def dashboard():
    print("==================") 
    print("  Budget Tracker  ")
    print("==================\n")
    print("Accounts:\n")
    
    printBudget() #print total budget

    print(f"\nExpenses this month:")
    printExpenses()

    print("==================\n")


def main():
    choice = 0

    dashboard()
    while True:
        print("What would you like to do?\n")
        print("[1] Add Income") # add value to key
        print("[2] Add Expense") # add expense, subtract from wallet
        print("[3] Transfer Money")
        print("[4] Exit\n")
        choice = int(input("Enter choice: "))

        match (choice):
            case 1: 
                addIncome()
                dashboard()
            case 2: 
                addExpense()
                dashboard()
            case 3: 
                transferMoney()
                dashboard()
            case 4: 
                print("Exiting...")
                sys.exit()
            case _:
                print("Invalid option.")
    
main()

