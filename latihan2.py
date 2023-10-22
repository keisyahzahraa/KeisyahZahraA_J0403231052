# import unittest

def calculator_sum(a,b):
    """
    fungsi ini berguna untuk menjumlahkan dua bilangan

    Args:
    num1 : bilangan pertama
    num2 : bilangan kedua

    Returns:
    int: hasil dari penjumlahan dua bilangan.

    Example:
    >>> calculator_sum(1,2)
    3
     """
    
    # penjumlahan
    result = num1 + num2
        
    return result

# input
while True:
    try:
        num1 = int(input("masukan nilai bilangan 1: "))
        num2 = int(input("masukan nilai bilangan 2: "))
        print(calculator_sum(num1,num2))
        break
    except Exception as e:
        print(e)


print("\n")

# unit test
# class TestStringMethods(unittest.TestCase):

#     def test_calculator(self):
#         sum = calculator_sum(1,2)
#         self.assertEqual(sum,3)

# if __name__ == '__main__':
#     unittest.main()