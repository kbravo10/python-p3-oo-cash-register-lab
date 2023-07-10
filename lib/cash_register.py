#!/usr/bin/env python3

class CashRegister:

  total = 0
  items = []
  receipt = []

  def __init__(self,discount = 0):
    self.discount = discount
    self.items = []
    self.receipt = []

  def add_item(self, title, price, amount = 1):
    for i in range(amount):
      self.items.append(title)
    self.receipt.append(price * amount)
    self.total += price * amount

  
  def apply_discount(self):
    if(self.discount != 0):
      self.total -= (self.total * self.discount/100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    self.total -= self.receipt[-1]