import unittest
from dbcon import IDBConnector, SourceDBConnector, TargetDBConnector


class DBConTestCase(unittest.TestCase):
    def test_source_connector_is_instance_of_DBConn(self):
        dut = SourceDBConnector()
        self.assertIsInstance(dut, IDBConnector)


    def test_target_connector_is_instance_of_DBConn(self):
        dut = TargetDBConnector()
        self.assertIsInstance(dut, IDBConnector)

if __name__ == '__main__':
    unittest.main()
