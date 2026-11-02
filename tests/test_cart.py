import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=10.0)))
        # Đĩa thứ 21 vượt quá giới hạn, phải trả về False
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("Extra DVD", cost=10.0)))


if __name__ == "__main__":
    unittest.main()
