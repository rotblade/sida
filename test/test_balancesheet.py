import unittest
from sida.balancesheet import BalanceSheet


class TestBalanceSheet(unittest.TestCase):
    def setUp(self):
        self.bs = BalanceSheet('03948', 'hk')

    def test_columns(self):
        print('\n')
        for col in self.bs.balancesheet.columns:
            print(col)
        print(self.bs.balancesheet['短期债项'])
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
