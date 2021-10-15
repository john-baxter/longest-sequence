import unittest
import longest_sequence

class LongestSequenceTest(unittest.TestCase):
  def test_longest_sequence_returns_a_when_input_is_a(self):
    test_origin__string = "a"
    expected_result = "a"
    actual_result = longest_sequence.find_longest_sequence(test_origin__string)
    self.assertEqual(actual_result, expected_result)

  def test_longest_sequence_returns_ab_when_input_is_ab(self):
    test_origin__string = "ab"
    expected_result = "ab"
    actual_result = longest_sequence.find_longest_sequence(test_origin__string)
    self.assertEqual(actual_result, expected_result)
  
  def test_longest_sequence_returns_abz_when_input_is_abz(self):
    test_origin__string = "abz"
    expected_result = "ab"
    actual_result = longest_sequence.find_longest_sequence(test_origin__string)
    self.assertEqual(actual_result, expected_result)
  
  def test_longest_sequence_returns_zab_when_input_is_zab(self):
    test_origin__string = "zab"
    expected_result = "ab"
    actual_result = longest_sequence.find_longest_sequence(test_origin__string)
    self.assertEqual(actual_result, expected_result)

  def test_check_longest_sequence_returns_abc_when_input_is_abc(self):
    test_origin__string = "abc"
    expected_result = "abc"
    actual_result = longest_sequence.find_longest_sequence(test_origin__string)
    self.assertEqual(actual_result, expected_result)
  
  def test_longest_sequence_returns_abcd_when_input_is_zabczzabcdz(self):
    test_origin__string = "zabczzabcdz"
    expected_result = "abcd"
    actual_result = longest_sequence.find_longest_sequence(test_origin__string)
    self.assertEqual(actual_result, expected_result)





if __name__ == '__main__':
  unittest.main(verbosity=2)
