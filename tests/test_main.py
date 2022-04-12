import unittest
from main import get_factory
from factories import ConcreteDataRefresherFactoryA, ConcreteDataRefresherFactoryB

class MyTestCase(unittest.TestCase):
    def test_get_factory_method_generator_yields_factory_objects(self):
        dut = get_factory()
        first_value = next(dut)
        self.assertEqual(first_value, ConcreteDataRefresherFactoryA)

        next_value = next(dut)
        self.assertEqual(next_value, ConcreteDataRefresherFactoryB)



if __name__ == '__main__':
    unittest.main()
