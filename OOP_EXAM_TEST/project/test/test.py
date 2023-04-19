from project.robot import Robot
import unittest


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot1 = Robot("001", "Military", 10, 100.0)
        self.robot2 = Robot("002", "Education", 20, 200.0)
        self.robot3 = Robot("003", "Entertainment", 30, 300.0)

    def test_category(self):
        self.assertRaises(ValueError, Robot, "004", "Construction", 10, 100.0)
        self.robot1.category = "Humanoids"
        self.assertEqual(self.robot1.category, "Humanoids")

    def test_price(self):
        self.assertRaises(ValueError, Robot, "004", "Military", 10, -100.0)
        self.robot1.price = 150.0
        self.assertEqual(self.robot1.price, 150.0)

    def test_upgrade(self):
        self.assertEqual(self.robot1.upgrade("arm", 50.0), "Robot 001 was upgraded with arm.")
        self.assertEqual(self.robot1.upgrade("arm", 50.0), "Robot 001 was not upgraded.")
        self.assertEqual(self.robot2.upgrade("leg", 75.0), "Robot 002 was upgraded with leg.")
        self.assertEqual(self.robot2.upgrade("leg", 75.0), "Robot 002 was not upgraded.")

    def test_update(self):
        self.assertEqual(self.robot1.update(1.0, 5), "Robot 001 was updated to version 1.0.")
        self.assertEqual(self.robot1.update(2.0, 10), 'Robot 001 was not updated.')
        self.assertEqual(self.robot1.update(3.0, 6), "Robot 001 was not updated.")
        self.assertEqual(self.robot2.update(1.5, 25), "Robot 002 was not updated.")
        self.assertEqual(self.robot2.update(2.0, 15), "Robot 002 was updated to version 2.0.")

    def test_comparison(self):
        self.assertEqual(self.robot1 > self.robot2, "Robot with ID 001 is cheaper than Robot with ID 002.")
        self.assertEqual(self.robot2 > self.robot1, "Robot with ID 002 is more expensive than Robot with ID 001.")
        self.assertEqual(self.robot2 > self.robot3, "Robot with ID 002 is cheaper than Robot with ID 003.")
        self.assertEqual(self.robot3 > self.robot2, "Robot with ID 003 is more expensive than Robot with ID 002.")


if __name__ == '__main__':
    unittest.main()



if __name__ == '__main__':
    unittest.main()

