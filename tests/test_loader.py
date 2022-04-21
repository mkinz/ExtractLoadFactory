import unittest
from iloader import ILoader, ConcreteLoaderInstanceA

class LoaderTestCase(unittest.TestCase):
    def test_concrete_loader_A_is_instance_of_Loader(self):
        dut = ConcreteLoaderInstanceA()
        self.assertIsInstance(dut, ILoader)  # add assertion here


if __name__ == '__main__':
    unittest.main()
