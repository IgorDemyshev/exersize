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