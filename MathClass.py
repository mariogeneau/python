# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
class MathClass(object):
    # ¬¬¬¬¬¬¬¬¬¬
    def __init__(self):
        super().__init__()
    # ¬¬¬¬¬¬¬¬¬¬
    def add(self, arr_nums):
        sum = 0
        for num in arr_nums:
            sum += num
        return sum
    # ¬¬¬¬¬¬¬¬¬¬
        
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
# mathObject = MathClass()
# sum = mathObject.add([2, 3])
# print(sum)