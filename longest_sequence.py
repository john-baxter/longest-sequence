ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def find_longest_sequence(origin_string):
  disallowed_letters = "z"
  for character in disallowed_letters:
    origin_string = origin_string.replace(character, "")
  
  return origin_string


def get_index_difference(origin_string):
  index_difference_list = []
  for i in range(len(origin_string) - 1):
    
    # # print letter at position i in origin_string
    # print(origin_string[i])

    # # print alphabet index of THIS
    # print(ALPHABET.index(origin_string[i]))

    # # print alphabet index of NEXT letter in origin_string
    # print(ALPHABET.index(origin_string[i+1]))

    index_difference_list.append(
      ALPHABET.index(origin_string[i+1]) - 
      ALPHABET.index(origin_string[i])
    )

  return index_difference_list

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

    return the new list
  """
  
  # if origin_string == "abz":
  #   return [1, 22]
  # elif origin_string == "zab":
  #   return [23, 1]
  # else:
  #   return [1]


if __name__ == '__main__':
  print(get_index_difference("zab"))