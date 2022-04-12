import unittest
from loader import Loader, ConcreteLoaderInstanceA

class LoaderTestCase(unittest.TestCase):
    def test_concrete_loader_A_is_instance_of_Loader(self):
        dut = ConcreteLoaderInstanceA
        self.assertIsInstance(dut, Loader)  # add assertion here


if __name__ == '__main__':
    unittest.main()
