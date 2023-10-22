# import unittest

def convert_temperature(temp,value):
    """
    This function converted Celcius between Fahrenheit

    Args:
    temp (string):  temperatur yang ingin di ubah.
    value (int): nilai value.

    Returns:
    float: converted temperature.

    Example:
    >>> convert_temperature("C",50)
    122
     """
    
    # mengubah temperatur menjadi lowercase
    temp = temp.lower()
    
    # konversi suhu
    if(temp == "c"):
        result = (value * 9/5) + 32 
    elif(temp == "f"):
        result = (value - 32) * 5/9  
    else:
        raise Exception("You did not select an option provided!")
        
    
    return result

# input
while True:
    try:
        temp = input("masukan temperatur yang ingin di convert : ")
        value = int(input("masukan nilai suhu : "))

        print(convert_temperature(temp,value))
        break
    except Exception as e:
        print(e)


# print("\n")

# # unit test
# class TestStringMethods(unittest.TestCase):

#     def test_celcius_to_fahrenheit(self):
#         fahrenheit = convert_temperature("c",50)
#         self.assertEqual(fahrenheit, 122)

#     def test_fahrenheit_to_celcius(self):
#         celcius = convert_temperature("f",50)
#         self.assertEqual(celcius, 10)

# if __name__ == '__main__':
#     unittest.main()