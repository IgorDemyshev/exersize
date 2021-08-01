import unittest


def convert_int_to_list(number):
    if type(number) != int and type(number) != float:
        raise TypeError('Please provide int and float input.')
    return [int(i) for i in str(number).replace('.', '').replace(',', '').replace('-', '') ]


def convert_text_to_list(text):
    if type(text) == int or type(text) ==float:
        raise TypeError('Please provide text input.')
    return [str(i) for i in str(text).replace('.', '').replace(',', '').replace('-', '').replace('"', '').replace("'", '') ]



class TextConvertTest(unittest.TestCase):
    def test_positive_text(self):
        expected =['a', 'b', 'c', 'd']
        actual = convert_text_to_list('a.,b"c-d')
        print(actual)
        self.assertEqual(expected,actual)

    def test_positive_int(self):
        expected =[1, 2, 3, 4]
        actual = convert_int_to_list(1234)
        print(actual)
        self.assertEqual(expected,actual)