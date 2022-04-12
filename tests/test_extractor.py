import unittest

from extractor import Extractor, ConcreteExtractorInstanceA

class ExtractorTestCases(unittest.TestCase):

    #@runtime_checkable
    def test_concrete_extractor_is_instance_of_Extractor(self):
        dut = ConcreteExtractorInstanceA()
        self.assertIsInstance(dut, Extractor)

if __name__ == '__main__':
    unittest.main()