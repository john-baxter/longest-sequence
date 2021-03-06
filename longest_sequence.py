ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def find_longest_sequence(origin_string):
  # disallowed_letters = "z"
  # for character in disallowed_letters:
  #   origin_string = origin_string.replace(character, "")
  
  index_difference_list = get_index_difference(origin_string)
  (index_of_ones, len_of_string_of_ones) = get_index_of_ones(index_difference_list)

  return origin_string

def get_index_difference(origin_string):
  """
    FOR LOOP
      get origin_string[i] 
      find that letter in ALPHABET
      get the index of that letter

      get origin_string[i+1]
      find that letter in ALPHABET
      get the index of that letter

      subtract one index from the other (make sure of the correct order)
      add this integer into a new list
    END FOR
  """
  index_difference_list = []
  for i in range(len(origin_string) - 1):
    index_difference_list.append(
      ALPHABET.index(origin_string[i + 1]) -
      ALPHABET.index(origin_string[i])
    )

  return index_difference_list

def get_index_of_ones(index_difference_list):
  index_diff_as_string = "".join(str(i) for i in index_difference_list)
  big_string_of_ones = "".join('1' for i in index_difference_list)

  while len(big_string_of_ones) > 0:
    if big_string_of_ones in index_diff_as_string:
      index_of_ones = index_diff_as_string.index(big_string_of_ones)
      return (index_of_ones, len(big_string_of_ones))
    else:
      big_string_of_ones = big_string_of_ones[:-1]

# def get_index_of_ones(index_difference_list):
#   index_diff_as_string = "".join(str(i) for i in index_difference_list)
#   big_string_of_ones = "".join('1' for i in index_difference_list)
#   while len(big_string_of_ones) > 0:
#     if big_string_of_ones in index_diff_as_string:
#       index_of_ones = index_diff_as_string.index(big_string_of_ones)
#       return (index_of_ones, len(big_string_of_ones))
#     else:
#       big_string_of_ones = big_string_of_ones[:-1]
