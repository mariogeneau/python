# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class Taxes(object):
    # ¬¬¬¬¬¬¬¬¬¬
    def __init__(self, initial_amount = 1):
        self.initial_amount = initial_amount
    # ¬¬¬¬¬¬¬¬¬¬
    def michiganTaxes(self):
        precision = '''%.02f'''
        return float(precision % (self.initial_amount * 0.06))
    # ¬¬¬¬¬¬¬¬¬¬
    def michiganTaxesWithAmount(self):
        precision = '''%.02f'''
        return float(precision % (self.michiganTaxes() + self.initial_amount))
    # ¬¬¬¬¬¬¬¬¬¬
    def quebecTaxes(self):
        precision = '''%.02f'''
        gst = float(precision % (self.initial_amount * 0.05))
        qst = float(precision % (self.initial_amount * 0.09975))
        total = gst + qst
        return float(precision % (total))
    # ¬¬¬¬¬¬¬¬¬¬
    def quebecTaxesWithAmount(self):
        precision = '''%.02f'''
        return float(precision % (self.quebecTaxes() + self.initial_amount))
    # ¬¬¬¬¬¬¬¬¬¬

# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
michigan = Taxes(100)
precision = '''$%.02f'''
print(precision % (michigan.michiganTaxesWithAmount()))

# quebec = Taxes(100)
# precision = '''$%.02f'''
# print(precision % (quebec.quebecTaxesWithAmount()))
