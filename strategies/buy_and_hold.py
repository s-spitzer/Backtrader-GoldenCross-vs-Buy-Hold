import backtrader as bt

class BuyHold(bt.Strategy):

    def next(self):
        # if we don't currently hold a position, buy as much as you can with the amount of cash you have
        if self.position.size == 0:
            size = int(self.broker.getcash() / self.data)
            self.buy(size=size)
