"""
Expense Splitter CLI

Enter participants and their expenses.
The program calculates who owes whom.

Usage:
- Run the script.
- Enter participant names and their expenses.
- Get the settlement amounts.

"""

def get_expenses():
    expenses = {}
    print("Enter participant expenses. Type 'done' when finished.")
    while True:
        name = input("Name: ")
        if name.lower() == "done":
            break
        try:
            amount = float(input(f"Amount paid by {name}: "))
            expenses[name] = expenses.get(name, 0) + amount
        except ValueError:
            print("Please enter a valid number.")
    return expenses

def calculate_settlement(expenses):
    total = sum(expenses.values())
    n = len(expenses)
    fair_share = total / n
    balances = {k: v - fair_share for k, v in expenses.items()}
    
    creditors = [(k, v) for k, v in balances.items() if v > 0]
    debtors = [(k, -v) for k, v in balances.items() if v < 0]
    
    i, j = 0, 0
    settlements = []
    
    while i < len(creditors) and j < len(debtors):
        creditor, credit = creditors[i]
        debtor, debt = debtors[j]
        settled_amount = min(credit, debt)
        
        settlements.append(f"{debtor} pays {creditor}: {settled_amount:.2f}")
        creditors[i] = (creditor, credit - settled_amount)
        debtors[j] = (debtor, debt - settled_amount)
        
        if creditors[i][1] == 0:
            i += 1
        if debtors[j][1] == 0:
            j += 1
    
    return settlements

def main():
    expenses = get_expenses()
    if not expenses:
        print("No expenses entered.")
        return
    
    print("\nExpenses entered:")
    for name, amount in expenses.items():
        print(f"{name}: {amount:.2f}")
        
    settlements = calculate_settlement(expenses)
    
    print("\nSettlements to balance expenses:")
    for s in settlements:
        print(s)

if __name__ == "__main__":
    main()
