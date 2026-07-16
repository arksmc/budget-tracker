
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

def printBudget():
    totalBudget = sum(wallets.values())
    for key, value in wallets.items(): 
        print(f"{key}: ₱{value}")
    
    print(f"\nTotal: ₱{totalBudget}")

def printExpenses():
    totalExpenses = sum(expenses.values())
    for key, value in expenses.items():
        print(f"{key}: ₱{value}")

    print(f"\nTotal: ₱{totalExpenses}")

def addIncome():
    walletNames = list(wallets.keys())
    for index, source in enumerate(walletNames):
        print(f"{index + 1}. {source}")

    choice = int(input("Choose a wallet: "))
    if choice <= 0 or choice > len(walletNames):
        print("Invalid option")
        return
    
    selectedWallet = walletNames[choice - 1]

    amount = float(input("Amount to add: "))

    wallets[selectedWallet] += amount

def addExpense():
    expenseNames = list(expenses.keys())

    for index, source in enumerate(expenseNames):
        print(f"{index + 1}. {source}")
    
    choice = int(input("Choose an expense: "))
    if choice <= 0 or choice > len(expenseNames):
        print("Invalid option")
        return
    
    selectedExpense = expenseNames[choice - 1]
    amount = float(input("Amount to add: "))
    expenses[selectedExpense] += amount ## ^ adding amount to expense category

    walletNames = list(wallets.keys())
    for index, source in enumerate(walletNames):
        print(f"{index + 1}. {source}")

    choice = int(input("Choose a wallet to deduct from: "))
    if choice <= 0 or choice > len(walletNames):
        print("Invalid option")
        return
    
    selectedWallet = walletNames[choice - 1]
    deduction = float(input("Amount to deduct: "))

    wallets[selectedWallet] -= deduction

def main():
    choice = 0
    print("==================") 
    print("Budget Tracker\n")
    print("==================\n")
    print("Accounts:\n")
    
    printBudget() #print total budget

    print(f"\nThis Month:")
    printExpenses()

    while True:
        print("What would you like to do?\n")
        print("[1] Add Income") # add value to key
        print("[2] Add Expense") # add expense, subtract from wallet
        print("[3] Add Wallet")
        print("[4] Transfer Money")
        print("[5] View History")
        print("[6] Exit\n")
        choice = int(input("Enter choice: "))

        match (choice):
            case 1: addIncome()
            case 2: addExpense()
    
main()

