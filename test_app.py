import unittest
from app import app, sweets
from flask import session

class SweetShopTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        sweets.clear()
        sweets["1001"] = {
            "id": "1001", "name": "Kaju Katli", "category": "Nut Based",
            "price": 50.0, "quantity": 20
        }

    def test_add_sweet(self):
        response = self.client.post("/add", data={
            "id": "2001",
            "name": "Rasgulla",
            "category": "Milk-Based",
            "price": 15.5,
            "quantity": 30
        }, follow_redirects=True)
        self.assertIn(b"Sweet added successfully", response.data)

    def test_delete_sweet(self):
        response = self.client.get("/delete/1001", follow_redirects=True)
        self.assertIn(b"Sweet deleted", response.data)
        self.assertNotIn(b"Kaju Katli", response.data)

    def test_edit_sweet(self):
        response = self.client.post("/update/1001", data={
            "name": "Kaju Deluxe",
            "category": "Premium",
            "price": 60,
            "quantity": 25
        }, follow_redirects=True)
        self.assertIn(b"Sweet updated", response.data)
        self.assertIn(b"Kaju Deluxe", response.data)

    def test_search_by_name(self):
        response = self.client.get("/?name=kaju")
        self.assertIn(b"Kaju Katli", response.data)

    def test_sort_by_price(self):
        sweets["2001"] = {
            "id": "2001", "name": "Ladoo", "category": "Nut",
            "price": 10.0, "quantity": 10
        }
        response = self.client.get("/?sort_by=price")
        self.assertTrue(response.data.find(b"Ladoo") < response.data.find(b"Kaju Katli"))

    def test_purchase(self):
        response = self.client.post("/purchase/1001", data={"quantity": 5}, follow_redirects=True)
        self.assertIn(b"Purchase successful", response.data)
        self.assertEqual(sweets["1001"]["quantity"], 15)

    def test_purchase_insufficient_stock(self):
        response = self.client.post("/purchase/1001", data={"quantity": 100}, follow_redirects=True)
        self.assertIn(b"Not enough stock", response.data)

    def test_total_bill_after_checkout(self):
        # Add two sweets to session cart
        with self.client.session_transaction() as sess:
            sess["cart"] = {
                "1001": {"name": "Kaju Katli", "category": "Nut", "qty": 2, "price": 50},
                "2001": {"name": "Ladoo", "category": "Nut", "qty": 1, "price": 20}
            }
        response = self.client.get("/checkout")
        self.assertIn(b"Total", response.data)
        self.assertIn(b"\xe2\x82\xb9120", response.data)  # ₹120

if __name__ == "__main__":
    unittest.main()
