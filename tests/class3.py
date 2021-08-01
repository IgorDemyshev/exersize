import unittest

def compare_lists(list1,list2):
    if type(list1) != list  and type(list2) != list  :
        raise TypeError("The data type of ohe or both of the inputs is not a list")

data = ['word' , 34, False, 0.99]

for item in data:
    print(f"The value {item} is of datatype '{type(item)}'")





    return sorted(list1) == sorted(list2)











class MyTestCase(unittest.TestCase):

    @unittest.
    def test_sae_list(self):
        ls1 = [1, 3, 6, 2  ]


        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
