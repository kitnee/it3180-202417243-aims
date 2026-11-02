import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title(self):
        dvds = [
            DigitalVideoDisc("The Lion King", "Animation", cost=19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", cost=24.95),
            DigitalVideoDisc("Aladdin", "Animation", cost=18.99)
        ]
        results = search_by_title(dvds, "Star")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Star Wars")


if __name__ == "__main__":
    unittest.main()
