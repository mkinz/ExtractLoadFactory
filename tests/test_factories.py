import unittest
from factories import ConcreteDataRefresherFactoryA, ConcreteDataRefresherFactoryB
from loader import Loader
from extractor import Extractor
from dbcon import DBConnector

class FactoriesTestCase(unittest.TestCase):
    def test_Concrete_factory_A_returns_correct_objects(self):
        dut = ConcreteDataRefresherFactoryA
        loader = dut.get_loader()
        extractor = dut.get_extractor()
        source_conn = dut.get_source_connector()
        target_conn = dut.get_target_connector()

        self.assertIsInstance(loader, Loader)
        self.assertIsInstance(extractor, Extractor)
        self.assertIsInstance(source_conn, DBConnector)
        self.assertIsInstance(target_conn, DBConnector)

    def test_Concrete_factory_B_returns_correct_objects(self):
        dut = ConcreteDataRefresherFactoryB
        loader = dut.get_loader()
        extractor = dut.get_extractor()
        source_conn = dut.get_source_connector()
        target_conn = dut.get_target_connector()

        self.assertIsInstance(loader, Loader)
        self.assertIsInstance(extractor, Extractor)
        self.assertIsInstance(source_conn, DBConnector)
        self.assertIsInstance(target_conn, DBConnector)




if __name__ == '__main__':
    unittest.main()
