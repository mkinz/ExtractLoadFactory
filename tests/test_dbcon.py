import unittest
from dbcon import DBConnector, SourceDBConnector, TargetDBConnector


class DBConTestCase(unittest.TestCase):
    def test_source_connector_is_instance_of_DBConn(self):
        dut = SourceDBConnector()
        self.assertIsInstance(dut, DBConnector)


    def test_target_connector_is_instance_of_DBConn(self):
        dut = TargetDBConnector()
        self.assertIsInstance(dut, DBConnector)

if __name__ == '__main__':
    unittest.main()
