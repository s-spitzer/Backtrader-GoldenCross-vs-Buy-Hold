import math 
import backtrader as bt

class GoldenCross(bt.Strategy):
    params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95), ('ticker', 'SPY'))

    def __init__(self):
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close,
            period=self.params.fast,
            plotname='50 day moving average'
        )
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close,
            period=self.params.slow,
            plotname='20 0 day moving average'
        )
        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

    def next(self):
        # if we own zero shares (position size 0)
        if self.position.size == 0:
            # if our crossover is 1 (greater than 0)
            if self.crossover > 0:
                # then the golden cross indicator has happened and we can issue a buy
                amount_to_invest = (self.params.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)

                print("Buy {} shares of {} at {}".format(self.data, self.params.ticker, self.data.close[0]))

                self.buy(size=self.size)

        # if we currently own stock  
        if self.position.size > 0:
            # and corssover reverses to be less than 0
            if self.crossover < 0:
                # then we process our sell
                print("Sell {} shares of {} at {}".format(self.data, self.params.ticker, self.data.close[0]))
                # close the position
                self.close()



        