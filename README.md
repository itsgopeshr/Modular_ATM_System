# Modular_ATM_System
# Secure ATM Simulation System 🏦

A modular, console-based ATM simulation built in Python. This project demonstrates core programming concepts like state management, modular package architecture, and menu-driven interfaces without relying on advanced exception handling.

## 🌟 Features
* **Interactive Menu:** An infinite loop menu ensuring seamless user navigation.
* **Display Balance:** Check your current account balance in real-time.
* **Deposit Money:** Add funds to your account with input validation.
* **Withdraw Money:** Securely withdraw funds, preventing overdrafts.
* **Mini Statement:** View a localized transaction history of deposits and withdrawals.

## 📂 Project Structure
```text
atm_project/
│── main.py                 # Main entry point and user interface
│── README.md               # Project documentation
└── atm/
    │── __init__.py         # Package initializer
    │── state.py            # Global dictionary holding balance and statement
    │── display_balance.py  # Logic for retrieving balance
    │── deposit_money.py    # Logic for adding funds
    │── withdraw_money.py   # Logic for deducting funds
    └── statement.py        # Logic for retrieving transaction history
