from models.order import *
import datetime

order1 = Order("Ben", datetime.date(2021, 5, 17), 5)
order2 = Order("Sam", datetime.date(2021, 4, 20), 4)
order3 = Order("Helen", datetime.date(2020, 9, 28), 3)
orders = [order1, order2, order3]
