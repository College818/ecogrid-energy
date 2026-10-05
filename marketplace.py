# Marketplace Module

def find_matches(households):
    sellers = []
    buyers = []
    trades = []

    for house in households:
        balance = house["generation"] - house["consumption"]

        if balance > 0:
            sellers.append({
                "name": house["name"],
                "energy": balance
            })

        elif balance < 0:
            buyers.append({
                "name": house["name"],
                "energy": abs(balance)
            })

    for seller in sellers:
        for buyer in buyers:
            if seller["energy"] > 0 and buyer["energy"] > 0:
                trade = min(seller["energy"], buyer["energy"])

                trades.append({
                    "seller": seller["name"],
                    "buyer": buyer["name"],
                    "energy": trade
                })

                seller["energy"] -= trade
                buyer["energy"] -= trade

    return sellers, buyers, trades