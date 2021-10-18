import unittest
import longest_sequence

class LongestSequenceTest(unittest.TestCase):
  def test_longest_sequence_returns_a_when_input_is_a(self):
    test_origin_string = "a"
    expected_result = "a"
    actual_result = longest_sequence.find_longest_sequence(test_origin_string)
    self.assertEqual(actual_result, expected_result)

  def test_longest_sequence_returns_ab_when_input_is_ab(self):
    test_origin_string = "ab"
    expected_result = "ab"
    actual_result = longest_sequence.find_longest_sequence(test_origin_string)
    self.assertEqual(actual_result, expected_result)
  
  def test_longest_sequence_returns_ab_when_input_is_abz(self):
    test_origin_string = "abz"
    expected_result = "ab"
    actual_result = longest_sequence.find_longest_sequence(test_origin_string)
    self.assertEqual(actual_result, expected_result)
  
  def test_longest_sequence_returns_ab_when_input_is_zab(self):
    test_origin_string = "zab"
    expected_result = "ab"
    actual_result = longest_sequence.find_longest_sequence(test_origin_string)
    self.assertEqual(actual_result, expected_result)

  def test_check_longest_sequence_returns_abc_when_input_is_abc(self):
    test_origin_string = "abc"
    expected_result = "abc"
    actual_result = longest_sequence.find_longest_sequence(test_origin_string)
    self.assertEqual(actual_result, expected_result)
  
  # def test_longest_sequence_returns_abcd_when_input_is_zabczzabcdz(self):
  #   test_origin_string = "zabczzabcdz"
  #   expected_result = "abcd"
  #   actual_result = longest_sequence.find_longest_sequence(test_origin_string)
  #   self.assertEqual(actual_result, expected_result)

class GetIndexDifferenceTest(unittest.TestCase):
  def test_index_difference_return(self):
      test_origin_string = ""
      actual_result = longest_sequence.get_index_difference(test_origin_string)
      self.assertIsInstance(actual_result, list)
  
  def test_index_difference_return_1_if_given_ab(self):
    test_origin_string = "ab"
    expected_result = [1]
    actual_result = longest_sequence.get_index_difference(test_origin_string)
    self.assertEqual(actual_result, expected_result)

  def test_index_difference_returns_1_24_if_given_abz(self):
    test_origin_string = "abz"
    expected_result = [1, 24]
    actual_result = longest_sequence.get_index_difference(test_origin_string)
    self.assertEqual(actual_result, expected_result)

  def test_index_difference_returns_25_1_if_given_zab(self):
    test_origin_string = "zab"
    expected_result = [-25, 1]
    actual_result = longest_sequence.get_index_difference(test_origin_string)
    self.assertEqual(actual_result, expected_result)

  def test_check_longer_strings(self):
    test_origin_string_one = "zabczzabcdz"
    test_origin_string_two = "yabcyyabcdy"
    expected_result_one = [-25, 1, 1, 23, 0, -25, 1, 1, 1, 22]
    expected_result_two = [-24, 1, 1, 22, 0, -24, 1, 1, 1, 21]
    actual_result_one = longest_sequence.get_index_difference(test_origin_string_one)
    actual_result_two = longest_sequence.get_index_difference(test_origin_string_two)
    self.assertEqual(actual_result_two, expected_result_two)
    self.assertEqual(actual_result_one, expected_result_one)
    







if __name__ == '__main__':
  unittest.main(verbosity=2)
