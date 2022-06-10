import unittest
from dbcon import IDBConnector, ConcreteSourceDBConnector, ConcreteTargetDBConnector


class DBConTestCase(unittest.TestCase):
    def test_source_connector_is_instance_of_DBConn(self):
        dut = ConcreteSourceDBConnector()
        self.assertIsInstance(dut, IDBConnector)


    def test_target_connector_is_instance_of_DBConn(self):
        dut = ConcreteTargetDBConnector()
        self.assertIsInstance(dut, IDBConnector)

if __name__ == '__main__':
    unittest.main()
