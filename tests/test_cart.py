import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=10.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("Extra DVD", cost=10.0)))

    def test_remove_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Aladdin", cost=18.99)
        cart.add_dvd(dvd)
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertFalse(cart.remove_dvd(dvd))

    def test_total_cost_with_discount(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(-10)


if __name__ == "__main__":
    unittest.main()
