import unittest

def compare_lists(list1,list2):
    if type(list1) != list and type(list2) !=list:
        raise TypeError('The data type of one or both of the inputs is not a list. ')

    # ls1 = []
    # for item in list1:
    #     ls1.append(str(item))
    # ls2 = []
    # for item in list2:
    #     ls2.append(str(item))

    ls2 = list(list2[::])
    for item in list1:

        try:
            idx = ls2.index(item)
        except ValueError:
            # idx = -1
            return False
        # if idx < 0:
        #     return False
        ls2.pop(idx)

    return len(ls2) == 0
    return True


    # return sorted(ls1) == sorted(ls2)


class ListCompareTests(unittest.TestCase):
    # simple positive test
    def test_same_list(self):
        ls1 =[1, 3, 5, 7]
        ls2 =[1, 3, 5, 7]
        self.assertTrue(compare_lists(ls1, ls2))

    def test_different_list(self):
        ls1 = [1, 2, 5, 8]
        ls2 = [0, 3, 5, 7]
        self.assertFalse(compare_lists(ls1, ls2))

    # @unittest.skip
    def test_different_lengths(self):
        ls1 = [1, 2, 5, 8]
        ls2 = [0, 3, 5, 7, 9]
        self.assertFalse(compare_lists(ls1, ls2))

    # @unittest.expectedFailure
    #todo ID  fix this after we learn loops
    def test_different_order(self):
        ls1 = [1, 2, 5, 8]
        ls2 = [8, 5, 2, 1]
        self.assertTrue(compare_lists(ls1, ls2))


    def test_unexpected_data_types(self):
        word1 = 'abcde'
        word2 = 'decba'
        self.assertRaises(TypeError, lambda : compare_lists(word1, word2))




    def test_check_if_two_lists_not_equal(self):
        list1 = ['a', 'b', 'c']
        list2 = ['a', 'b', 'd']
        self.assertNotEqual(list1, list2, "Lists are equal")

    def test_check_if_two_lists_equal(self):
        # 1) takes 2 lists as input
        list1 = [1,3,5,7]
        list2 = [7,1,5,3]
        # 2) checks if the lists have same members, regardless of order
        result1 = sorted(list1)
        result2 = sorted(list2)
        self.assertListEqual(result1, result2, "Lists are not equal")

    def test_if_lists_have_same_number_of_members(self):
        list1 = [1,3,5,7]
        list2 = [7,1,5,3]
        member_count1 = len(list1)
        member_count2 = len(list2)
        self.assertTrue(member_count1 == member_count2, "Number of members is different")

    # 3) does not effect the original order within either list
    def test_check_changed_original_lists_order(self):
        list1 = [1,3,7,5]
        list2 = [7,1,5,3]
        result1 = list1.sort()
        result2 = list2.sort()
        print("list1 and list2 changed: " + str(list1)+ str(list2))
        self.assertListEqual(list1, list2, "Lists are not equal")


    # 4) return True if the lists have the same members
    # or False if they have different members
    def test_check_if_2_lists_not_equal(self):
        list1 = [9,8,7,6]
        list2 = [9,8,7,6]
        self.assertTrue(list1 == list2, "Lists are not equal")


    def test_check_if_2_lists_not_equal(self):
        list1 = [9, 8, 7, 6, 5]
        list2 = [9, 8, 7, 6]
        self.assertFalse(list1 == list2, "Lists are equal")


    def test_with_duos(self):
        ls1 = [1, 2, 3, 2]
        ls2 = [1, 2, 3]

if __name__ == '__main__':
    unittest.main()