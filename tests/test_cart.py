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

    def test_sort_by_title(self):
        cart = Cart()
        d1 = DigitalVideoDisc("Star Wars", cost=20.0)
        d2 = DigitalVideoDisc("Aladdin", cost=15.0)
        cart.add_dvd(d1)
        cart.add_dvd(d2)
        cart.sort_by_title()
        self.assertEqual(cart.items[0].title, "Aladdin")
        self.assertEqual(cart.items[1].title, "Star Wars")

    def test_sort_by_cost(self):
        cart = Cart()
        d1 = DigitalVideoDisc("Aladdin", cost=15.0)
        d2 = DigitalVideoDisc("Star Wars", cost=25.0)
        cart.add_dvd(d1)
        cart.add_dvd(d2)
        cart.sort_by_cost()
        self.assertEqual(cart.items[0].title, "Star Wars")
        self.assertEqual(cart.items[1].title, "Aladdin")


if __name__ == "__main__":
    unittest.main()
