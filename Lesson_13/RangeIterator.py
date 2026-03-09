class RangeIterator:
    def __init__(self, count, step):
        self.count = count
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= self.step
        if self.count > 0:
            return self.count
        raise StopIteration

rangeIter = RangeIterator(50, 10)
for i in rangeIter:
    print(i)