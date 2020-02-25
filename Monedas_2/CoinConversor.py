class CoinConversor:
    def __init__(self, quantity):
        self.quantity = quantity
        self.euros = {}
        self.coins = ""
        self.read()

    def read(self):
        coin_euro_types=(2,1)
        for coins in coin_euro_types:
            coin_type = str(coins)+"€"
            self.euros[coin_type] = self.quantity//coins
            self.make_result(self.euros[coin_type], coins)

    def make_result(self, amount, coin_type):
        if amount <= 0:
            return
        else:
            if self.coins != "":
                self.coins += ", "
            if amount == 1:
                self.coins += str(amount) + " coin of " + str(coin_type) + "€"
            else:
                self.coins += str(amount) + " coins of " + str(coin_type) + "€"
            self.quantity -= amount*coin_type

    def write(self):
        return self.coins