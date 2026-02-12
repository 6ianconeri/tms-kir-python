class LogReader:
    def __init__(self):
        self.array = [
            "Привет",
            "",
            " ",
            "Как",
            "Дела?"
        ]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.array):
            line = self.array[self.index]
            self.index += 1
            if line.strip():
                return line.strip()
        raise StopIteration

logReader = LogReader()
for string in logReader:
    print(string)