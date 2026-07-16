
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

totalBudget = sum(wallets.values())

def printBudget():
    for key, value in wallets.items(): 
        print(f"{key}: ₱{value}")
    
    print(f"\nTotal: ₱{totalBudget}")

def printExpenses():
    totalExpenses = sum(expenses.values())
    for key, value in expenses.items():
        print(f"{key}: ₱{value}")


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
        print("[1] Add Income")
        print("[2] Add Expense")
        print("[3] Add Wallet")
        print("[4] Transfer Money")
        print("[5] View History")
        print("[6] Exit")
        choice = int(input("Enter choice: "))

        match (choice):
            case 1:
    
main()

