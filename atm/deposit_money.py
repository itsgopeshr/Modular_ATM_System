# atm/deposit_money.py
from .state import acc

def deposit(amt):
    if amt > 0:
        acc["bal"] += amt
        acc["stmt"].append("Deposited: + Rs." + str(amt))
        return True
    return False