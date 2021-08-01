import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_python_lerned(self):
        mylist = [10, 20, 30]

        new_list = [50,60,70]
        mylist.append(40)
        print(mylist)
        for item in new_list:
            mylist.append(item)
        print(mylist)



if __name__ == '__main__':
    unittest.main()
