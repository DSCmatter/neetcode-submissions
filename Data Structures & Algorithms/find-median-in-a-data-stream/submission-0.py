class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)

        if n % 2 == 1:
            middle = n // 2 
            return self.data[middle]
        else:
            middle1 = n // 2 - 1 
            middle2 = n // 2

            return (self.data[middle1] + self.data[middle2]) / 2 
            