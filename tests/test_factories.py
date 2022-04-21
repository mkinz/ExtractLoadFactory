import unittest
from factories import ConcreteDataRefresherFactoryA, ConcreteDataRefresherFactoryB
from iloader import ILoader
from iextractor import IExtractor
from dbcon import IDBConnector

class FactoriesTestCase(unittest.TestCase):
    def test_Concrete_factory_A_returns_correct_objects(self):
        dut = ConcreteDataRefresherFactoryA
        loader = dut.get_loader(self)
        extractor = dut.get_extractor(self)
        source_conn = dut.get_source_connector(self)
        target_conn = dut.get_target_connector(self)

        self.assertIsInstance(loader, ILoader)
        self.assertIsInstance(extractor, IExtractor)
        self.assertIsInstance(source_conn, IDBConnector)
        self.assertIsInstance(target_conn, IDBConnector)

    def test_Concrete_factory_B_returns_correct_objects(self):
        dut = ConcreteDataRefresherFactoryB
        loader = dut.get_loader(self)
        extractor = dut.get_extractor(self)
        source_conn = dut.get_source_connector(self)
        target_conn = dut.get_target_connector(self)

        self.assertIsInstance(loader, ILoader)
        self.assertIsInstance(extractor, IExtractor)
        self.assertIsInstance(source_conn, IDBConnector)
        self.assertIsInstance(target_conn, IDBConnector)




if __name__ == '__main__':
    unittest.main()
