import unittest

from marketplace import find_matches


class TestMarketplace(unittest.TestCase):

    def test_buyer_seller_matching(self):
        households = [
            {"name": "House A", "generation": 10, "consumption": 6},
            {"name": "House B", "generation": 3, "consumption": 7}
        ]

        sellers, buyers, trades = find_matches(households)

        self.assertEqual(len(sellers), 1)
        self.assertEqual(len(buyers), 1)
        self.assertEqual(len(trades), 1)

        self.assertEqual(trades[0]["seller"], "House A")
        self.assertEqual(trades[0]["buyer"], "House B")
        self.assertEqual(trades[0]["energy"], 4)


if __name__ == "__main__":
    unittest.main()