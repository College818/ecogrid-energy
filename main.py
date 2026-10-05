# EcoGrid Energy Trading Simulator
# Main Application

from smart_meter import get_meter_readings, calculate_energy_balance
from marketplace import find_matches
from settlement import calculate_settlement, display_settlement


print("================================")
print("   ECOGRID ENERGY TRADING")
print("================================")


# Smart Meter Integration
households = get_meter_readings()

print("\nSMART METER READINGS")

for house in households:
    print("\nHouse:", house["name"])
    print("Generation:", house["generation"], "kWh")
    print("Consumption:", house["consumption"], "kWh")

    balance = calculate_energy_balance(house)

    if balance > 0:
        print("Energy to sell:", balance, "kWh")
    elif balance < 0:
        print("Energy needed:", abs(balance), "kWh")
    else:
        print("Energy balanced")


# Marketplace
print("\nBUYER-SELLER MATCHING")

sellers, buyers, trades = find_matches(households)

for trade in trades:
    print(
        trade["seller"],
        "sells",
        trade["energy"],
        "kWh to",
        trade["buyer"]
    )

print("\nMATCHING COMPLETE")


# Financial Settlement
total_amount = calculate_settlement(trades)

display_settlement(trades, total_amount)


# Save Transaction Records
existing_records = set()

try:
    with open("transactions.txt", "r") as file:
        for line in file:
            existing_records.add(line.strip())
except FileNotFoundError:
    pass


with open("transactions.txt", "a") as file:
    for trade in trades:
        record = (
            f"Seller: {trade['seller']}, "
            f"Buyer: {trade['buyer']}, "
            f"Energy: {trade['energy']} kWh, "
            f"Price: Rs. {trade['price']} per kWh, "
            f"Payment: Rs. {trade['amount']}"
        )

        if record not in existing_records:
            file.write(record + "\n")


print("Transaction record saved.")


# System Summary
total_generation = sum(
    house["generation"] for house in households
)

total_consumption = sum(
    house["consumption"] for house in households
)

total_energy_traded = sum(
    trade["energy"] for trade in trades
)


print("\n================================")
print("       SYSTEM SUMMARY")
print("================================")

print("Total generation:", total_generation, "kWh")
print("Total consumption:", total_consumption, "kWh")
print("Number of sellers:", len(sellers))
print("Number of buyers:", len(buyers))
print("Energy traded:", total_energy_traded, "kWh")
print("Total settlement: Rs.", total_amount)

print("\nEcoGrid simulation completed successfully.")