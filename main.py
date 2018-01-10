import unittest
from block_io import BlockIo
import sys
import requests

class Main:

    def send_bitcoin(self):
        version = 2
        block_io = BlockIo('e61b-2513-431a-3906', 'shakurraph2', version)
        block_io.withdraw_from_labels(
            amounts='0.001',
            from_labels='default',
            to_addresses='2N23YsTMNSdgxcfebqekGcJjDEkqKk8eunm',
            pin='shakurraph2'
        )


class MainTest(unittest.TestCase):
    def testMain(self):
        result = Main().send_bitcoin()
        self.assertEqual(result["status"], "succes")


if __name__ == '__main__':
    unittest.main()