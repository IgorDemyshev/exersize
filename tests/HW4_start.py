import random
# Homework 4
# Using the make_tree function created in class as an example...
# Create a new function which generates a tree where each branch uses numbers:
#     1
#    222
#   33333
#  4444444
#     |

# print(' '*4, '1'*1)
# print(' '*3, '2'*3)
# print(' '*2, '3'*5)
# print(' '*1, '4'*7)

import random

def make_num_tree(height: int):
    if height < 9:
        new = (list(str(height)).pop(1))
        print(list(str(height)).pop(1))
    # else:



    for i in range(1, (height+1)):
        if range == 1:
            print(str(' ' * (height-i)) + (str(i) * ((i * 2)-1)))
        print(str(' ' * (height-i)) + (str(i) * ((i * 2)-1)))
    print(str(' ' * (height)) + '|')



make_num_tree(12)

#   *
#  ***
# *****
#   |
height_of_tree = 3
# print(' '*3 + '*')
# print(' ' * 2 + '*'*3)
# print(' '  + '*' * 5)
def make_tree(height_of_tree: int, symbol:str ='*'):
    for branch in range(height_of_tree):
        if range == 1 :
            print(' ' * (height_of_tree - branch) + symbol * (1 + (branch * 2)))
        print(' ' * (height_of_tree - branch) + symbol * (1 + (branch * 2)))
    print(' ' * height_of_tree + '|')



# make_tree()
# make_tree(4)
# make_tree(7, '$')
# make_tree(random.randint(2, 12), '$')





# The height of the tree should still be variable, however if height is > 9, the numbers should be reused from zero.
# if height = 10 then the bottom branch should use 0
# if height = 11 then the bottom branch should use 1
# if height = 12 then the bottom branch should use 2... etc.

