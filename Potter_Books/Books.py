class PotterBooks():
    def __init__(self, books):
        self.books = books

    def price(self):
        total = 8*self.books["1"] + 8*self.books["2"]

        return total