import unittest
from loader import ILoader, GenericConcreteLoader

class LoaderTestCase(unittest.TestCase):
    def test_concrete_loader_A_is_instance_of_Loader(self):
        dut = GenericConcreteLoader()
        self.assertIsInstance(dut, ILoader)  # add assertion here


if __name__ == '__main__':
    unittest.main()
