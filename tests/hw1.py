import unittest

def vowel_counter(word) -> int:
    count = 0
    if type(word) is list:
        for x in word: count += vowel_counter(x)
    elif type(word) is dict:

        for x, y in word.items():
            count += vowel_counter(x)
            count += vowel_counter(y)


    elif type(word) is not str:
        print (word)
        return count
    if not word.isascii():
        raise ValueError("It is not  English language")

    vowel = set("aeiou")

    for letter in word:
        if letter.lower() in vowel:
            count = count + 1

    return count

class TestVowelCount(unittest.TestCase):
    # Positive simple smoke test

    def test_small_word(self):
        input = "dog"
        expected_count =1
        actual_count = vowel_counter(input)
        self.assertEqual(expected_count, actual_count, "They are not equal")

    def test_sentence(self):
        sentence = "It is a great Tuesday evening!"
        expected_count = 11
        actual_count = vowel_counter(sentence)

        self.assertTrue(expected_count == actual_count,
                        f"The actul count of {actual_count} vowels in the input '{sentence}' "
                        f"did not match expected count {expected_count}.")

        # self.assertTrue(10 == vowel_counter("It is a great Tuesday evening!"))

# negative test
    def test_int_input(self):
        input = 266
        expected = 0
        actual = vowel_counter(input)
        self.assertEqual(expected, actual)

# Localization
    def test_russian_word(self):
        word = "корова"

        # self.assertEqual(, vowel_counter(word))
        self.assertRaises(ValueError, lambda : vowel_counter(word))


    def test_no_vowel_input(self):
        word = "sddSSDS"

    def test_empty_input(self):
        word = ""
        self.assertEqual(0, vowel_counter(word))

    # negative test

    def test_object_input(self):
        obj = object()
        self.assertEqual(0, vowel_counter(obj))





class MyTestCase(unittest.TestCase):
    def test_word(self):
        self.assertEqual(2, vowel_counter('password'))
        print(vowel_counter('password'))


    def test_word_plus_symbol(self):
        self.assertEqual(1, vowel_counter('big??_'))
        print(vowel_counter('big??_'))

    def test_word_plus_symbols(self):
        self.assertEqual(1, vowel_counter('big??_'))
        print(vowel_counter('big??_'))

    def test_empty(self):
        self.assertEqual(0, vowel_counter(' '))
        print(vowel_counter(' '))

    def test_symbols(self):
        self.assertEqual(0, vowel_counter('?><_@#$'))
        print(vowel_counter('?><_@#$'))



    # corrected
    def test_assertFalse(self):
        result = vowel_counter('Ø∏ˆ¨ˇ◊˜Â')
        self.assertFalse(0, result)
        # the test failed in case  :
        # self.assertFalse(1, result)

        print(vowel_counter(result))


    # Added

    def test_digits_letters_search(self):
        mess = 123 + vowel_counter('letters')
        self.assertEqual(125, mess)
        print(mess)

    def test_float_letters(self):
        self.assertEqual(0, vowel_counter(float(1.676764)))
        print(vowel_counter(float(1.676764)))

    def test_digits(self):
        self.assertEqual(0, vowel_counter(int(4567890)))
        print(vowel_counter(int(4567890)))

    def test_non_english_symbols(self):
        self.assertEqual(0, vowel_counter('æàâäāå'))
        print(vowel_counter('æàâäāå'))

#     Try to use new assertions

    def test_assert_greater_equal(self):
        self.assertGreaterEqual(9, vowel_counter('iuiuiuiui'))
        # in case 8 and less self.assertGreaterEqual(8, vowel_counter('iuiuiuiui')) ==>failed
        print(vowel_counter('iuiuiuiui'))

    def test_assert_is(self):
        self.assertIs(9, vowel_counter('iuiuiuiui'))
        # in case 8 and less self.assertGreaterEqual(8, vowel_counter('iuiuiuiui')) ==>failed
        print(vowel_counter('iuiuiuiui'))

    def test_assert_is_not(self):
        self.assertIsNot(15, vowel_counter('iuiuiuiui'))
        # in case 9 ==> failed
        print(vowel_counter('iuiuiuiui'))


    def test_assert_in(self):
        symbol ='a'
        self.assertIn(symbol, set("aeiou"))
        # if symbol ='b' => failed
        print('The symbol [ ' + symbol + ' ] include in ' + "[ aeiou ]" )

# class TestVowelCount(unittest.TestCase):
    #positive


    # def test_sentence(self):
    #     sentence = "It is  great Tuesdy evening"
    #     actual = vowel_counter(sentence)
    #     expected = 10
    #     self.assertTrue(expected == actual)

      #  self.assertTrue(10 == vowel_counter("It is  great Tuesdy evening"))