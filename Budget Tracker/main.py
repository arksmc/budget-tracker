def deductWallet(totalCost):
    if not wallets:
        print("You don't have a wallet. Create one first.")
        return
    else:
        remaining = totalCost
        while True:
            selectedWallet = chooseWallet()
            deduct = float(input("Amount to deduct from this wallet: "))
            if deduct > wallets[selectedWallet]:
                print("You don't have enough balance to deduct this amount. Please try again.")
                continue
            else:
                print(f"Deducting ₱{deduct} from {selectedWallet}.")
                wallets[selectedWallet] -= deduct
                remaining -= deduct

                if remaining > 0:
                    print(f"You still have ₱{remaining} left. Deducting from another wallet.")
                    continue
                elif remaining < 0:
                    print(f"You overpaid. You only need ₱{remaining * -1} left. Try again.")
                    wallets[selectedWallet] += deduct
                    remaining += deduct
                    continue
                else:
                    print("Expense paid successfully.")
                    return
