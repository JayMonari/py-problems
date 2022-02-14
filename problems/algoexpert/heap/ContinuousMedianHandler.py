from Heap import Heap  # type: ignore


class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(lambda a, b: a > b, [])
        self.greaters = Heap(lambda a, b: a < b, [])
        self.median: int = 0

    def insert(self, value: int) -> None:
        if not len(self.lowers) or value < self.lowers.peek():
            self.lowers.insert(value)
        else:
            self.greaters.insert(value)
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self) -> None:
        if len(self.lowers) - len(self.greaters) == 2:
            self.greaters.insert(self.lowers.remove())
        elif len(self.greaters) - len(self.lowers) == 2:
            self.lowers.insert(self.greaters.remove())

    def updateMedian(self) -> None:
        if len(self.lowers) == len(self.greaters):
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif len(self.lowers) > len(self.greaters):
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

    def getMedian(self) -> int:
        return self.median


test = ContinuousMedianHandler()
test.insert(5)
test.insert(10)
test.insert(100)
test.insert(200)
test.insert(6)
test.insert(13)
test.insert(14)
test.insert(51)
test.insert(52)
test.insert(53)
test.insert(1000)
test.insert(10000)
test.insert(10001)
test.insert(10002)
test.insert(10003)
test.insert(10004)
test.insert(75)
print(test.getMedian())
test.insert(80)
print(test.getMedian())
