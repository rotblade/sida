# -*- coding: utf-8 -*-


from pathlib import Path


class Config:
    STOCK_PATH = Path.home() / 'downloads' / 'stocks'
    MARKET_HK_SUFFIX = 'HK'
    MARKET_SH_SUFFIX = 'SH'
    MARKET_SZ_SUFFIX = 'SZ'
    BALANCESHEET_ABBR = 'fzb'
    PROFIT_ABBR = 'lrb'
    CASHFLOW_ABBR = 'llb'
