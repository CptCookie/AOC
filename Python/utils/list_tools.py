class CircleList:
    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, index):
        return self.lst[index % len(self.lst)]
