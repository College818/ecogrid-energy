# Smart Meter Integration Module

def get_meter_readings():
    households = [
        {"name": "House A", "generation": 10, "consumption": 6},
        {"name": "House B", "generation": 3, "consumption": 7},
        {"name": "House C", "generation": 8, "consumption": 5}
    ]

    return households


def calculate_energy_balance(house):
    return house["generation"] - house["consumption"]