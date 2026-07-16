# TODO: make it scalable, start with an empty dict
# TODO: remove add wallet, unnecessary

import sys

wallets = {
    "Cash": 500,
    "GCash": 1500,
    "Landbank": 3000
}

expenses = {
    "Food": 0,
    "Transport": 0,
    "School": 0
}

def displayWallet():
    for key, value in wallets.items(): 
        print(f"{key}: ₱{value}")

def displayExpenses():
    for key, value in expenses.items():
        print(f"{key}: ₱{value}")

def printBudget():
    totalBudget = sum(wallets.values())
    
    displayWallet()
    
    print(f"\nTotal: ₱{totalBudget}")

def printExpenses():
    totalExpenses = sum(expenses.values())
    
    displayExpenses()

    print(f"\nTotal: ₱{totalExpenses}")

def chooseWallet():
    walletNames = list(wallets.keys())
    for index, source in enumerate(walletNames):
        print(f"{index + 1}. {source}")

    choice = int(input("Choose a wallet: "))
    if choice <= 0 or choice > len(walletNames):
        print("Invalid option")
        return
    
    selectedWallet = walletNames[choice - 1]
    return selectedWallet

def chooseExpense():
    expenseNames = list(expenses.keys())

    for index, source in enumerate(expenseNames):
        print(f"{index + 1}. {source}")
    
    choice = int(input("Choose an expense: "))
    if choice <= 0 or choice > len(expenseNames):
        print("Invalid option")
        return
    
    selectedExpense = expenseNames[choice - 1]
    return selectedExpense

def addIncome():
    selectedWallet = chooseWallet()

    amount = float(input("Amount to add: "))
    wallets[selectedWallet] += amount

def addExpense():
    
    selectedExpense = chooseExpense()
   
    amount = float(input("Amount to add: "))
    expenses[selectedExpense] += amount ## ^ adding amount to expense category

    selectedWallet = chooseWallet()
    deduction = float(input("Amount to deduct: "))

    wallets[selectedWallet] -= deduction

def transferMoney():
    print(f"Transfer from: ")
    selectedWallet = chooseWallet()
    print(f"Transfer to: ")
    receivingWallet = chooseWallet()
    amount = float(input("Amount to transfer: "))

    wallets[selectedWallet] -= amount
    wallets[receivingWallet] += amount

    #edge cases: transferring to same wallet, amount more than balance

def dashboard():
    print("==================") 
    print("Budget Tracker\n")
    print("==================\n")
    print("Accounts:\n")
    
    printBudget() #print total budget

    print(f"\nThis Month:")
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

