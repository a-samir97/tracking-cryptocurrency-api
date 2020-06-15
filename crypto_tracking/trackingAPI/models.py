from django.db import models

class Cryptocurrency(models.Model):
    crypto_name = models.CharField(max_length=25)
    price = models.CharField(max_length=20)
    market_cap = models.CharField(max_length=30)
    change = models.CharField(max_length=30)

    def __str__(self):
        return '{} || {} || {} || {}'.format(
            self.crypto_name,
            self.price,
            self.market_cap,
            self.change
        ) 