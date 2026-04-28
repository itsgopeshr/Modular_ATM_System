# main.py
from atm import display_balance, deposit_money, withdraw_money, statement

def run_atm():
    print("=== Welcome to the Secure ATM ===")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Exit")
        
        choice = input("Please select an option (1-5): ")
        
        if choice == '1':
            current_bal = display_balance.get_bal()
            print("\n[INFO] Your current balance is: Rs.", current_bal)
            
        elif choice == '2':
            user_input = input("\nEnter amount to deposit: Rs.")
            if user_input.isdigit():
                amt = int(user_input)
                if deposit_money.deposit(amt):
                    print("[SUCCESS] Rs.", amt, "deposited successfully.")
                else:
                    print("[ERROR] Please enter a positive number.")
            else:
                print("[ERROR] Invalid input. Numbers only.")
                
        elif choice == '3':
            user_input = input("\nEnter amount to withdraw: Rs.")
            if user_input.isdigit():
                amt = int(user_input)
                if withdraw_money.withdraw(amt):
                    print("[SUCCESS] Please collect your cash: Rs.", amt)
                else:
                    print("[ERROR] Insufficient funds or invalid amount.")
            else:
                print("[ERROR] Invalid input. Numbers only.")
                
        elif choice == '4':
            print("\n--- Mini Statement ---")
            history = statement.get_stmt()
            if len(history) == 0:
                print("No transactions made yet.")
            else:
                for record in history:
                    print(record)
            print("Current Balance: Rs.", display_balance.get_bal())
            print("----------------------")
            
        elif choice == '5':
            print("\nThank you for using the Secure ATM. Have a great day!")
            break
            
        else:
            print("[ERROR] Invalid selection. Please try again.")

if __name__ == "__main__":
    run_atm()