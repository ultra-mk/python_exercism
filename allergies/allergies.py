
class Allergies:
  allergens = {'eggs' : 1, 'peanuts' : 2, 'shellfish' : 4, 'strawberries' : 8, 'tomatoes' : 16, 'chocolate' : 32, 'pollen' : 64, 'cats' : 128}

  def __init__(self, score=0):
    self.allergen_list = []
    self.score = 0

  def is_allergic_to(self, allergen):
    return "is this thing on?"