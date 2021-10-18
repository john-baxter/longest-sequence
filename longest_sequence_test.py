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

  def test_index_difference_returns_1_22_if_given_abz(self):
    test_origin_string = "abz"
    expected_result = [1, 22]
    actual_result = longest_sequence.get_index_difference(test_origin_string)
    self.assertEqual(actual_result, expected_result)

  def test_index_difference_returns_23_1_if_given_zab(self):
    test_origin_string = "zab"
    expected_result = [23, 1]
    actual_result = longest_sequence.get_index_difference(test_origin_string)
    self.assertEqual(actual_result, expected_result)







if __name__ == '__main__':
  unittest.main(verbosity=2)
