# atm/withdraw_money.py
from .state import acc

def withdraw(amt):
    if amt > 0 and amt <= acc["bal"]:
        acc["bal"] -= amt
        acc["stmt"].append("Withdrew:  - Rs." + str(amt))
        return True
    return False