import unittest

from smart_meter import get_meter_readings, calculate_energy_balance


class TestSmartMeter(unittest.TestCase):

    def test_meter_readings(self):
        households = get_meter_readings()

        self.assertEqual(len(households), 3)
        self.assertEqual(households[0]["generation"], 10)
        self.assertEqual(households[0]["consumption"], 6)

    def test_energy_balance(self):
        house = {
            "name": "Test House",
            "generation": 10,
            "consumption": 6
        }

        balance = calculate_energy_balance(house)

        self.assertEqual(balance, 4)


if __name__ == "__main__":
    unittest.main()