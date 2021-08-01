import random
#   *
#  ***
# *****
#   |
height_of_tree = 10
# print(' '*3 + '*')
# print(' ' * 2 + '*'*3)
# print(' '  + '*' * 5)
def make_tree(height_of_tree: int, symbol:str ='*'):
    for branch in range(height_of_tree):
        print(' ' * (height_of_tree - branch) + symbol * (1 + (branch * 2)))
    print(' ' * height_of_tree + '|')

# make_tree()
make_tree(4)
make_tree(7, '$')
make_tree(random.randint(2, 12), '$')

def register(name, gender =None,race='', *other, **stuff):
  print(f'Hello {name}!')
  if gender:
    print(f"You are a {gender}")
  if race:
    print(f'...your race is "{race}"')
  for i in other:
    print(f".... and you are {i}")
  # for (k, v) in stuff.items( ):
  #   print(f"... you {k} is {v}")
  for (key, value) in stuff.items():
    print(f"...your {key} is {value}")

register('Jane')
register('Bob', 'male')
register("Jessi", None,'hispanic', 21, 'white', height=170, cell='434-2321-2131')
register(
    race ='white',
    gender= 'male',
    address='123 Apple Ln',
    name='Steve'
)

# import unittest
#
#
# def convert_int_to_list(number):
#     if type(number) != int and type(number) != float:
#         raise TypeError("Please provide int and float input")
#     return [int(i) for i in str(number).replace(
#         '.', '').replace(',', '').replace('-', '')]
#
#
#
#
# class IntConvertTests(unittest.TestCase):
#     def test_positive_int(self):
#         expected = [7, 4, 2, 1]
#         actual = convert_int_to_list(7421)
#         self.assertEqual(expected, actual)
#
#
# if __name__ == '__main__':
#     unittest.main()
