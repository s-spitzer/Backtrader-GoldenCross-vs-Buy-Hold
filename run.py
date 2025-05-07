import os, sys, argparse
import pandas as pd
import backtrader as bt
from backtrader import cerebro 
from strategies.golden_cross import GoldenCross
from strategies.buy_and_hold import BuyHold

strategies = {
    "golden_cross": GoldenCross,
    "buy_and_hold": BuyHold
}
# parse any arguments that come in (list of strategies to run)
parser = argparse.ArgumentParser()
parser.add_argument("strategy", help="which strategy to run", type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print("invalid strategy, must be one of {}".format(strategies.keys()))
    sys.exit()

# instantiate Cerebro and set starting cash amount
cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)
# setting spy.csv data to spy_prices
spy_prices = pd.read_csv('data/spy.csv', index_col='Date', parse_dates=True)
# providing cerebro a data feed
feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)
# providing cerebro a strategy (passing in using args)
# run "python3 run.py golden_cross" in command line for Golden Cross
# run "python3 run.py buy_and_hold" in command line for Buy Hold 
cerebro.addstrategy(strategies[args.strategy])
 
cerebro.run()
cerebro.plot()
