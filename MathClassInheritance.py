# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class MathClass:
    # ¬¬¬¬¬¬¬¬¬
    def __init__(self):
        super().__init__()
    # ¬¬¬¬¬¬¬¬¬
    def add(self, arr_nums):
        sum = 0
        for num in arr_nums:
            sum += num
        return sum
        # ¬¬¬¬¬¬¬¬¬
    def multiply(self, arr_nums):
        product = 1
        for num in arr_nums:
            product *= num
        return product
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class QuebecTaxes(MathClass):
    # ¬¬¬¬¬¬¬¬¬
    def __init__(self, price_amount):
        MathClass.__init__(self)
        self.price_amount = price_amount
        self.precision = '''%.02f'''
    # ¬¬¬¬¬¬¬¬¬
    def getGST(self):
        value = self.multiply([self.price_amount, 0.05])
        precision = self.precision % (value)
        return precision
    # ¬¬¬¬¬¬¬¬¬
    def getQST(self):
        value = self.multiply([self.price_amount, 0.09975])
        precision = self.precision % (value)
        return precision
    # ¬¬¬¬¬¬¬¬¬
    def getTotalTaxes(self):
        gst = float(self.getGST())
        qst = float(self.getQST())
        total = self.add([gst, qst])
        precision = self.precision % (total)
        return precision
    # ¬¬¬¬¬¬¬¬¬
    def getTotalTaxesPlusAmount(self):
        taxes = float(self.getTotalTaxes())
        grand_total = self.add([taxes, self.price_amount])
        precision = self.precision % (grand_total)
        return precision
        
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
x = QuebecTaxes(100)
print(f'{x.getTotalTaxesPlusAmount()}$')





