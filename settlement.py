# Financial Settlement Module

def calculate_settlement(trades, price_per_kwh=8):
    total_amount = 0

    for trade in trades:
        trade["price"] = price_per_kwh
        trade["amount"] = trade["energy"] * price_per_kwh
        total_amount += trade["amount"]

    return total_amount


def display_settlement(trades, total_amount):
    print("\nFINANCIAL SETTLEMENT")

    for trade in trades:
        print("\nSeller:", trade["seller"])
        print("Buyer:", trade["buyer"])
        print("Energy:", trade["energy"], "kWh")
        print("Price: Rs.", trade["price"], "per kWh")
        print("Payment: Rs.", trade["amount"])

    print("\nTotal settlement: Rs.", total_amount)
    print("Settlement complete")