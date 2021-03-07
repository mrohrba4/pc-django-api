from django.db import models
from django.contrib.auth import get_user_model

class Item(models.Model):
  # Type Choices
  dairy = 'dairy'
  drinks = 'drinks'
  meats = 'meats'
  fnv = 'fruits and veggies'
  cond = 'condiments'
  snacks = 'snacks'
  petfood = 'pet food'
  canned = 'canned food'
  dry = 'dry goods'
  clean = 'cleaning supplies'
  type_choices = [
    (dairy, 'Dairy'),
    (drinks, 'Drinks'),
    (meats, 'Meats'),
    (fnv, 'Fruit and Veggies'),
    (cond, 'Condiments'),
    (snacks, 'Snacks'),
    (petfood, 'Pet Food'),
    (canned, 'Canned Food'),
    (dry, 'Dry Goods'),
    (clean, 'Cleaning Supplies'),
  ]

  # Item Name
  name = models.CharField(max_length=100)
  # Item Type
  type = models.CharField(
      max_length=50,
      choices=type_choices,
      default=dairy
  )
  # Item Quantity
  quantity = models.CharField(max_length=3)
  # Item Description
  description = models.TextField()
  # Owner Link
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def as_dict(self):
    """'Returns dictionary version of Item model'"""
    return {
      'id': self.id,
      'name': self.name,
      'type': self.type,
      'quantity': self.quantity,
      'description': self.description
    }
