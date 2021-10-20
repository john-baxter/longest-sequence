ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def find_longest_sequence(origin_string):
  disallowed_letters = "z"
  for character in disallowed_letters:
    origin_string = origin_string.replace(character, "")
  
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
  if "11" in index_diff_as_string:
    return index_diff_as_string.index("11")
  else:
    return index_difference_list.index(1)