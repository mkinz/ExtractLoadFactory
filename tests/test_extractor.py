import unittest

from extractor import IExtractor, GenericConcreteExtractor

class ExtractorTestCases(unittest.TestCase):

    #@runtime_checkable
    def test_concrete_extractor_is_instance_of_Extractor(self):
        dut = GenericConcreteExtractor()
        self.assertIsInstance(dut, IExtractor)

if __name__ == '__main__':
    unittest.main()