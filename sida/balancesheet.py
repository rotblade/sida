# -*- coding: utf-8 -*-
"""
BalanceSheet in financial term.
"""


import pandas as pd
from config import Config


class BalanceSheet:
    """
    Represent balance sheet.
    """
    def __init__(self, symbol, market):
        self.symbol = symbol
        self.market = market
        self.full_symbol = '.'.join((symbol, market))
        filepath = Config.STOCK_PATH / self.full_symbol
        name_pattern = '_'.join((self.market,
                                 Config.BALANCESHEET_ABBR,
                                 self.symbol))
        files = filepath.glob(name_pattern+'_*.csv')

        def file2df(f):
            df = pd.read_csv(f, parse_dates=['截止日期'], index_col=3)
            return df.drop(columns=['起始日期'])

        dfs = [file2df(f) for f in files]
        self.balancesheet = pd.concat(dfs)
