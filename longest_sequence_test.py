import unittest
from unittest import mock
from unittest.mock import patch, call
import longest_sequence


class LongestSequenceTest(unittest.TestCase):
  # def test_longest_sequence_returns_a_when_input_is_a(self):
  #   test_origin_string = "a"
  #   expected_result = "a"
  #   actual_result = longest_sequence.find_longest_sequence(test_origin_string)
  #   self.assertEqual(actual_result, expected_result)

  # def test_longest_sequence_returns_ab_when_input_is_ab(self):
  #   test_origin_string = "ab"
  #   expected_result = "ab"
  #   actual_result = longest_sequence.find_longest_sequence(test_origin_string)
  #   self.assertEqual(actual_result, expected_result)
  
  # def test_longest_sequence_returns_ab_when_input_is_abz(self):
  #   test_origin_string = "abz"
  #   expected_result = "ab"
  #   actual_result = longest_sequence.find_longest_sequence(test_origin_string)
  #   self.assertEqual(actual_result, expected_result)
  
  # def test_longest_sequence_returns_ab_when_input_is_zab(self):
  #   test_origin_string = "zab"
  #   expected_result = "ab"
  #   actual_result = longest_sequence.find_longest_sequence(test_origin_string)
  #   self.assertEqual(actual_result, expected_result)

  # def test_check_longest_sequence_returns_abc_when_input_is_abc(self):
  #   test_origin_string = "abc"
  #   expected_result = "abc"
  #   actual_result = longest_sequence.find_longest_sequence(test_origin_string)
  #   self.assertEqual(actual_result, expected_result)
  
  # def test_longest_sequence_returns_abcd_when_input_is_zabczzabcdz(self):
  #   test_origin_string = "zabczzabcdz"
  #   expected_result = "abcd"
  #   actual_result = longest_sequence.find_longest_sequence(test_origin_string)
  #   self.assertEqual(actual_result, expected_result)

  @patch('longest_sequence.get_index_difference')  
  def test_longest_sequence_calls_get_index_difference_returns_a_when_input_is_a(self, mock_call_get_index_difference):
      manager = mock.Mock()
      manager.attach_mock(mock_call_get_index_difference, 'mock_call_get_index_difference')
      test_origin_string = "a"
      # actual_result = longest_sequence.find_longest_sequence(test_origin_string)
      longest_sequence.find_longest_sequence(test_origin_string)
      expected_mock_call = [mock.call.mock_call_get_index_difference(test_origin_string)]
      self.assertEqual(manager.mock_calls, expected_mock_call)
      mock_call_get_index_difference.assert_called_once()



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
    
class GetIndexOfOnesSequenceTest(unittest.TestCase):
  # def test_get_index_of_ones_returns_list(self):
  #   test_index_difference_list = []
  #   actual_result = longest_sequence.get_index_of_ones(test_index_difference_list)
  #   self.assertIsInstance(actual_result, int)

  def test_get_index_of_ones_returns_1_for_0_1(self):
    test_index_difference_list = [0, 1]
    expected_result = 1
    actual_result = longest_sequence.get_index_of_ones(test_index_difference_list)
    self.assertEqual(actual_result[0], expected_result)

  def test_get_index_of_ones_returns_2_for_0_0_1(self):
    test_index_difference_list = [0, 0, 1]
    expected_result = 2
    actual_result = longest_sequence.get_index_of_ones(test_index_difference_list)
    self.assertEqual(actual_result[0], expected_result)

  def test_get_index_of_ones_returns_3_for_0_1_0_1_1(self):
    test_index_difference_list = [0, 1, 0, 1, 1]
    expected_result = 3
    actual_result = longest_sequence.get_index_of_ones(test_index_difference_list)
    self.assertEqual(actual_result[0], expected_result)

  def test_get_index_of_ones_returns_4_for_0_1_1_0_1_1_1(self):
    test_index_difference_list = [0, 1, 1, 0, 1, 1, 1]
    expected_result = 4
    actual_result = longest_sequence.get_index_of_ones(test_index_difference_list)
    self.assertEqual(actual_result[0], expected_result)
    
  def test_get_index_of_ones_returns_length_of_1_for_0_1(self):
    test_index_difference_list = [0, 1]
    expected_result = 1
    actual_result = longest_sequence.get_index_of_ones(test_index_difference_list)
    self.assertEqual(actual_result[1], expected_result)

  def test_get_index_of_ones_returns_length_of_3_for_0_1_0_1_1(self):
    test_index_difference_list = [0, 1, 0, 1, 1]
    expected_result = 2
    actual_result = longest_sequence.get_index_of_ones(test_index_difference_list)
    self.assertEqual(actual_result[1], expected_result)

  def test_check_get_index_of_ones_returns_length_of_4_for_0_1_1_0_1_1_1(self):
    test_index_difference_list = [0, 1, 1, 0, 1, 1, 1]
    expected_result = 3
    actual_result = longest_sequence.get_index_of_ones(test_index_difference_list)
    self.assertEqual(actual_result[1], expected_result)


  





if __name__ == '__main__':
  unittest.main(verbosity=2)
